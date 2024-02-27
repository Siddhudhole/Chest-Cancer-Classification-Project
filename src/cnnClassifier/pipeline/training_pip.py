import os 
import sys 
from cnnClassifier.components.data_ingestion import DataIngestion  
from cnnClassifier.utils.common import read_yaml
from cnnClassifier.constants import * 
from cnnClassifier.config.configuration import ConfigurationManager 


if __name__ == '__main__':
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config() 
    data_ing = DataIngestion(data_ingestion_config) 
    # data_ing.download_file()
    data_ing.extract_zip_file()