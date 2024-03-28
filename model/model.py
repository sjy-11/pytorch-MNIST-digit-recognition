import torch.nn as nn
import torch.nn.init as init

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 16, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1)
        self.fc1 = nn.Linear(32*7*7, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 10)

        init.kaiming_uniform_(self.conv1.weight, nonlinearity='relu')
        init.kaiming_uniform_(self.conv2.weight, nonlinearity='relu')
        init.kaiming_uniform_(self.fc1.weight, nonlinearity='relu')
        init.kaiming_uniform_(self.fc2.weight, nonlinearity='relu')

        self.layers = nn.Sequential(
            self.conv1,
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            self.conv2,
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Flatten(),
            nn.Dropout(p=0.2),
            self.fc1,
            nn.BatchNorm1d(128),
            nn.ReLU(),
            self.fc2,
            nn.BatchNorm1d(64),
            nn.ReLU(),
            self.fc3
        )
    
    def forward(self, x):
        x = self.layers(x)
        return x
    