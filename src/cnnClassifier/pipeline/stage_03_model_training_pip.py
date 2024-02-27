from cnnClassifier.config.configuration import ConfigurationManager 
from cnnClassifier.components.model_trainer import Training 
from cnnClassifier import logger 



stage_name = "training"

class ModelTrainingPipeline:
    def __init__(self):
        pass 
    
    def main(self): 
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()


if __name__=="__main__": 
    try :
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {stage_name} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e