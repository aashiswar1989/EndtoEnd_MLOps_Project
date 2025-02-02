import pandas as pd
import numpy as np
import os
import sys
from dataclasses import dataclass
from pathlib import Path

from src.logger.logging import logging
from src.exception.exception import CustomException

from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    raw_data_path = Path('artifacts')/'raw_data.csv'
    train_data_path = Path('artifacts')/'train_data.csv'
    test_data_path = Path('artifacts')/'test_data.csv'
    # raw_data_path = os.path.join('artifacts', 'raw_data.csv')
    # train_data_path = os.path.join('artifacts', 'train_data.csv')
    # test_data_path = os.path.join('artifacts', 'test_data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def init_data_ingestion(self):
        logging.info("Data ingestion started")

        try:
            df = pd.read_csv('gemsotne\\train.csv')
            logging.info('Data read as dataframe')

            if not Path('artifacts').is_dir():
                Path('artifacts').mkdir(parents = True, exist_ok=True)
            # os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)))
            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Raw data saved in artifacts folder")

            df_train, df_test = train_test_split(df, test_size=0.25)
            logging.info("Data split done as train and test")

            df_train.to_csv(self.ingestion_config.train_data_path, index =False)
            df_test.to_csv(self.ingestion_config.test_data_path, index=False)
            logging.info("Data ingestion completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)   

# if __name__ == '__main__':
#     obj = DataIngestion()
#     obj.init_data_ingestion()