import time
import os
from os import listdir

# directory = os.listdir("C:\\Users\\YOUR_USER_HERE\\Documents\\VSCode\\Professor-Layton-Text-Encoding-Changer\\original files (Shift-JIS encoding)")
# with open("C:\\Users\\YOUR_USER_HERE\\Documents\\VSCode\\Professor-Layton-Text-Encoding-Changer\\processed\\output.txt", "a") as f:
#     for i in directory:
#         print(i, file=f)
#         subDirectory = os.listdir("C:\\Users\\YOUR_USER_HERE\\Documents\\VSCode\\Professor-Layton-Text-Encoding-Changer\\original files (Shift-JIS encoding)" + "\\" + i)
#         for j in subDirectory:
#             print(j, file=f)

directory = os.listdir("C:\\Users\\YOUR_USER_HERE\\Documents\\VSCode\\Professor-Layton-Text-Encoding-Changer\\original files (Shift-JIS encoding)")
noOfFolders = 0
noOfFiles = 0

for i in directory:
    noOfFolders = noOfFolders + 1
    subDirectory = os.listdir("C:\\Users\\YOUR_USER_HERE\\Documents\\VSCode\\Professor-Layton-Text-Encoding-Changer\\original files (Shift-JIS encoding)" + "\\" + i)
    for j in subDirectory:
        noOfFiles = noOfFiles + 1

newpath = "C:\\Users\\YOUR_USER_HERE\\Documents\\VSCode\\Professor-Layton-Text-Encoding-Changer\\processed"

if os.path.exists(newpath) == True:
    print("Already exists: processed")
    time.sleep(0.5)
else:
    os.makedirs(newpath)

# directory = os.listdir("C:\\Users\\YOUR_USER_HERE\\Documents\\VSCode\\Professor-Layton-Text-Encoding-Changer\\original files (Shift-JIS encoding)")
completedFolders = 0
completedFiles = 1

for i in directory:
    newpath = "C:\\Users\\YOUR_USER_HERE\\Documents\\VSCode\\Professor-Layton-Text-Encoding-Changer\\processed" + "\\" + i
    if os.path.isdir(newpath) == True:
        print(f"Already exists: processed/{i}")
        completedFolders = completedFolders + 1
        time.sleep(0.5)
    else:
        os.makedirs(newpath)
        completedFolders = completedFolders + 1
    
        subDirectory = os.listdir("C:\\Users\\YOUR_USER_HERE\\Documents\\VSCode\\Professor-Layton-Text-Encoding-Changer\\original files (Shift-JIS encoding)" + "\\" + i)
        for j in subDirectory:
            fileCheck = "C:\\Users\\YOUR_USER_HERE\\Documents\\VSCode\\Professor-Layton-Text-Encoding-Changer\\processed\\{i}\\{j}"
            if os.path.isfile(fileCheck) == True:
                print(f"Already exists: processed/{i}/{j}")
                completedFiles = completedFiles + 1
            else:
                file1 = open(f"C:\\Users\\YOUR_USER_HERE\\Documents\\VSCode\\Professor-Layton-Text-Encoding-Changer\\original files (Shift-JIS encoding)\\{i}\\{j}", "r", encoding = "shiftjis")
                file2 = open(f"C:\\Users\\YOUR_USER_HERE\\Documents\\VSCode\\Professor-Layton-Text-Encoding-Changer\\processed\\{i}\\{j}", "w", encoding="utf8")
                l = file1.readline()
                while l:
                    file2.write(l)
                    l = file1.readline()
                file1.close()
                file2.close()
                print(f"Completed: {completedFolders}/{noOfFolders} {completedFiles}/{noOfFiles}")
                completedFiles = completedFiles + 1



# file1 = open("C:\\Users\\YOUR_USER_HERE\\Documents\\VSCode\\Professor-Layton-Text-Encoding-Changer\\original files (Shift-JIS encoding)\\etext\\e1_t0.txt", "r", encoding = "shiftjis")
# file2 = open("C:\\Users\\YOUR_USER_HERE\\Documents\\VSCode\\Professor-Layton-Text-Encoding-Changer\\processed\\e1_t0.txt", "w", encoding="utf8")
# l = file1.readline()
# while l:
#     file2.write(l)
#     l = file1.readline()
# file1.close()
# file2.close()