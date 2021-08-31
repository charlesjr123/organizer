import os 
import shutil


source=input("please enter your source name ")
destination=input("please enter your destination folder")


source=source+'/'
destination=destination+'/'

list_of_files=os.listdir(source)

for file in  list_of_files:
    shutil.copy((source+file), destination)
