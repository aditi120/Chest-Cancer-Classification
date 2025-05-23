from src.Chest_Cancer_Classifier.components.model_trainer import Training
from src.Chest_Cancer_Classifier import logger
from src.Chest_Cancer_Classifier.config.configuration import ConfigurationManager

STAGE_NAME= "Training"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        training_Config=config.get_training_config()
        training=Training(config=training_Config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()


if __name__== '__main__':
    try:
          logger.info(f'>>>>> stage {STAGE_NAME} started <<<<<<<')
          obj=ModelTrainingPipeline()
          obj.main()
          logger.info(f'>>>>>> stage {STAGE_NAME} completed<<<<<<< \n\n ====================x=====================')
    except Exception as e:
          logger.exception(e)
          raise e


