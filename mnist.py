import numpy as np
import os

DATA_DIR = "/data/ziz/not-backed-up/datasets-ziz-only"

def load_data(which_set="train", mode="all"):
    assert which_set in ['train', 'valid', 'test'], \
            "which_set takes values in [train, valid, test]"
    assert mode in ['all', 'batch'], \
            "mode takes values in [all, batch]"
    if mode == 'all':
        path = os.path.join(DATA_DIR, "raw_data/mnist", "mnist.npz")
        return _load_data_all(path, which_set)
    elif mode == 'batch':
        return _load_data_batch()

def _load_data_all(path, which_set):
    data = np.load(path)
    return data["x_"+which_set], data['y_'+which_set]

def _load_data_batch():
    pass
