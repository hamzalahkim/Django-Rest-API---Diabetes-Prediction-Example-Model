from django.apps import AppConfig
import pickle
from pathlib import Path

class PimaConfig(AppConfig):
    name = 'pima'

    pima_model = Path("pima/model/pima_dataset.pkl")
    predictor_model = pickle.load(open(pima_model, 'rb'))