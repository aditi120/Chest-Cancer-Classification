import os
import zipfile
import gdown
from Chest_Cancer_Classifier import logger
from Chest_Cancer_Classifier.utils.common import get_size
from src.Chest_Cancer_Classifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config=config

    def download_file(self)->str:
        #Will fetch data from url

        try:
            dataset_url=self.config.source_URL
            zip_download_dir=self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"downloading data from {dataset_url} into file {zip_download_dir}")
            
            file_id= dataset_url.split("/")[-2]
            prefix="https://drive.google.com/uc?id="
            suffix="&export=download"
            gdown.download(prefix+file_id+suffix, zip_download_dir)
            

            logger.info(f'downloaded data from {dataset_url} into file {zip_download_dir}')

        except Exception as e:
            raise e
    def extract_zip_file(self):
        unzip_path= self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)   

      