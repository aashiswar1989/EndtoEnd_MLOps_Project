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

    def init_data_transformation(self, train_data_path, test_data_path):
        try:
            logging.info('Data transformation started')

            train_df = pd.read_csv(train_data_path)
            test_df = pd.read_csv(test_data_path)

            


        except Exception as e:
            raise CustomException(e, sys)            