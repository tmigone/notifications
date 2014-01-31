from textParser import *
from pushover import sendNotification
from os import listdir
from os.path import isfile, join


path = "/Users/tomi/Documents/notifications/samples"
newfiles = [ f for f in listdir(path) if (isfile(join(path,f)) and f != ".DS_Store") ]

# newFiles.append("samples/cc.txt")
# call to get new files 
# newFiles = getNewFiles()

for fileName in newFiles:
    service = ''
    value = ''

    service = getService(fileName, "establecimiento")
    value = getValue(fileName)
    
    if service and value:
        sendNotification(createMessage(service, value))
    
    print(service)
    print(value)   