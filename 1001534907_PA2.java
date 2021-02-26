//Benjamin Stanelle 
//1001534907
//3/312020
//Java Version: jdk-13.0.2        OS: windows 10 pro 64x
import java.io.File;
import java.io.IOException;
public class 1001534907_PA2 {
	
	public static void main(String args[]) 
    { 
       File currentDir= new File("."); //The current directory
       long totalSum=directoryDisplay(currentDir);
       if(totalSum >= 1000) {
    	   double sizekb= (double)totalSum;
           sizekb=sizekb/1000;
    	   System.out.println(sizekb + " kilobytes");
       } else if(totalSum>= 1000000) {
    	   double sizekb= (double)totalSum;
           sizekb=sizekb/1000000;
    	   System.out.println(sizekb + " megabytes"); 
       } else {
    	   System.out.println(totalSum + " bytes"); 
       }
       
    } 
	
	public static long directoryDisplay(File currentDir) {  //recursive function for getting the files and sub directories, and getting sum of file size in bytes
		long sum=0;
		try {File[] files= currentDir.listFiles(); //Makes an array of the files and sub-directories   
		for(File file: files) { 	//loops through each file in the Array of files (the Current directory) to check and see if it is a directory or a text file
			if(file.isDirectory()) {		//library function for determining if it is a directory 
				System.out.println("Directory:" + file.getCanonicalPath());  //printing out the current path
				sum += directoryDisplay(file);  //recursive step, when it is a sub-directory take what ever files or sub directories are in that and sum them
			}
			else {
				System.out.println("     file:" + file.getCanonicalPath()); //if its not a directory sum the file lengths
				sum += file.length();  //add file bytes to the sum
			}
		
		}
		
		}
		catch (IOException e) {
			e.printStackTrace();
		}
		return sum;
	}
	
}

