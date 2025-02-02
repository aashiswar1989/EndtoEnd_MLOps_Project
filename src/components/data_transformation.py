import pandas as pd
import numpy as np
import os
import sys
from dataclasses import dataclass
from pathlib import Path

from src.logger.logging import logging
from src.exception.exception import CustomException
from src.utils.utils import save_object

from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


@dataclass
class DataTransformationConfig:
    preprocessor_obj_path = Path('artifacts')/'preprocessor.pkl'

class DataTransformation:
    
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation(self, numerical_cols, categorical_cols):
        
        try:
            logging.info('Data Transformation initiated')
            
            # Define which columns should be ordinal-encoded and which should be scaled
            # categorical_cols = cat_cols
            # numerical_cols = num_cols
            
            # Define the custom ranking for each ordinal variable
            cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']
            
            logging.info('Pipeline Initiated')
            
            ## Numerical Pipeline
            num_pipeline=Pipeline(
                steps=[
                ('imputer',SimpleImputer(strategy='median')),
                ('scaler',StandardScaler())
                ]

            )
            
            # Categorical Pipeline
            cat_pipeline=Pipeline(
                steps=[
                ('imputer',SimpleImputer(strategy='most_frequent')),
                ('ordinalencoder',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories]))
                ]

            )
            
            preprocessor=ColumnTransformer([
            ('num_pipeline',num_pipeline,numerical_cols),
            ('cat_pipeline',cat_pipeline,categorical_cols)
            ])
            
            return preprocessor
            
        except Exception as e:
            logging.info("Exception occured in the initiate_datatransformation")

            raise CustomException(e,sys)

    def init_data_transformation(self, train_data_path, test_data_path):
        try:
            logging.info('Data transformation started')

            train_df = pd.read_csv(train_data_path)
            test_df = pd.read_csv(test_data_path)
            logging.info("Training and Test data read successfully")

            num_cols = train_df.select_dtypes(exclude='object').columns
            cat_cols = train_df.select_dtypes(include='object').columns
            preprocessor_obj = self.get_data_transformation(numerical_cols=num_cols, categorical_cols=cat_cols)
            logging.info("Preporcessor object creation finished")

            X_train = train_df.drop(labels=['price', 'id'], axis = 1)
            y_train = train_df['price']

            X_test = test_df.drop(labels = ['price', 'id'], axis = 1)
            y_test = test_df['price']

            
            X_train_arr = preprocessor_obj.fit_transform(X_train)
            X_test_arr = preprocessor_obj.fit(X_test)
            logging.info("Preprocessing on train and test data finished")

            train_arr = np.c_[X_train_arr, np.array(y_train)]
            test_arr = np.c_[X_test_arr, np.array(y_test)]

            save_object(file_path=self.data_transformation_config.preprocessor_obj_path,
                        obj= preprocessor_obj)
            logging.info("Preprocessing object saved in pkl format")
            
            return (
                train_arr, 
                test_arr
                )

        except Exception as e:
            raise CustomException(e, sys)            