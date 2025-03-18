def evaluate(model, test_loader, criterion):
    model.eval()
    total_loss = 0
    with torch.no_grad():
        for batch in test_loader:
            output = model(batch)
            loss = criterion(output, batch)  # 예시 코드
            total_loss += loss.item()
    print(f"Test Loss: {total_loss / len(test_loader)}")
