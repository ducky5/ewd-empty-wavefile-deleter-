#code I found on this website: https://sites.utexas.edu/margolis/2021/04/16/script-the-removal-of-blank-mp3-files-with-python/
#it removes silent wave files from a given directory

from pydub import AudioSegment
import os
import fnmatch

def askForDirectory():
    return input('Directory: ')

def findAllDeadMP3(toDelete):
    for dirpath, dirnames, files in os.walk(askForDirectory()):
        #Iterate through files and folders in the current directory
        for file_name in files:
            #Iterate through the files in the current directory
            if fnmatch.fnmatch(file_name,'*.wav'):
                #If the file is an wav, find its full path
                pathtofile = os.path.abspath(os.path.join(dirpath,file_name))
                print("Looking at: ", pathtofile)
                #Look at the size of the file in bytes, had an issue with small corrupted files
                sizeoffile = os.stat(pathtofile).st_size
                if sizeoffile > 1000:
                    sound = AudioSegment.from_file(pathtofile, format="wav")
                    SampMax = sound.max
                    print(file_name, "is a wav, and its loudest sample is: ", SampMax)
                    if SampMax == 0:
                        toDelete.append(pathtofile)
                else:
                    toDelete.append(pathtofile)

def DeleteFiles(toDelete):
    for path in toDelete:
        if os.path.exists(path):
            os.remove(path)
            print("Removing: ", path)
        else:
            print("The file does not exist")

IsDead = list()
findAllDeadMP3(IsDead)
DeleteFiles(IsDead)
