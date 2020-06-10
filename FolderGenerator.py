import os
from FoldersSetup import *

customFolders = ['Assets',
                 'Scripts', 'Scripts/Blender', 'Scripts/Nuke', 'Scripts/AE',
                 'Renders', 'Renders/Blender', 'Renders/Nuke', 'Renders/AE',
                 '3D Tracking',
                 'Footages']


def createFolder(directory):
    try:
        if not os.path.exists(dirPath):
            print('Esse caminho nao existe!')
        if os.path.exists(dirPath) and not os.path.exists(finalPath):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory.' + directory)


lines = f"{40 * '-'}"
msgError = lines + "\nERROR! Please type a correct value!\n" + lines

# INSERT DIRECTORY
dirPath = ""
while True:
    try:
        dirPath = input('Directory: ').strip()
        if dirPath != "":
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
        askPath = int(input('[1] This directory is my main folder, \n'
                            '[2] I need to create a new main folder;\n'))
        if askPath == 1:
            for c in customFolders:
                finalPath = dirPath + f'/{c}'
                createFolder(finalPath)
                print(f'Final Path: {finalPath}')
            break
        elif askPath == 2:
            folderName = input('Main folder name: ')
            for c in customFolders:
                finalPath = dirPath + '/' + folderName + f'/{c}'
                createFolder(finalPath)
                print(f'Final Path: {finalPath}')
            break
    except:
        print(msgError)
        continue

print()
print('Developed by: Danilo de Lúcio')
print('Site: www.danilodelucio.com')
print('GitHub: www.github.com/danilodelucio')
print()
