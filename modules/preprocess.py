import pandas as pd
from sklearn.preprocessing import LabelEncoder
from modules.paths import *

paths = path()

# List of expected columns
expected_columns = ['koi_score', 'koi_fpflag_nt', 'koi_fpflag_ss',
                    'koi_fpflag_co','koi_impact', 'koi_model_snr', 
                    'koi_steff', 'koi_slogg', 'ra','dec']

def preprocess(data_path): #input
    """
    to pre-process the "raw_unlabeled_data" and save the 
    preprocessed data to a file called 'cln_unlabeled_data.csv'
    args:
        data_path: path to the raw_unlabeled_data
    """
    # Load the CSV dataset into a DataFrame
    try:
        data = pd.read_csv(data_path)
    except FileNotFoundError:
        raise FileNotFoundError("File not found")
    except pd.errors.EmptyDataError:
        raise pd.errors.EmptyDataError("Empty file")
    
    # Verify if the dataset has the expected columns
    missing_columns = set(expected_columns) - set(data.columns)
    extra_columns = set(data.columns) - set(expected_columns)

    if missing_columns:
        raise Exception(f"Dataset is missing columns: {', '.join(missing_columns)}")

    if extra_columns:
        # Drop extra columns if present
        data = data.drop(columns=list(extra_columns))

    #Missing values
     # Handle missing values in categorical features (fill with mode)
    categorical_features = data.select_dtypes(include=['object']).columns
    for col in categorical_features:
        data[col].fillna(data[col].mode()[0], inplace=True)

        # Label encode categorical features
        label_encoder = LabelEncoder()
        data[col] = label_encoder.fit_transform(data[col])

    # Handle missing values in numeric features (fill with mean)
    numeric_features = data.select_dtypes(include=['number']).columns
    for col in numeric_features:
        data[col].fillna(data[col].mean(), inplace=True)

    # Remove duplicates
    data.drop_duplicates(inplace=True)

    # save the preprocessed data to a file called 'cln_unlabeled_data.csv'
    data.to_csv(paths.CLN_DATA_PATH, index=False)


#############################################
# this part is for the accuracy evalution during the production phase
# List of expected columns
expected_columns2 = ['koi_score', 'koi_fpflag_nt', 'koi_fpflag_ss',
                    'koi_fpflag_co','koi_impact', 'koi_model_snr', 
                    'koi_steff', 'koi_slogg', 'ra','dec', "koi_disposition"]

def preprocess2(data_path): #input
    """
    to pre-process the "raw_unlabeled_data" and save the 
    preprocessed data to a file called 'cln_unlabeled_data.csv'
    args:
        data_path: path to the raw_unlabeled_data
    """
    # Load the CSV dataset into a DataFrame
    try:
        data = pd.read_csv(data_path)
    except FileNotFoundError:
        raise FileNotFoundError("File not found")
    except pd.errors.EmptyDataError:
        raise pd.errors.EmptyDataError("Empty file")
    
    # Verify if the dataset has the expected columns
    missing_columns = set(expected_columns2) - set(data.columns)
    extra_columns = set(data.columns) - set(expected_columns2)

    if missing_columns:
        raise Exception(f"Dataset is missing columns: {', '.join(missing_columns)}")

    if extra_columns:
        # Drop extra columns if present
        data = data.drop(columns=list(extra_columns))

    #Missing values
     # Handle missing values in categorical features (fill with mode)
    categorical_features = data.select_dtypes(include=['object']).columns
    for col in categorical_features:
        data[col].fillna(data[col].mode()[0], inplace=True)

        # Label encode categorical features
        label_encoder = LabelEncoder()
        data[col] = label_encoder.fit_transform(data[col])

    # Handle missing values in numeric features (fill with mean)
    numeric_features = data.select_dtypes(include=['number']).columns
    for col in numeric_features:
        data[col].fillna(data[col].mean(), inplace=True)

    # Remove duplicates
    data.drop_duplicates(inplace=True)

    # save the preprocessed data to a file called 'cln_unlabeled_data.csv'
    data.to_csv("./data/preprocessed_data1.csv", index=False)