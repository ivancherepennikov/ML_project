import torch
from torch import optim
import torch.nn as nn

class Model_to_numbers(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_layers = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=5, padding=2),  # input 28x28 → 32x28x28
            nn.ReLU(),
            nn.MaxPool2d(2),                              # → 32x14x14
            nn.Conv2d(32, 64, kernel_size=5, padding=2), # → 64x14x14
            nn.ReLU(),
            nn.MaxPool2d(2)                              # → 64x7x7
        )
        self.fc_layers = nn.Sequential(
            nn.Linear(64 * 7 * 7, 256),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(256, 14)
        )

    def forward(self, x):
        x = self.conv_layers(x)
        x = x.view(x.size(0), -1)
        return self.fc_layers(x)

    

DIVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
model = Model_to_numbers().to(DIVICE)
errow_function = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)