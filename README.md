# Student Performance Analysis

![DagsHub](https://github.com/38832/mlproject/blob/d8d00b957f5640452f96cd0259049111a52fec4a/assets/dagshub.png)


## Project Overview
This project conducts a comprehensive analysis of student performance using a dataset extracted from a MySQL database. It adheres to the complete data science lifecycle, encompassing data ingestion, preprocessing, model development, evaluation, and deployment. Advanced tools such as MLflow and DVC are utilized for experiment tracking and data versioning, ensuring a reproducible and efficient workflow. Version control is maintained via Git and GitHub, providing a clear audit trail of project progress through iterative commits.

The objective is to leverage machine learning algorithms to forecast academic performance, enabling proactive interventions and data-driven educational strategies.

---

## Technologies Used

### Data Science Tools
|                                                                                                    |                                                                                                    |                                                                                                    |
|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| ![MLflow](https://github.com/38832/mlproject/blob/d8d00b957f5640452f96cd0259049111a52fec4a/assets/mlfow.png) | ![DVC](https://github.com/38832/mlproject/blob/d8d00b957f5640452f96cd0259049111a52fec4a/assets/dvc.png) | ![Pandas](https://github.com/38832/mlproject/blob/d8d00b957f5640452f96cd0259049111a52fec4a/assets/pandas.png) |
| **MLflow** for experiment tracking                                                                 | **DVC** for data version control                                                                   | **Pandas** for data manipulation                                                                   |
|                                                                                                    |                                                                                                    |                                                                                                    |
| ![NumPy](https://github.com/38832/mlproject/blob/d8d00b957f5640452f96cd0259049111a52fec4a/assets/numpy.png) | ![Matplotlib](https://github.com/38832/mlproject/blob/d8d00b957f5640452f96cd0259049111a52fec4a/assets/matplotlib.png) | ![MySQL](https://github.com/38832/mlproject/blob/d8d00b957f5640452f96cd0259049111a52fec4a/assets/mysqllogo.png) |
| **NumPy** for numerical computations                                                               | **Matplotlib** for data visualization                                                              | **MySQL** for data storage and retrieval                                                           |


---

## Table of Contents
1. [Introduction](#introduction)
2. [Technologies Used](#technologies-used)
3. [Data Ingestion](#data-ingestion)
4. [Data Transformation](#data-transformation)
5. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
6. [Model Training](#model-training)
7. [Results](#results)
8. [DagsHub Experiments](#dagshub-experiments)
9. [MLflow Tracking](#mlflow-tracking)
10. [Conclusion](#conclusion)

---

## Introduction
This project aims to implement predictive analytics to model student performance using machine learning. By adhering to a structured data science workflow, we systematically approach data handling, model development, and evaluation. The project serves as a practical application of machine learning methodologies in educational data mining.

---

## Data Ingestion
Data was ingested from a MySQL database into a Pandas DataFrame. This process involved querying the database, handling data types, and ensuring consistency in the data structure for further analysis.

---

## Data Transformation
The transformation phase included rigorous data preprocessing. Tasks such as handling One Hot Encodng, normalizing data, and performing feature engineering were executed. This step is critical for enhancing model performance and ensuring data quality.

---

## Exploratory Data Analysis (EDA)
EDA was conducted using Matplotlib and Seaborn, focusing on statistical summaries and visualizations. Insights were drawn regarding data distribution, correlations, and potential anomalies, which guided the feature selection and model development process.

---

## Model Training
Various machine learning models were trained, including Linear Regression, Decision Trees, XGBregessor, Random Forest Regressor, AdaBoost, and CatBoost. A GridSearchCV was applied to all models for hyperparameter tuning to identify the best configuration for each. After evaluating the performance of all models, Linear Regression emerged as the best performer, delivering the highest accuracy and lowest error metrics among the tested algorithms.

---

## Results
Performance metrics of the Linear Regression model include:

- **RMSE**: 5.39
- **R² Score**: 0.88
- **MAE**: 4.21

These metrics underscore the model's predictive accuracy and robustness in handling the dataset.

---

## DagsHub Experiments
![DagsHub Experiments](https://github.com/38832/mlproject/blob/e8bf6321024896840f6e291e9b5c683594eef93c/dagshubexp.png)

DagsHub was utilized for experiment tracking and collaborative development. This platform enabled efficient version control and seamless collaboration among team members.

---

## MLflow Tracking
The project employed MLflow for comprehensive experiment tracking. Below are the configuration details for MLflow:

- **MLFLOW_TRACKING_URI**: `https://dagshub.com/38832/mlproject.mlflow`
- **MLFLOW_TRACKING_USERNAME**: `38832`
- **MLFLOW_TRACKING_PASSWORD**: `ed5a6942f3480d84b1bbd6bfccba8e3c5fbc9195`

MLflow ensured a streamlined tracking process, capturing all model parameters, metrics, and artifacts, thereby facilitating reproducibility and transparency.

---

## Conclusion
The project provided a detailed analysis of factors influencing student performance and demonstrated the applicability of machine learning in educational settings. The insights gained and the models developed can be leveraged for targeted interventions and strategic decision-making in educational institutions. Future work will focus on expanding the dataset and integrating additional predictive features to further enhance model accuracy.
