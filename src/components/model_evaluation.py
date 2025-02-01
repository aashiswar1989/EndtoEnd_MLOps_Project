import pandas as pd
import numpy as np
import os
import sys
from dataclasses import dataclass
from pathlib import Path
import pickle
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn

from src.logger.logging import logging
from src.exception.exception import CustomException
from src.utils.utils import load_object

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score

@dataclass
class ModelEvaluationConfig:
    pass

class ModelEvaluation:
    def __init__(self):
        pass

    def init_model_evaluation(self):
        try:
            pass

        except Exception as e:
            raise CustomException(e, sys)            