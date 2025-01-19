# Student Performance Analysis

![dagshub](https://github.com/user-attachments/assets/0fdead23-46be-45e2-83bc-74b18b32b0d9)

## Project Overview
This project conducts a comprehensive analysis of student performance using a dataset extracted from a MySQL database. It adheres to the complete data science lifecycle, encompassing data ingestion, preprocessing, model development, evaluation, and deployment. Advanced tools such as MLflow and DVC are utilized for experiment tracking and data versioning, ensuring a reproducible and efficient workflow. Version control is maintained via Git and GitHub, providing a clear audit trail of project progress through iterative commits.

The objective is to leverage machine learning algorithms to forecast academic performance, enabling proactive interventions and data-driven educational strategies.

---

## Technologies Used

### Data Science Tools
|                                                                                                    |                                                                                                    |                                                                                                    |
|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| ![mlflow](https://github.com/user-attachments/assets/76bc4e91-838a-4a65-8dfe-75f77208b4c5)         | ![dvc](https://github.com/user-attachments/assets/458f699e-fb23-458c-a10a-2a1c6f1079f5)            | ![pandas](https://github.com/user-attachments/assets/7456f031-ea96-4373-9743-a87a87369596)         |
| **MLflow** for experiment tracking                                                                 | **DVC** for data version control                                                                   | **Pandas** for data manipulation                                                                   |
|                                                                                                    |                                                                                                    |                                                                                                    |
| ![numpy](https://github.com/user-attachments/assets/df1fa382-b8bb-440e-b337-2447e0b1f463)          | ![matplotlib](https://github.com/user-attachments/assets/e1c79058-4005-49f8-9441-c1908bc851ed)     | ![mysql](https://github.com/user-attachments/assets/3c8bcf09-3acb-4d4b-8331-0bbc1ef08faa)          |
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
![DagsHub Experiments](https://github.com/user-attachments/assets/deae8657-6b73-4926-9c89-8b924d8d7500)

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
