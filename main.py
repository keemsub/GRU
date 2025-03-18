from dataset import *
from model import *
from train import *
from evaluate import *
from utils import *

if __name__ == "__main__":
    train_loader, test_loader = load_data()
    model = GRUModel(input_size=10, hidden_size=HIDDEN_SIZE, num_layers=NUM_LAYERS, output_size=1)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)
    
    train(model, train_loader, criterion, optimizer)
    evaluate(model, test_loader, criterion)
    save_model(model)