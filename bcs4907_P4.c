/*Benjamin Stanelle
1001534907
4/16/2020
Windows 10 Pro x64 
*/
#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <sys/stat.h>
#include <string.h>
#include <errno.h>

long fileSizeAccumulator(char* dir){  

    DIR *d;   //type: directory stream
    d = opendir(dir);  //open directory specified by dir
    if(! d){  //if the directory doesn't exist
        return 0;
    }

    long size=0;
    char dirName[1024];
    struct dirent* entry; // dirent has type serial number(d_ino) and name of entry  (d_name[])
    struct stat buf; //Buffer for reading file
   
    while(entry=readdir(d)){ //the next file or folder in the directory is not Null or an error, loop
        
	if(strcmp(entry->d_name, ".")==0 || strcmp(entry->d_name, "..")==0){ //if readdir returns the current directory(.) or the above directory (..)
           continue; //go to the next
        }
        memset(dirName,0,strlen(dirName)); //Empty the string dirName

        strcat(dirName, dir); //current directory 
        strcat(dirName, "/"); // next 
        strcat(dirName, entry->d_name); //readdir returns next a pointer to the next file or directory which is now in the structure  entry

        if(stat(dirName, &buf)!=0){ //File doesn't exist
            continue; //Move on
        }

        if(S_ISDIR(buf.st_mode)){ //If the file is a directory returns non-zero
            size+= fileSizeAccumulator(dirName); //recursively enter that directory
        }
	else{
            size += buf.st_size; //Else add the file
        }

    }
    closedir(d);
    return size;
}

int main()
{
  long size = fileSizeAccumulator(".");
  printf("Total number of bytes: %ld\n", size);

  return 0;
}