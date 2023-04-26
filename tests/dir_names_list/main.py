import os
import shutil

os.chdir(os.path.dirname(__file__))
root = os.getcwd()
list_dir = os.listdir(root)

for i in list_dir:
    current_dir = f"{root}/{i}"
    
    current_dir_rus = f"{current_dir}/rus"
    current_dir_eng = f"{current_dir}/eng"
    
    current_back_rus = f"{root}/_backup/{i}/rus"
    current_back_eng = f"{root}/_backup/{i}/eng"
    
    
    if not os.path.isdir(current_dir):
        continue
    
    if os.path.exists(current_dir_rus):
        print(current_dir, "rus")
        os.makedirs(current_back_rus, exist_ok=True)
        shutil.copytree(current_dir_rus, current_back_rus, dirs_exist_ok=True)
        

    if os.path.exists(current_dir_eng):
        print(current_dir, "eng")
        os.makedirs(current_back_eng, exist_ok=True)
        shutil.copytree(current_dir_eng, current_back_eng, dirs_exist_ok=True)
    
