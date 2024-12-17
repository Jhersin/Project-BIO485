import h5py
import numpy as np

def getinfo():
    fname_train = './data/file1000001.h5'

    with h5py.File(fname_train, 'r') as f:
        ls = list(f.keys())

        kspace_TRAIN = f.get('kspace')
        kspace_TRAIN = np.array(kspace_TRAIN)

        high_resolution_TRAIN = f.get('reconstruction_rss')
        high_resolution_TRAIN = np.array(high_resolution_TRAIN)
        f.close()
    return kspace_TRAIN, high_resolution_TRAIN
