#Benjamin Stanelle
#1001534907
#4/8/2020
#Windows 10 Pro 64-bit operating system, x64-based processor

#Python 3.7 on Anaconda: Spyder.
def main():
    
    file1 = open("input_EC.txt", "r") 
    max=0
    currentMax=0
    balance=0
    for x in file1: #Loop through each line in the file
        temp=0   #for counting the number of '{'  or  '}' in a line
        if '/' in x: #Disregard that line if it is a comment
            print(max, x)
            continue
        
        if '{' in x and '"' not in x: #when the line is not " and contains { 
            temp=x.count('{')  #count the number of {
            currentMax+=temp;
            if currentMax>max: #update the max and print
                max=currentMax
            print(max, x)
        elif '}' in x:    #subtract one from the max if }
            print(max, x)
            temp=x.count('}')
            currentMax-=temp
            max-=temp
        else:  #if neither { nor } print the max
            print(max, x)
        
    file1.close()
main()
