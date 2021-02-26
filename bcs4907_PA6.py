#Benjamin Stanelle
#1001534907
#4/27/2020
#Windows 10 Pro x64, using Python Version 3.7
import os
def main():
    cwd=os.getcwd()     #get current working directory that this file is in
    total=0
    total=getAllFileSize(cwd)           #call to recursive function
    print(total/1000, "Kilobytes")      #print in kilobytes
    
def getAllFileSize(cwd):                #take in directory 
    total=0
    for filename in os.listdir(cwd):    #list all the files in that directory
        file=os.path.join(cwd,filename) #concatenate the current directory and file names
        if os.path.isdir(file):         #new concatenated string tested to see if directory
            total+=getAllFileSize(file) 
        elif os.path.isfile(file):      #or if file
            total+=os.path.getsize(file)    #if directory recursively call getAllFileSize
                                            #if file calculate the sum of the files
        else:
            continue
        
    return total
main()
