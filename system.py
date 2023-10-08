import os
import time
from modules import classify, preprocess, retrain
from modules.paths import *
import warnings
warnings.filterwarnings("ignore")

paths = path()

INPUT_PATH = './input/raw_telescope_data.csv'

print("System started!")
while True:
    # preprocess the input data if available
    if os.path.exists(INPUT_PATH):
        preprocess.preprocess(INPUT_PATH)
        print("Preprocessing done!")
        os.remove(INPUT_PATH)
    
    # classify the preprocessed data if available
    if os.path.exists(paths.CLN_DATA_PATH):
        classify.classify(paths.MODEL_PATH2)
        print("Classification done!")
        os.remove(paths.CLN_DATA_PATH)

    # retrain the model if new data is available in public_data.csv
    if os.path.exists(paths.PUBLIC_DATA_PATH):
        retrain.retrain()
        print("Retraining done!")
    time.sleep(60) # sleep for 60 seconds before checking again