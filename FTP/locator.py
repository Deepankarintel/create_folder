import os
import shutil

def create_folders(file_path,base_folder_name):
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    else:
        shutil.rmtree(file_path)
        os.makedirs(file_path)
    os.makedirs(os.path.abspath(os.path.join(file_path, base_folder_name)))

if __name__ =='__main__':
    file_path = 'Testing'
    base_folder_name = 'GenericFramwork/Package_name/scripts'
    create_folders(file_path,base_folder_name)
    print ("Folders and Subfolder has created")
