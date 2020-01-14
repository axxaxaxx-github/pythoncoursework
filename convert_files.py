import os

def convert_files(path, listOfFiles, numberOfFilesCoverted, numberOfFilesConvertedError):
    for i in listOfFiles:
        filePath = os.path.realpath(i)
        try:
            print("Trying to convert: {0}".format(filePath))
            os.system("python3 /home/user/CI5235_Matthew_K1818940/pythoncoursework/evt_logs/{0} > /home/user/CI5235_Matthew_K1818940/pythoncoursework/evt_logs/{1}.xml > output.txt".format(filePath, filePath[:-5]))
            numberOfFilesConverted += 1
        except:
            print("Could not convert: {0}".format(i))
            numberOfFilesConvertedError += 1
            break

    return(numberOfFilesConvertedError, numberOfFilesConvertedError)
