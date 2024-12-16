import os
import sys
import pandas as pd
from icecream import ic
from sklearn.model_selection import train_test_split
from src.utils import unzipping_file
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join("artifacts", "data.csv")
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):

        logging.info("Data ingestion initiated.")
        
        try:
            unzipping_file("data\scfp2019excel.zip")
            df=pd.read_csv(r"data\SCFP2019.csv")
            
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.train_data_path, index=False, header=True)

            logging.info("Splitting the dataset.")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            logging.info("Saving train and test sets.")
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Data ingestion complete.")

            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path
            
        except Exception as e:
            raise CustomException(e, sys)

if __name__=="__main__":

    obj = DataIngestion()
    train_set, test_set = obj.initiate_data_ingestion()
    
   