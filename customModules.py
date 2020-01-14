import os, platform

def getOS(f):
    operatingSystem = (platform.system())
    if operatingSystem == "Linux":
        f.write("The OS is {0}".format(operatingSystem) + "\n")
        path = '/home/user/CI5235_Matthew_K1818940/pythoncoursework/evtx_logs/'
        f.write('Path set to {0}'.format(path) + "\n")
        return path
    else:
        f.write("The OS is {0}".format(operatingSystem))
        path = "%systemroot%/sysnative/winevt/Logs"
        f.write('Path is set to {0}'.format(path))
        return path

def exsistCheck(exsistingXml, filesToCheckNoExt):
    print("Chekcing for exsisting XML Files")
    for i in filesToCheckNoExt:
        if (str(i) + ".xml") in exsistingXml:
            print("File Exists: {0}".format(i))
        else:
            print("No File Exists")