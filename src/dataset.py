import os
import pathlib

import torch
from torch.utils.data import Dataset, DataLoader


class MyDataset(Dataset):
    def __init__(self, datapath, **kwargs):
        self.datapath = pathlib.Path(datapath)
        self.cache= {}
    """Data preprocessing parameters..."""
    
    def Dataset_func1(self, x):
        return
    
    def Dataset_func1(self, x):
        return 
    
    def collate_fn(self, x):
        return
    
    def __len__(self):
        return # len(self.filenames)
    
    def __getitem__(self, idx): 
        
        # filename = self.filenames[idx]
        # data = self.datapath / load_data(filename)
        # if cache is not None:
        #     self.cache[filename] = {"data": data, "label": label}          
        # return data, label
        return