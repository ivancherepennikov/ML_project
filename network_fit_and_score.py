import os
import torch
import cv2
import numpy as np
from model import Model_to_numbers

def final():
    model = Model_to_numbers()
    model.load_state_dict(torch.load("model.pth", map_location="cpu"))
    model.eval()

    input_dir = 'symbols_28x28'

    math_array = []

    def extract_number(name):
        return int(name.split("_")[1].split(".")[0])

    files = sorted(
        [f for f in os.listdir(input_dir) if f.endswith(".png")],
        key=extract_number
    )

    for filename in files:

        path = os.path.join(input_dir, filename)

        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        img = img.astype(np.float32) / 255.0
        img = 1.0 - img
        img = img.reshape(1, 28, 28)

        tensor = torch.tensor(img).unsqueeze(0).contiguous()

        with torch.no_grad():
            logits = model(tensor)
            prediction = logits.argmax(1).item()

        math_array.append(prediction)

    # scoring
    score = ''
    for symbol in math_array:
        if symbol == 10:
            score += '*'
        elif symbol == 11:
            score += '-'
        elif symbol == 12:
            score += '+'
        elif symbol == 13:
            score += '/'
        else:
            score += str(symbol)

    return(eval(score))