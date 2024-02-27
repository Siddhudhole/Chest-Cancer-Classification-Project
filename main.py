from cnnClassifier import logger 

from cnnClassifier.pipeline.stage_01_data_ingestion_pip import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model_pip import PrepareBaseModelTrainigPipeline 
from cnnClassifier.pipeline.stage_03_model_training_pip import ModelTrainingPipeline 

stage_1_name ='Data Ingestion Stage'
stage_2_name ='Prepare Base Model'

try :
    logger.info(f">>>>>> stage {stage_1_name} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {stage_1_name} completed <<<<<<\n\nx==========x")
except Exception as e :
    logger.exception(e)
    raise e 

try:
    logger.info(f">>>>>> stage {stage_2_name} started <<<<<<")
    obj = PrepareBaseModelTrainigPipeline()
    obj.main()
    logger.info(f">>>>>> stage {stage_2_name} completed <<<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e

stage_3_name = 'Training'

try :
    logger.info(f"****************")
    logger.info(f">>>>>> stage {stage_3_name} started <<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {stage_3_name} completed <<<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e