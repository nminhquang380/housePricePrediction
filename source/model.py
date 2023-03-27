from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from source.preprocess import Prepocessing
import joblib
from pathlib import Path

class Model:
    def __init__(self):
        self._model = RandomForestRegressor(max_features=8 ,random_state=42)
        self._pipline = make_pipeline(Prepocessing.preprocessing,
                                      self._model)
        
    def load_model(self):
        model_path = Path("my_model.pkl")
        if model_path.is_file():
            self._model = joblib.load()
    
    def train_model(self, housing, housing_labels):
        self.train_model.fit(housing, housing_labels)
    
    def predict(self, data):
        return self._model.predict(data)
    
    def train_pipeline(self, x= None, y=None):
        if x and y:
            self._pipline.fit(x, y)

    def preprocess_predict(self, data):
        return self._pipline.predict(data)