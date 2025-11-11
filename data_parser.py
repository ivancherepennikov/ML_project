import os 
import shutil

def create_category(str):
    for i in range(0, len(str)):
        if str[i] == '-':
            return str[0:i]

dir_path = 'bhmsds/symbols/'

path = os.path.dirname(os.path.abspath(__file__))
dataset = os.path.join(path, "dataset")
os.makedirs(dataset, exist_ok=True)

target_classes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'plus', 'minus', 'dot', 'slash']

for target in target_classes:
    os.makedirs(os.path.join(dataset, target), exist_ok=True)

for pic in os.listdir(dir_path):
    if create_category(pic) in target_classes:
        src_path = os.path.join(dir_path, pic)
        dst_path = os.path.join(dataset, create_category(pic), pic)
        shutil.move(src_path, dst_path)