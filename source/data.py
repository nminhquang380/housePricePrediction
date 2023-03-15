"""
This file for doing tasks related to data:
- Get data
"""
# Download data
from pathlib import Path
import pandas as pd
import tarfile
import urllib.request

def load_housing_data():
    data_path = Path('data/housing.tgz')
    if not data_path.is_file():
        Path('data').mkdir(parents=True, exist_ok=True)
        