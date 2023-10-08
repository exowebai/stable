class path:
    def __init__(self) -> None:
        self.KEPLER_DATA_PATH = './data/kepler_data.csv'
        self.PUBLIC_DATA_PATH = './data/public_network_data.csv'
        self.CLN_DATA_PATH = './data/cln_unlabeled_data.csv'
        self.PSEUDO_DATA_PATH = './data/pseudo_labeled_data.csv'
        self.MODEL_PATH = './model/model_kepler.pkl'
        self.MODEL_PATH2 = './model/model.pkl'
        self.TARGET_COLUMN = 'koi_disposition'