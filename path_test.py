import os,re

path='../deep_project'
def find_dir(path):
    return [f"{path}/{i}" for i in os.listdir(path)
              if os.path.isdir(f"{path}/{i}")]

def final_path_update(path,list):
    sub_paths=find_dir(path)
    print(sub_paths)
    for sub_path in sub_paths:
        if len(find_dir(sub_path))==0:
            list.append(sub_path)
        else:
            find_final_path(sub_path)
    

def find_final_path(path):
    ls=list()
    final_path_update(path,ls)
    return ls

ls=list()
print(find_final_path(path))