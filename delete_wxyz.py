import os 

dir_path = 'bhmsds/symbols/'
delete_symbols = ['w', 'x', 'y', 'z']

for pic in os.listdir(dir_path):
    if pic[0].lower() in delete_symbols:
        os.remove(os.path.join(dir_path, pic))
