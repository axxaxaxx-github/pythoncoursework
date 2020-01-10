import platform
import os
from customModules import *
import subprocess

files = []
directories = []
directoriesList = []
discoveredFiles = []
filesToCheck = []
exsistingXml = []
filesToCheckNoExt = []
count = 0

#Calls getOS module from customModules script to determine the path to be used.
path = getOS()

#Get a list of the files in the specified directory. Print statement included to make sure it is working for debugging purposes. Will removed when finished and functional.
directories = os.listdir(path)

for i in directories:
    files.append(os.listdir(path + "/" + i))

#Print list of files with their directories. Creates a list of files without their extension
for i in range(len(directories)):
    #print(directories[i])
    for j in range(len(files[i])):
        #print(files[i][j])
        filesToCheck.append(directories[i] + "/" + files[i][j][:-5])
        filesToCheckNoExt.append(files[i][j][:-5])
'''
for i in filesToCheck:
    print(i)
'''

#WORKS - Need to change to add this information to the log
'''
for i in filesToCheck:
    if i not in discoveredFiles:
        print("New file found: {0}".format(i))
    else:
        print("File already found {0}".format(i))
'''
#Check for files with .xml extension. If it exsists, add it to the list of detected XMl files
for root, dirs, files in os.walk(path):
    for file in files:
        if (file.endswith(".xml")):
            #print(os.path.join(root,file))
            exsistingXml.append(file)
        else:
            continue
            #print("No xml found")

#Print if an XML Files exsists
#print("XML Found: {0}".format(exsistingXml))

for i in filesToCheckNoExt:
    print(i)

for i in exsistingXml:
    print(i)

for i in filesToCheckNoExt:
    if (str(i) + ".xml") in exsistingXml:
        print("File Exists: {0}".format(i))
    else:
        print("No File Exists")

subprocess.run(["python3", "evtx_dump.py" "privexchange_dirkjan.evtx > test1.xml"])