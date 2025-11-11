from torch.utils.data import DataLoader, random_split
from torchvision.datasets import ImageFolder
from torchvision import transforms
from torch.utils.data import DataLoader

from model import model, errow_function, optimizer, DIVICE

BATCH_SIZE = 32
EPOCHS = 10

dataset = ImageFolder('dataset/', transform=transforms.ToTensor())
train_size = int (0.8 * len(dataset))
test_size = len(dataset) - train_size

train_data, test_data = random_split(dataset, [train_size, test_size])

train_loader = DataLoader(train_data, batch_size=BATCH_SIZE, shuffle=True)
test_loader = DataLoader(test_data, batch_size=BATCH_SIZE, shuffle=False)

'''for images, labels in train_loader:
    print(images.shape)
    break'''

def train(epoch):
    model.train()
    total_loss = 0
    correct = 0
    total = 0

    for images, labels in train_loader:
        images, labels = images.to(DIVICE), labels.to(DIVICE)
        
        preds = model(images)
        loss = errow_function(preds, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item() * images.size(0)
        correct += (preds.argmax(1) == labels).sum().item()
        total += labels.size(0)
    
    avg_loss = total_loss / total
    acc = correct / total

    print(f'Epoch: №{epoch}\nTrain_loss: {avg_loss:.2f}, AcCuracity:{acc:.2f}')

def test():
    model.eval()
    total_loss, correct, total = 0, 0 ,0 

    for images, labels in test_loader:
        images, labels = images.to(DIVICE), labels.to(DIVICE)

        preds = model(images)
        loss = errow_function(preds, labels)

        total_loss += loss.item() * images.size(0)
        correct += (preds.argmax(1) == labels).sum().item()
        total += labels.size(0)

    avg_loss = total_loss / total
    acc = correct / total

    print(f'Test_loss: {avg_loss:.2f}, AcCuracity:{acc:.2f}')

for epoch in range(1, EPOCHS+1):
    train(epoch)
    test()
