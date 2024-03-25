import os 
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')

class DataIngestion:
    def __init__(self):
        self.ingestionConfig=DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Data ingestion has started")
        try:
            df_train=pd.read_csv(r'notebook\data\train.csv')# This is were data import is done from mongodb or other servers
            df_test=pd.read_csv(r'notebook\data\test.csv')
            os.makedirs(os.path.dirname(self.ingestionConfig.train_data_path),exist_ok=True)
            os.makedirs(os.path.dirname(self.ingestionConfig.test_data_path),exist_ok=True)
            df_train.to_csv(self.ingestionConfig.train_data_path,index=False,header=True)
            df_test.to_csv(self.ingestionConfig.test_data_path,index=False,header=True)
            logging.info('Importing the dataset completed')
            return (
                self.ingestionConfig.train_data_path,
                self.ingestionConfig.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)

if(__name__=="__main__"):
    obj=DataIngestion()
    obj.initiate_data_ingestion()