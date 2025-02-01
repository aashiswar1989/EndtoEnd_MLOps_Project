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
    pass

class ModelTrainer:
    def __init__(self):
        pass

    def init_model_training(self):
        try:
            pass

        except Exception as e:
            raise CustomException(e, sys)            