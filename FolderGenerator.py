import os
from FoldersSetup import *


def createFolder(directory):
    try:
        if os.path.exists(dirPath) and not os.path.exists(finalPath):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory.' + directory)


lines = f"{40 * '-'}"
msgError = lines + "\nERROR! Please type a correct value!\n" + lines

# ADDING DIRECTORY
dirPath = ""
while True:
    try:
        dirPath = input('Directory: ').strip()
        if dirPath != "":
            if not os.path.exists(dirPath):
                print("\nThis directory doesn't exist!\n")
                continue
            break
        elif dirPath == "":
            continue
    except:
        print(msgError)
        continue

# EXISTING FOLDER OR CREATING A NEW ONE
finalPath = ""
while True:
    try:
        askPath = int(input('\n[1] This directory is my main folder, \n'
                            '[2] I need to create a new main folder;\n'))
        if askPath == 1:
            file = open('customFolders.txt', 'r')
            for line in file:
                line = line.rstrip()
                print(line)
                finalPath = dirPath + f'/{line}'
                createFolder(finalPath)
                print(f'Final Path: {finalPath}')
            file.close()
            break
        elif askPath == 2:
            folderName = input('Main folder name: ')
            file = open('customFolders.txt', 'r')
            for line in file:
                line = line.rstrip()
                print(line)
                finalPath = dirPath + '/' + folderName + f'/{line}'
                createFolder(finalPath)
                print(f'Final Path: {finalPath}')
            file.close()
            break
    except:
        print(msgError)
        continue

# CREDITS
print()
print('Developed by: Danilo de Lúcio | June/2020')
print('Site: www.danilodelucio.com')
print('GitHub: www.github.com/danilodelucio')
print()
