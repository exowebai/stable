import pandas as pd
import joblib
from modules.paths import *
import json

# load the confg.json file
with open('nasa_app/config.json') as f:
    config = json.load(f)


paths = path()

def retrain(probability_threshold=0.75):
    """
    Retrain the existing logistic regression model on the updated data
    args:
        probability_threshold: the probability threshold to use for filtering the public data
    """
    # Load  original training data
    kepler_data = pd.read_csv(paths.KEPLER_DATA_PATH)
    # Load the public network data
    public_data = pd.read_csv(paths.PUBLIC_DATA_PATH)
    # load the model
    loaded_model = joblib.load(paths.MODEL_PATH)
    
    # Filter the public data based on a probability threshold
    filtered_public_data = public_data[public_data['probability'] > probability_threshold]

    # Drop the probability column before combining
    filtered_public_data = filtered_public_data.drop(columns=['probability', 'source'])

    # Combine the filtered public data with your original data
    combined_data = pd.concat([kepler_data, filtered_public_data], ignore_index=True)

    # Split the combined dataset into features (X) and target (y)
    X = combined_data.drop(columns=[paths.TARGET_COLUMN])
    y = combined_data[paths.TARGET_COLUMN]

    loaded_model.fit(X, y)

    # Save the updated model to the 'modules' folder
    joblib.dump(loaded_model, paths.MODEL_PATH)