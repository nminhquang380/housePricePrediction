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

class Data:
# Step to get data:
# Create a path -> Check existance 
# -> If not exist -> Make path, download tarfile -> Extract File
    def __init__(self) -> None:
        self.housing = None
        
    def load_housing_data(self):
        data_path = Path('data/housing.tgz')
        if not data_path.is_file():
            Path('data').mkdir(parents=True, exist_ok=True)
            url = "https://github.com/ageron/data/raw/main/housing.tgz"
            urllib.request.urlretrieve(url, data_path)
            with tarfile.open(data_path) as housing_data:
                housing_data.extractall(path="data")
        return pd.read_csv(Path("data/housing/housing.csv"))

    
    # Split Test set
    def train_test_set(self):
        self.housing = pd.read_csv(Path("data/housing/housing.csv"))
        return train_test_split(self.housing, test_size=0.2, random_state=42)