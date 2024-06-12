from datetime import datetime


fileToWrite = open("dd.txt", "a", encoding="utf-8")
now = datetime.now()
str = now.strftime('%Y-%m-%d %H:%M:%S')
fileToWrite.write(str)  
fileToWrite.close()