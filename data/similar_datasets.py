import os
from kaggle.api.kaggle_api_extended import KaggleApi

def download_dataset(dataset_identifier, download_path):
    # Initialize the Kaggle API
    api = KaggleApi()
    api.authenticate()

    # Create the download directory if it does not exist
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # Download the dataset
    api.dataset_download_files(dataset_identifier, path=download_path, unzip=True)
    print(f"Dataset '{dataset_identifier}' downloaded and extracted to {download_path}")

# List of datasets to download
datasets = [
    ('berkanoztas/synthetic-transaction-monitoring-dataset-aml', 'synthetic-transaction-monitoring-dataset-aml'),
    ('llabhishekll/fraud-transaction-detection', 'fraud-transaction-detection'),
    ('arjunjoshua/predicting-fraud-in-financial-payment-services', 'predicting-fraud-in-financial-payment-services'),
    ('ealaxi/paysim1', 'paysim1'),
    ('stefanouccelli/tesis-1', 'tesis-1')
]

# Download each dataset
for dataset_identifier, download_path in datasets:
    download_dataset(dataset_identifier, download_path)
