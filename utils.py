from dataset import *
from model import *
from train import *
from evaluate import *

def save_model(model, path="model.pth"):
    torch.save(model.state_dict(), path)

def load_model(model, path="model.pth"):
    model.load_state_dict(torch.load(path))