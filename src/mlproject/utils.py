import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score
import pymysql

import pickle
import numpy as np 

load_dotenv()


host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv('db')



def read_sql_data():
    
    logging.info("Reading SQL database started")
    
    try:
        
        mydb=pymysql.connect(
            host = host,
            user=user,
            password=password,
            db=db
        )
        logging.info(f"Loaded credentials - Host: {host}, User: {user}, DB: {db}")
        logging.info(f"Connection Established: {mydb}")
        df=pd.read_sql_query("Select * from students ",mydb)
        print(df.head())
        return df
    
    
    except Exception as ex:
        raise CustomException(ex)
    
def evaluate_models(X_train, y_train,X_test,y_test,models,param):
    try:
        report = {}
        for i in range(len(list(models))):
            model_name = list(models.keys())[i]
            model = list(models.values())[i]
            
            para = param[list(models.keys())[i]]
            logging.info(f"Evaluating model: {model_name} with parameters: {para}")
            
            try:
                
                gs = GridSearchCV(model,para,cv=3)
                gs.fit(X_train,y_train)
                model.set_params(**gs.best_params_)
                model.fit(X_train,y_train)
            
            except Exception as e:
                logging.warning(f"Error with {model_name} during fitting: {str(e)}")
                continue
            
                
            #model.fit(X_train, y_train)  # Train model
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)
            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)
            report[list(models.keys())[i]] = test_model_score
            
        logging.info("Model evaluation completed.")
            
        return report
    except Exception as e:
        
        logging.error(f"Error during model evaluation: {str(e)}")
        
        raise CustomException(e, sys)
   
    
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        
        os.makedirs(dir_path, exist_ok = True)
        
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
    
    except Exception as e:
        raise CustomException(e, sys)            