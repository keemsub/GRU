import torch.optim as optim

def train(model, train_loader, criterion, optimizer):
    model.train()
    for epoch in range(EPOCHS):
        for batch in train_loader:
            optimizer.zero_grad()
            output = model(batch)
            loss = criterion(output, batch)  # 예시 코드, 타겟 필요
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch+1}/{EPOCHS}, Loss: {loss.item()}")