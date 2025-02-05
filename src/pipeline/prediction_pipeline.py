import sys
from pathlib import Path
import pandas as pd
from src.exception.exception import CustomException
from src.logger.logging import logging
from src.utils.utils import load_object

class PredictPipeline:

    def predict(self, features):
        try:
            preprocessor_path = Path('artifacts')/'preprocessor.pkl'
            model_path = Path('artifacts')/'model.pkl'

            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)
            logging.info("Preprocessor and Model objects are loaded")

            preprocessed_features = preprocessor.transform(features)
            pred = model.predict(preprocessed_features)

            return pred

        except Exception as e:
            raise CustomException(e, sys)
        

class CustomData:
    def __init__(self,
                 carat:float,
                 depth:float,
                 table:float,
                 x:float,
                 y:float,
                 z:float,
                 cut:str,
                 color:str,
                 clarity:str):
        
        self.carat=carat
        self.depth=depth
        self.table=table
        self.x=x
        self.y=y
        self.z=z
        self.cut = cut
        self.color = color
        self.clarity = clarity
            
    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'carat':[self.carat],
                'depth':[self.depth],
                'table':[self.table],
                'x':[self.x],
                'y':[self.y],
                'z':[self.z],
                'cut':[self.cut],
                'color':[self.color],
                'clarity':[self.clarity]
                }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise CustomException(e,sys)