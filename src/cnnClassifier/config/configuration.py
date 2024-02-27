import os 
from cnnClassifier.constants import * 
from cnnClassifier.utils.common import read_yaml,create_directories
from cnnClassifier.entity.entity_config import (DataIngestionConfig,PrepareBaseModelConfig,TrainModelConfig)

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
    
    def  get_prepare_base_model_config(self)->PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        params = self.param
        create_directories([config.root_dir])
        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=config.root_dir,
            base_model_path=config.base_model_path,
            updated_base_model_path=config.updated_base_model_path,
            params_image_size=params.IMAGE_SIZE,
            params_learning_rate=params.LEARNING_RATE,
            params_include_top=params.INCLUDE_TOP,
            params_weights=params.WEIGHTS,
            params_classes=params.CLASSES
        )
        return prepare_base_model_config  
    

    def get_training_config(self)->TrainModelConfig:
        training = self.config.training 
        params = self.param 
        prepare_base_model = self.config.prepare_base_model 
        create_directories([training.root_dir])
        training_data = os.path.join(self.config.data_ingestion.unzip_file,'Chest-CT-Scan-data')
        training_config = TrainModelConfig(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            updated_trained_model_path=Path(prepare_base_model.updated_base_model_path),
            training_data=Path(training_data),
            params_batch_size=params.BATCH_SIZE,
            params_epochs=params.EPOCHS,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE)
        return training_config 

    