import os
import shutil 
from datetime import datetime

def organize_files_by_type_and_date(folder_path): 
    if not os.path.isdir(folder_path): 
       print("Invalid folder path.") 
       return 

    for filename in os.listdir(folder_path): 
        full_path = os.path.join(folder_path, filename) 
        if os.path.isfile(full_path): 
           
           file_ext=filename.split('.')[-1].lower()

           mod_time=os.path.getmtime(full_path)
           date_folder=datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d')

           target_dir=os.path.join(folder_path, date_folder)
           os.makedirs(target_dir, exist_ok=True) 
           shutil.move(full_path, os.path.join(target_dir, filename)) 

    print("Files organized by type successfully.") 


folder = input("Enter the full path to the folder you want to organize:")
organize_files_by_type_and_date(folder)
