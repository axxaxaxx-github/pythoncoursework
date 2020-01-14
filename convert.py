import platform, os, subprocess, time
from customModules import *
from convert_files import *

'''
Todo:
Add timestamp to log file

'''

'''
Variables:

f -> log file
path -> path to evtx files
directories -> list of directories found within specified path
listOfFiles -> list of files with the directory the files have been found in
'''

#Create and open log file
f = open("converstion_log.txt", "w+")

#Calls getOS module from customModules script to determine the path to be used.
path = getOS(f)

#Get list of directories and create directories list
directories = os.listdir(path)


#Remove any directories with .txt in the name to remove any files from the list of directories
for i in directories:
    if ".txt" in i:
        directories.remove(i)    

#Output list of directories to the log file
for i in directories:
    f.write("Directory found: {0} \n".format(i))        

#print(os.listdir(path + str(directories[0])))

# Get the list of all files in directory tree at given path
listOfFiles = list()
for (dirpath, dirnames, filenames) in os.walk(path):
    listOfFiles += [os.path.join(dirpath, file) for file in filenames]

#Remove any files without the .evtx extension from the listOfFiles
for i in listOfFiles:
    if ".evtx" not in i:
        listOfFiles.remove(i)

#Remove path from lit of files to only leave directory and file name
for i in listOfFiles:
    listOfFiles.remove(i)
    i = i.replace(path, '')
    listOfFiles.append(i)

#Write list of files to log file
for i in listOfFiles:
    f.write("File Found: {0} \n".format(i))

numberOfFilesCoverted = 0
numberOfFilesCovertedError = 0


convert_files(path, listOfFiles, numberOfFilesCoverted, numberOfFilesCovertedError)

'''
#Use subprocesses module to call the evtx_dump.py file from terminal
for i in listOfFiles:
    print(i)
    try:
        f.write("Converting: {0} to: {1}\n".format(path + i,path + i[:-5]))
        os.system("python3 /home/user/CI5235_Matthew_K1818940/evtx_dump.py '/{0}' > '/{1}'.xml > output.txt".format(str(i), (str(i[:-5]))))
        f.write("Yes {} \n".format(i))
        numberOfFilesCoverted += 1
    except:
        print("ERROR: {0}".format(i))

'''

f.write("Total number of files: {} \n".format(len(listOfFiles)))
f.write("Number of files converted sucsessfully: {} \n".format(numberOfFilesCoverted))
f.write("Number of Errors: {} \n".format(numberOfFilesCovertedError))


f.close()