from textParser import *
from pushover import sendNotification
from os import listdir
from os.path import isfile, join
import shutil


path = "/home/ec2-user/Dropbox/IFTTT/Gmail - Visa"
processedPath = "/home/ec2-user/notifications/processed"
newFiles = [ f for f in listdir(path) if (isfile(join(path,f)) and f != ".DS_Store") ]


for fileName in newFiles:

    fileName = path + "/" + fileName
    service = ''
    value = ''

    service = getService(fileName, "establecimiento")
    value = getValue(fileName)
    
    if service and value:
        sendNotification(createMessage(service, value))
        shutil.move(fileName,processedPath)
    
    print(service)
    print(value)   