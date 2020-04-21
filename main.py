import os
from shutil import copy

root = input("Path to phone:- ")
dst = input("Folder to save files to")


print(os.chdir(root))

for path, subdirs, files in os.walk(root):
    for name in files:
        temp = os.path.join(path, name)
        print(temp)
        if(temp[-4:] == '.png'):
            print("\n*****************************************")
            print(temp)
            try:
                copy(temp, dst)
            except :
                pass

            print("***************************************** ")
    
        if(temp[-4:] == '.jpg'):
            print("\n*****************************************")
            print(temp)
            try:
                copy(temp, dst)
            except:
                pass

            print("***************************************** ")

        if(temp[-5:] == '.jpeg'):
            print("\n*****************************************")
            print(temp)
            try:
                copy(temp, dst)
            except:
                pass
            print("***************************************** ")
        


'''
        
        
        '''
