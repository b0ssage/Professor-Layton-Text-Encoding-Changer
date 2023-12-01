import tkinter
from tkinter import filedialog
import time
import os
from os import listdir
from pathlib import Path

# directory = os.listdir(inputPath)
# with open("C:\\Users\\andre\\Documents\\VSCode\\Professor-Layton-Text-Encoding-Changer\\processed\\output.txt", "a") as f:
#     for i in directory:
#         print(i, file=f)
#         subDirectory = os.listdir(inputPath + "\\" + i)
#         for j in subDirectory:
#             print(j, file=f)

tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing
inputPath = filedialog.askdirectory()
# relative = Path(userSelection)
# inputPath = relative.absolute()

# print("#############################################################################")
# print("\n")
# print("Selected:")
# print(inputPath)
# print("\n")
# print("#############################################################################")
# time.sleep(2)

# inputPath = "C:\\Users\\andre\\Documents\\VSCode\\Professor-Layton-Text-Encoding-Changer\\lt2\\lt2 - JP - Diabolical Box\\data_jp"
outputPath = "C:\\Users\\andre\\Documents\\VSCode\\Professor-Layton-Text-Encoding-Changer\\processed"

# directory = os.listdir(inputPath)
directory = [d for d in os.listdir(inputPath) if os.path.isdir(os.path.join(inputPath, d))]
print(directory)

noOfFolders = 0
noOfFiles = 0

for i in directory:
    noOfFolders = noOfFolders + 1
    subDirectory = os.listdir(inputPath + "\\" + i)
    for j in subDirectory:
        noOfFiles = noOfFiles + 1


if os.path.exists(outputPath) == True:
    print("Already exists: /processed")
    time.sleep(0.5)
else:
    os.makedirs(outputPath)

# directory = os.listdir(inputPath)
completedFolders = 0
completedFiles = 1

for i in directory:
    outputPath = "C:\\Users\\andre\\Documents\\VSCode\\Professor-Layton-Text-Encoding-Changer\\processed" + "\\" + i
    if os.path.isdir(outputPath) == True:
        print(f"Already exists: /processed/{i}")
        completedFolders = completedFolders + 1
        time.sleep(0.5)
    else:
        os.makedirs(outputPath)
        completedFolders = completedFolders + 1
    
        subDirectory = os.listdir(inputPath + "\\" + i)
        for j in subDirectory:
            fileCheck = "C:\\Users\\andre\\Documents\\VSCode\\Professor-Layton-Text-Encoding-Changer\\processed\\{i}\\{j}"
            if os.path.isfile(fileCheck) == True:
                print(f"Already exists: processed/{i}/{j}")
                completedFiles = completedFiles + 1
            else:
                file1 = open(f"{inputPath}\\{i}\\{j}", "r", encoding = "shiftjis")
                file2 = open(f"C:\\Users\\andre\\Documents\\VSCode\\Professor-Layton-Text-Encoding-Changer\\processed\\{i}\\{j}", "w", encoding="utf8")
                l = file1.readline()
                while l:
                    file2.write(l)
                    l = file1.readline()
                file1.close()
                file2.close()
                print(f"Completed: {completedFolders}/{noOfFolders} {completedFiles}/{noOfFiles}")
                completedFiles = completedFiles + 1



# file1 = open("C:\\Users\\andre\\Documents\\VSCode\\Professor-Layton-Text-Encoding-Changer\\original files (Shift-JIS encoding)\\etext\\e1_t0.txt", "r", encoding = "shiftjis")
# file2 = open("C:\\Users\\andre\\Documents\\VSCode\\Professor-Layton-Text-Encoding-Changer\\processed\\e1_t0.txt", "w", encoding="utf8")
# l = file1.readline()
# while l:
#     file2.write(l)
#     l = file1.readline()
# file1.close()
# file2.close()