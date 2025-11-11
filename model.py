import torch
from torch import optim
import torch.nn as nn

class Model_to_numbers(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(3 * 28 * 28, 64),
            nn.ReLU(),           
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 14)
        )

    def forward(self, x):
        x = x.view(x.size(0), -1)
        return self.net(x)
    

DIVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
model = Model_to_numbers().to(DIVICE)
errow_function = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)