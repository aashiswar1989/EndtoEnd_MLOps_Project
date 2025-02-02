import pandas as pd
import numpy as np
import os
import sys
from dataclasses import dataclass
from pathlib import Path

from src.logger.logging import logging
from src.exception.exception import CustomException
from src.utils.utils import save_object, evaluate_model

from sklearn.linear_model import LinearRegression,Lasso,Ridge,ElasticNet
from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor

@dataclass
class ModelTrainerConfig:
    model_obj_path = Path('artifacts')/'model.pkl'

class ModelTrainer:
    def __init__(self):
        self.model_obj_path = ModelTrainerConfig()

    def init_model_training(self, train_arr, test_arr):
        try:
            logging.info("Model training initiated")

            X_train, y_train, X_test, y_test = (
                train_arr[:, -1],
                train_arr[-1],
                test_arr[:, -1],
                test_arr[-1]
            )

            models = {
                'LinearRegression': LinearRegression(),
                'Lasso Regression' : Lasso(),
                'Ridge Regression' : Ridge(),
                'ElasticNet Regression' : ElasticNet(),
                'XGBRegressor'  : XGBRegressor(),
                'RandomForestRegressor' : RandomForestRegressor(),
            }

            model_report:dict = evaluate_model(X_train, y_train, 
                                               X_test, y_test, 
                                               models)
            
            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model = models[best_model_name]

            print(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')
            print('\n====================================================================================\n')
            logging.info(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')
            logging.info('Model training completed.')
            save_object(
                file_path=self.model_obj_path.model_obj_path,
                obj= best_model
            )
            logging.info('Best model object saved')
            
             

        except Exception as e:
            raise CustomException(e, sys)            