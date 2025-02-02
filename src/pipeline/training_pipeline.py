from src.exception.exception import CustomException
from src.logger.logging import logging
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

if __name__ == '__main__':

    # Data ingestion
    data_ing_obj = DataIngestion()
    train_path, test_path = data_ing_obj.init_data_ingestion()

    # Data transformation
    data_transform_obj = DataTransformation()
    train_arr, test_arr = data_transform_obj.init_data_transformation(train_path, test_path)

    # Model training
    model_train_obj = ModelTrainer()
    model_train_obj.init_model_training(train_arr, test_arr)