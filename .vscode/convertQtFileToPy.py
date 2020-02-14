import os
from os import path
import os.path

def timeOfSourcFileBiggerThanDestinationFile(src, dest):
    if os.path.exists(dest):
        srcTime=os.path.getmtime(src)
        destTime=os.path.getmtime(dest)
        if destTime<srcTime:
            return True
        return False
    else:
        return True
  
def traverseDirectoryToConvertUiToPy(rootDir):
    for subdir, dirs, files in os.walk(rootDir):
        for file in files:
            if file.split('.')[-1].lower()=='ui':
                src = os.path.join(subdir, file) 
                dest = os.path.join(subdir, file[0:-3]+".py")
                if timeOfSourcFileBiggerThanDestinationFile(src, dest):
                    os.system('pyuic5.exe'+ ' \"'+src+'\"' + ' -o' + ' \"'+dest+'\"') 
                    print("Creating: "+os.path.join(subdir, dest))

rootDir = '../'  
traverseDirectoryToConvertUiToPy(rootDir) 