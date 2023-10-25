import os
import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformation()

    def get_data_transformer_object(self):
        """
        This function does data transformation with pipeline
        """
        try:
            numerical_columns=["writing_score", "reading_score"]
            categorical_columns=[
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course"
            ]

            num_pipline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")), #handles missing values
                    ("scaler", StandardScaler())
                ]
            )

            cat_pipline = Pipeline(

                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder", OneHotEncoder()),
                    ("scaler", StandardScaler())
                ]
            )

            logging.info("Numerical columns standart scaling completed")

            logging.info("Categorical columns encoding completed")

            preprocessing = ColumnTransformer(
                [
                    ("num_pipeline", num_pipline, numerical_columns),
                    ("cat_pipeline", cat_pipline, categorical_columns)

                ]
            )

            return preprocessing
        
        except Exception as e:
            raise CustomException(e, sys)
        
    def initiate_date_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Train and test data reading is completed")

            logging.info("Obtaining preprocessing object")

            preprocessing_obj=self.get_data_transformer_object()

            target_column_name = "math_score"
        except:
            pass