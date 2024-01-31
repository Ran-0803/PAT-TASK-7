
# File handling
import datetime
def createFile():
    currTime = datetime.datetime.now()
    print(currTime)
    file=open("Currenttime.txt",'w')
    file.write(str(currTime))
    file.close()

createFile()

# Read the file
def readtextfile():
    file=open("Sample.txt",'r')
    print(file.read())
    file.close()
readtextfile()








