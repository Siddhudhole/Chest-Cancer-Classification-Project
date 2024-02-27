import os 
import sys 
from cnnClassifier.components.data_ingestion import DataIngestion  
from cnnClassifier.utils.common import read_yaml
from cnnClassifier.constants import * 
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_model import PrepareBaseModel 


if __name__ == '__main__':
    try :

        config = ConfigurationManager()
        prepare_base_model_config =config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.upadte_base_model()
    except Exception as e:
        raise e 