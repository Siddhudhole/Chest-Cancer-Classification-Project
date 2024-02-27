import os 
from cnnClassifier.constants import * 
from cnnClassifier.utils.common import read_yaml,create_directories
from cnnClassifier.entity.entity_config import (DataIngestionConfig)

class ConfigurationManager():
    def __init__(self,config_filepath=CONFIG_FILE_PATH,param_filepath=PARAMS_FILE_PATH):

        self.config = read_yaml(CONFIG_FILE_PATH) 
        self.param = read_yaml(PARAMS_FILE_PATH) 



    def get_data_ingestion_config(self)->DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir]) 

        data_ingestion_config =DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL = config.source_URL,
            local_data_file = config.local_data_file,
            unzip_file = config.unzip_file 
        )

        return data_ingestion_config 