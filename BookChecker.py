import os
import shutil

newpath =  "/Users/pratham12/Desktop/Book_Downloads"
if not os.path.exists(newpath):
    os.makedirs(newpath)
os.chdir("/Users/pratham12/Downloads")
for file in os.listdir():
    name, extension = os.path.splitext(file)
    if "z-lib.org" in name:
        shutil.move(file, "/Users/pratham12/Desktop/Book_Downloads")

