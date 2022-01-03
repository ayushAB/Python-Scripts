import os
import shutil
#get all files in the current directory
listOfFilesInDirectory = os.listdir()
#above array has all file names in the directory this script will be executed.
print(listOfFilesInDirectory)
#array of extenstion to be sorted
extensions=['exe','jpg','jpeg','py']
#get current working directory
currentDirectoryPath=os.getcwd()
#create folder for each extension
for extension in extensions:
  if not os.path.isdir(currentDirectoryPath+"/"+extension):
    os.mkdir(currentDirectoryPath+"/"+extension)
  
#loop through each file and change the diectory for that file according to extension
for fileName in listOfFilesInDirectory:
  for extension in extensions:
    extns=fileName.rsplit('.',1)
    if extns[1]==extension:
      des = shutil.move(fileName,currentDirectoryPath+'/'+ extension)
	 

