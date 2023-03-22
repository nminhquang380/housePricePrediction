from source.data import Data
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.compose import make_column_selector, make_column_transformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import numpy as np

train_set, test_set = Data.train_test_set()

# Make a copy of train_set for processing
housing = train_set.drop("median_house_value", axis=1)
housing_labels = train_set["median_house_value"].copy()

class Prepocessing:

    def __init__(self):
        
        # Make a num_pipeline, cat_pipeline for preprocessing numbers and categories data 
        self.num_pipeline = make_pipeline(SimpleImputer(strategy="median"),
                                    StandardScaler())
        self.cat_pipeline = make_pipeline(SimpleImputer(strategy="most_frequent"),
                                    OneHotEncoder(handle_unknown="ignore", sparse_output=False))

        # Final Pipline which can preprocess seperate set of attribute (num, cat)
        # by using make_column_selector function

        self.preprocessing = make_pipeline(
            (self.num_pipeline, make_column_selector(dtype_include=np.number)),
            (self.cat_pipeline, make_column_selector(dtype_include=object))
        )