from cnnClassifier import logger 
from cnnClassifier.config.configuration import ConfigurationManager 
from cnnClassifier.components.prepare_model import PrepareBaseModel 


Stage_name = 'Prepare Base Model'

class PrepareBaseModelTrainigPipeline:
    def __init__(self):
        pass 

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.upadte_base_model()

if __name__ == '__main__':
    try :
        logger.info(f"****************************************************************")
        logger.info(f">>>>>> stage {Stage_name} started <<<<<<")
        obj = PrepareBaseModelTrainigPipeline()
        obj.main()
        logger.info(f">>>>>> stage {Stage_name} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e 