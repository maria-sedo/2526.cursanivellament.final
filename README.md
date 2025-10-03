
***README.TXT*** 


*Introduction*
Welcome to my small Data Explorer Program! ^^ This program allows the user to load, search, and analyse text-based data (CSV or TXT). 

*How to run the program*
The program is divided into two modules: main.py and utils.py. The module main.py contains the main flow of the program, while utils.py contains functions used in main.py. Therefore, to run the program, you only need to run main.py. 

*Menu System*
When the program starts, the user must enter the name of the file he wants to analyse. Then, the user is asked to choose between different actions from the main menu. The different actions are as follows: “Show basic file information”, “Search for a keyword”, “Count word frequencies”, “Extract information with regular expressions”, “Load as a DataFrame and show basic stats (requirement: CSV file)” and “Quit”. Each action must be selected writing the number it has assigned. All actions support both TXT and CSV files, except number 5, which requires a CSV file.

I hope you enjoy this small Data Explorer Program.




*Sources used*

I have used ChatGPT to search for the purposes listed here, but I have never asked it to give me the solutions, just the theory to do the project:

- Understand the templates of main.py and utils.py given by the teacher.
- How to separate the treatment that TXT and CSV files receive. I didn’t know “.endswith()” and “isinstance()”.
- Understand tracebacks (like the one I got when trying to append rows to a new dataframe. I learned “row.to_frame().T”.
- Ideas on what type of information can I display about TXT files and CSV files. 
- How to iterate through the values of a dataframe.

These are specific internet sources I used:

- Python for Everybody (especially for regex).
- www.W3schools.com (“Python tutorial” and “Pandas tutorial”)

