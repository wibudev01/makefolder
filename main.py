# This is a sample Python script.
import os

count = 0
sumarize = 0
sumarate = 0.0

def makeFolder(file_path, numb_folder_in_folder, class_of_folder):
    global count, sumarize, sumarate
    if class_of_folder > 0:
        directory = ""
        for j in range(0, numb_folder_in_folder + 1):
            directory = str(j)
            path = os.path.join(file_path, directory)
            os.mkdir(path)
            makeFolder(path, numb_folder_in_folder, class_of_folder - 1)
            count+=1
            if count > sumarate+sumarize/1000:
                print(str(round((count/sumarize)*100,2))+"%")
                sumarate += sumarize/1000


if __name__ == '__main__':
    #locate your folder
    # parent_dir = "D:\go" 
    parent_dir = input("your directory: ") 
    #number of folders create in a folder (these folder will be named by number from 0)
    folder = int(input("number of folder: "))
    #number of folders include folders
    class_folder = int(input("number of folder include upper folders: "))
    #name folder include upper folders
    directory_pr = input("name of folder: ")

    #processing ratio
    class_folder_s = class_folder
    while(class_folder_s > 0):
        sumarize += (folder+1)**class_folder_s
        class_folder_s -= 1
    print(sumarize)

    path = os.path.join(parent_dir, directory_pr)
    print(path)
    os.mkdir(path)

    print(str(round((count/sumarize)*100,2))+"%")
    makeFolder(path, folder, class_folder)
    print("success")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
