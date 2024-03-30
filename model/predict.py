from model import Net
from train_test import test_data, device
import torch
import matplotlib.pyplot as plt

model = Net().to(device)
model.load_state_dict(torch.load('./model/model_state_dict.pth'))
model.eval()

data, label = test_data[100]

data = data.unsqueeze(0).to(device)
output = model(data)
_, prediction = torch.max(output, 1)
print(f"prediction: {prediction.item()}")

img = data.squeeze(0).squeeze(0).cpu().numpy()
plt.imshow(img,cmap='gray')
plt.show()