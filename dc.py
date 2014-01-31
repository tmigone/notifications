from textParser import *
from pushover import sendNotification


newFiles = []
newFiles.append("samples/dc.txt")
# call to get new files 
# newFiles = getNewFiles()

for fileName in newFiles:
    service = ''
    value = ''

    service = getService(fileName, "servicio")
    value = getValue(fileName)
    
    if service and value:
        sendNotification(createMessage(service, value))
    
    print(service)
    print(value)   