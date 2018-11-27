# snifftest
Scan tool to check CSV files  
Note: Python 3 must be installed on computer prior to running the script. 

To run the script:
1.	Copy and paste the script file (Scanner.py), as well as the .csv file you would like to scan, to your desktop. *The file and script can be posted anywhere, but the desktop allows for the easiest access. 
2.	Click on the Windows start menu and type ‘cmd’ (excluding the parentheses). Then press ‘Enter’ on your keyboard. This will bring up the Command Prompt in a new window. 
3.	In the command prompt type ‘cd desktop’. Press enter.
4.	Enter your CSV filename without the .csv extension (ex. ‘Test File’ instead of ‘Test File.csv’) and press enter. 
5.	You will be prompted to search by Types (enter ‘T’) or Keywords (enter ‘K’). Make selection and press enter. 
6.	Once selected, the script will show the available columns with their respective numbers.
     a.	You can enter multiple columns you want checked separated by a ‘,’ (ex. 1,2,3 or 1, 2, 3)
     b.	There a checks in place to deny duplicate column names, columns that don’t exist, etc. 
7.	The script will ask you what to check for per column inputted above.    
     a.	The choices are String (‘s’), Digit (‘d’), Currency (‘c’)    
     b.	When working with types, you can enter either choice per column based on their respective column number. An example input would be 1,        2, 3 and s, c, s. This would test columns 1 and 3 for strings and column 2 for currency. 
     c.	When searching by keyword (‘k’), the process is the same except you enter the keywords to search for per column number. 
8.	Once entered, the script will display any errors found and their line numbers. 
