import os
path = 'E:/Box_detection/preparing_data/OpenLabeling-master/OpenLabeling-master/main/input'
files = os.listdir(path)


for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index+151), '.jpg'])))