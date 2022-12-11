import os

os.chdir(os.path.dirname(__file__))

for i in range(1,21):
    os.mkdir(f'batch{i}')

