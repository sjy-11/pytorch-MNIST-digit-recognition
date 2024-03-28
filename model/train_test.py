import torch
import torch.nn as nn
import torch.optim as optim
from torchmetrics import Accuracy
from torchvision import datasets
from torch.utils.data import DataLoader
import torchvision.transforms as transforms
from model import Net


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f'device: {device}')

transform = transforms.Compose([
    transforms.ToTensor()
])

root_path = '../data'

train_data = datasets.MNIST(
    root=root_path,
    train=True,
    transform=transform,
    download=True
)

test_data = datasets.MNIST(
    root=root_path,
    train=False,
    transform=transform,
    download=True
)

dataloader_train = DataLoader(train_data, shuffle=True, batch_size=100)
dataloader_test = DataLoader(test_data, shuffle=True, batch_size=100)

model = Net().to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=1e-3)
num_epochs = 20


for epoch in range(num_epochs):
    running_loss = 0
    for features, labels in dataloader_train:
        features, labels = features.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = model(features)
        loss = criterion(outputs, labels)
        running_loss += loss
        loss.backward()
        optimizer.step()

    print(f'Epoch: {epoch+1}, loss: {running_loss}')


acc_metric = Accuracy(task='multiclass', num_classes=10, average='micro').to(device)

with torch.no_grad():
    model.eval()
    for features, labels in dataloader_test:
        features, labels = features.to(device), labels.to(device)
        outputs = model(features)
        _, preds = torch.max(outputs, 1)
        acc_metric(preds, labels)
        

acc = acc_metric.compute()
print(f'Training accuracy: {acc}')