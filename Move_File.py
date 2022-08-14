import os
import shutil

from_dir="C:/Users/LENOVO/OneDrive/Desktop"
to_dir="C:/Users/LENOVO\OneDrive/DownloadedImages"

list_of_files=os.listdir(from_dir)
print(list_of_files)

for file in list_of_files:
    name,extension=os.path.splitext(file)
