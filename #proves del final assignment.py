#proves del final assignment
import utils
import pandas as pd

data = utils.filename()





def basic_information(data):
    #The isinstance() function returns True if the specified object is of the specified type. I use to check if we are dealing with a dataframe or a string
    if isinstance(data,str):   #this treats data as a string
        wordsclean = []
        lines_list = []       
        for line in data.splitlines():
            lines_list.append(line.strip())    #adds each line to a list, without whitespaces at the end of the lines       
            words = line.split()               #to get the words of each line
            for word in words: 
                wordsclean.append(word.rstrip(".:,!"))  #to add each word to a list without the punctuation on the right of the words
        num_words = len(wordsclean)   #Number of words    
        num_lines = len(lines_list)   #Number of lines
        first_line = lines_list[0]    #The first line
        print("Option 1. File basic information:")    
        print("Number of lines:", num_lines)
        print("Number of words:", num_words)
        print("First line of the file: ", first_line)
    elif isinstance(data, pd.DataFrame):   #this treats data as a dataframe
        print("meh")

basic_information(data)

quit()

file = input("Please, enter the name of your file here (TXT or CSV): ")

h = open(file, "r")
wordsclean = []
lines_list = []

#Number of lines
for line in h:
    lines_list.append(line.strip())
    #lines = line.strip()
    #print(lines)   
    #Num_lines = len(lines)   #this is the number of characters!!!!!!!!
    #print(Num_lines)
    #number of words
    words = line.split()
    for word in words: 
        wordsclean.append(word.rstrip(".:,!"))  #to get rid of the punctuation on the right of the words
#print(len(wordsclean))
print(lines_list)
print(len(lines_list))
print(wordsclean)
first_line = lines_list[0]
print(first_line)

#data.strip().split()

#num_characters = len(h)
#print(num_characters)





if isinstance(h,str):   #this treats data as a string
    #Number of lines
    data.strip().split()
    #Number of words

    #Number of characters
    num_characters = len(h)
    print(num_characters)
    #First line
    print("Option 1. File basic information:") 
    print("")
    print("")
    prtin("Number of characters: ", num_characters)
    print("")
    

"""
#codi original per a def basic_information(data) que crec que està malament
#def basic_information(data):
    #The isinstance() function returns True if the specified object is of the specified type. I use to check if we are dealing with a dataframe or a string
    #if isinstance(data,str):   #this treats data as a string
    #    wordsclean = []
    #    lines_list = []
    #    #Name of the file

        #Number of lines
     #   for line in data:
      #      lines = line.strip()
       #     num_lines = len(lines)
        #Number of words
        #    words = lines.split()
            for word in words: 
                wordsclean.append(word.rstrip(".:,!"))  #to get rid of the punctuation on the right of the words
        num_words = len(wordsclean)      
        #First line
        lines[0]
        print("Option 1. File basic information:") 
        print("Name of the file: ", )
        print("Number of lines: ", num_lines )
        print("Number of words:", num_words)
        print("Number of characters: ", num_characters)
        print("First line of the file: ", )
    elif isinstance(data, pd.DataFrame):   #this treats data as a dataframe
"""


"""
Brut guardat de la funció search_keyword(data), per si el document és csv. No acosnegueixo que funcioni:

elif isinstance(data, pd.DataFrame):    #this treats data as a dataframe
        for i in range(len(data)):
            row = data.iloc[i]
            if any(keyword in str(value) for value in row):
                print("The rows that contain this word are as follows: ", row)
            else:
                print("Oops, we didn't find any row with the keyword")

"""