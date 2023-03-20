"""
This file for doing tasks related to data:
- Get data
- Split train test set
"""
from pathlib import Path
import pandas as pd
import tarfile
import urllib.request
from sklearn.model_selection import train_test_split

# Step to get data:
# Create a path -> Check existance 
# -> If not exist -> Make path, download tarfile -> Extract File 
def load_housing_data():
    data_path = Path('data/housing.tgz')
    if not data_path.is_file():
        Path('data').mkdir(parents=True, exist_ok=True)
        url = "https://github.com/ageron/data/raw/main/housing.tgz"
        urllib.request.urlretrieve(url, data_path)
        with tarfile.open(data_path) as housing_data:
            housing_data.extractall(path="data")
    return pd.read_csv(Path("data/housing/housing.csv"))

housing = load_housing_data()

# Split Test set
def train_test_set(data, test_ratio):
    return train_test_split(data, test_size=test_ratio, random_state=42)