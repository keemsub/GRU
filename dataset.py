import torch
from config import *
from torch.utils.data import DataLoader, Dataset

class CustomDataset(Dataset):
    def __init__(self, data):
        self.data = data
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        return self.data[idx]

def load_data():
    train_data, test_data = ...  # 데이터 로딩 로직
    return DataLoader(CustomDataset(train_data), batch_size=BATCH_SIZE), DataLoader(CustomDataset(test_data), batch_size=BATCH_SIZE)