import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Initialize the Kaggle API
api = KaggleApi()
api.authenticate()

# Define the dataset URL or identifier
dataset = 'ealtman2019/ibm-transactions-for-anti-money-laundering-aml'

# Define the path where the dataset will be downloaded
download_path = 'ibm-transactions-for-anti-money-laundering-aml'

# Create the download directory if it does not exist
if not os.path.exists(download_path):
    os.makedirs(download_path)

# Download the dataset
api.dataset_download_files(dataset, path=download_path, unzip=True)

print(f"Dataset downloaded and extracted to {download_path}")
