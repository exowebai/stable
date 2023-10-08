import pandas as pd
import joblib
from modules.paths import *
import json

# load the confg.json file
with open('nasa_app/config.json') as f:
    config = json.load(f)

paths = path()

def classify(model):
    """
    Classify the data in data_path using the model in model_path
    args:
        model_path: the path to the model to use for classification
        data_path: the path to the data to classify
    """
    # load the model
    trained_model = joblib.load(model)#paths.MODEL_PATH)

    # load the data
    preprocessed_data = pd.read_csv(paths.CLN_DATA_PATH)

    # Perform classification using the trained model
    predictions = trained_model.predict(preprocessed_data)
    
    # add the predictions to the preprocessed data as a new column called 'koi_disposition'
    preprocessed_data['koi_disposition'] = predictions
    
    # save the probability of being well classified for each record to a file called 'pseudo_labeled_data.csv'
    preprocessed_data['probability'] = trained_model.predict_proba(
        preprocessed_data.drop(columns=['koi_disposition'])
        ).max(axis=1)
    
    # add the source of the data (client name) as a new column called 'source'
    preprocessed_data['source'] = "TRAPSIT"

    # save the predictions to a file called 'pseudo_labeled_data.csv'
    preprocessed_data.to_csv(paths.PSEUDO_DATA_PATH, index=False)