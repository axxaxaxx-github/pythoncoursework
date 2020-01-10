import os, platform

def getOS():
    operatingSystem = (platform.system())
    if operatingSystem == "Linux":
        print("The OS is {0}".format(operatingSystem))
        path = '/home/user/CI5235_K1818940_Matthew/evt_logs'
        print('Path set to {0}'.format(path))
        return path
    else:
        print("The OS is {0}".format(operatingSystem))
        path = "%systemroot%/sysnative/winevt/Logs"
        print('Path is set to {0}'.format(path))
        return path
