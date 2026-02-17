#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: Maria Sedó González
"""

# utils.py
# import the needed libraries/modules

import pandas as pd
import re

#Define your functions


#Function that asks the user for a filename and checks if it's csv or txt. It returns the file as a dataframe or a string

def filename():
    while True:
        try:
            file = input("Please, enter the name of your file here (TXT or CSV): ")
            #To check if it's csv or txt
            if file.endswith(".csv"):
                df = pd.read_csv(file)
                return df   #This returns a dataframe
            elif file.endswith(".txt"):
                h = open(file, "r")
                text = h.read()
                return text    #This returns a string
            else:
                print("Sorry. Only TXT and CSV files are allowed.")
                continue
        except FileNotFoundError: 
            print("Sorry, but the file was not found. Do you want to try it again? Remember: only TXT and CSV files.")
            continue
                


#Function with the menu options. It returns the user's choice:

def menu():
    print("\n*** M E N U ***")
    print("Welcome to the main menu! Here, you can choose between different actions. Please, select the option with its number:")
    print("1. Show basic file information")
    print("2. Search for a keyword")
    print("3. Count word frequencies")
    print("4. Extract information with regular expressions (email)")
    print("5. Load as a DataFrame and show basic stats (requirement: CSV file)")
    print("6. Quit")
    choice = input("Enter your choice (number): ")
    return choice



#Function for option 1: Show basic file information

wordsclean = []     #If I put these empty lists here, I can use them in other functions
lines_list = [] 

def basic_information(data):  
    #The isinstance() function returns True if the specified object is of the specified type. I use it to check if we are dealing with a dataframe or a string
    if isinstance(data,str):   #this treats data as a string     
        for line in data.splitlines():        
            lines_list.append(line.strip())    #adds each line to a list, without whitespaces at the end of the lines       
            words = line.split()               #to get the words of each line
            for word in words: 
                wordsclean.append(word.rstrip(".:,!"))  #to add each word to a list without the punctuation on the right of the words
        num_words = len(wordsclean)   #number of words    
        num_lines = len(lines_list)   #number of lines
        first_line = lines_list[0]    #the first line
        print("\nOption 1. File basic information:")    
        print("- Number of lines:", num_lines)
        print("- Number of words:", num_words)
        print("- First line of the file: ", first_line)
    
    elif isinstance(data, pd.DataFrame):   #this treats data as a dataframe
        columns = (data.columns)
        num_columns = len(columns)   #number of columns
        num_rows = len(data)           #number of rows: it's just the length of the dataframe
        first_row = data.iloc[[0]]        #the first row. The double brackets are used to make the data look like a table
        print("\nOption 1. File basic information:")
        print("- Number of columns:", num_columns)
        print("- Number of rows: ", num_rows)
        print("- The first row:\n", first_row)



#Function for option 2: Search for a keyword

def search_keyword(data):
     
    print("\nOption 2. Search for a keyword")
    keyword = input("Write here the keyword you want to search in the file. For example, Python: ")
    if isinstance(data,str):     #this treats data as a string
        lines_list = []
        keyword_list = []
        for line in data.splitlines():        
            lines_list.append(line.strip())    #adds each line to a list, without whitespaces at the end of the lines
        for l in lines_list:     
            if keyword in l:
                keyword_list.append(l)   #this adds the lines that contain the keyword to the keywords_list  
        if keyword_list:    #this means: if there's something in the list, do this       
            print("The lines that contain this keyword are as follows:", keyword_list)
        else:
            print("Sorry, the keyword isn't in the file.")
    
    elif isinstance(data, pd.DataFrame):   #this treats data as a dataframe     
        matched_rows = []
        for i in range(len(data)):    #these three loops let us iterate through each word in each row (in some values there are more than two words, that's why we need a third loop)
            row = data.iloc[i]         #[i] is the number of the row (row index)
            for value in row:
                value = str(value)      #convert each value to a string
                for word in value.split():
                    if keyword == word:
                        matched_rows.append(row)  #This stores all rows with the keyboard in a list                         
        keyword_dataframe = pd.DataFrame(matched_rows)  #This converts the list "matched_rows" to a dataframe
        if keyword_dataframe.shape[0] > 0:  #shape[0] = number of rows. This means: if there are more than 0 rows, print the dataframe
            print("The rows that contain this keyword are as follows:\n", keyword_dataframe)
        else:
            print("Sorry, the keyword isn't in the file.")



#Function for option 3: Count word frequencies. It counts how much times each unique word appears

count_unique_words = {}

def count_word_frequencies(data):
    print("\nOption 3. Count word frequencies ")
    print("Here, you have how many times each word appears: ")
    if isinstance(data,str):    #this treats data as a string
        for line in data.splitlines(): 
            words = line.split()   #to get the words of each line
            for word in words: 
                wordsclean.append(word.rstrip(".:,!"))  #to add each word to a list named "wordsclean" without the punctuation on the right of the words
        for w in wordsclean:
            if w in count_unique_words:       #if the word is in the dictionary "count_unique_words", this raises the count
                count_unique_words[w] = count_unique_words[w] + 1     
            else:                             #in another situation (= the word isn't in the dictionary "count_unique_words"), this adds the word to the dictionary with the count of 1
                count_unique_words[w] = 1
        for k,v in count_unique_words.items():        #to print the data in the dictionary
            print(k, ":", v)   
    
    elif isinstance(data, pd.DataFrame):  #this treats data as a dataframe
        for i in range(len(data)):    #these three loops let us iterate through each word in each row (in some values there are more than two words, that's why we need a third loop)
            row = data.iloc[i]         #[i] is the number of the row (row index)
            for value in row:
                value = str(value)      #convert each value to a string
                for word in value.split():    #for each word in every group of words(splited)
                    wordsclean.append(word.rstrip(".:,! "))  #to add each word to a list named "wordsclean" without the punctuation on the right of the words
        for w in wordsclean:
            if w in count_unique_words:       #if the word is in the dictionary "count_unique_words", this raises the count
                count_unique_words[w] = count_unique_words[w] + 1     
            else:                             #in another situation (= the word isn't in the dictionary "count_unique_words"), this adds the word to the dictionary with the count of 1
                count_unique_words[w] = 1
        for k,v in count_unique_words.items():        #to print the data in the dictionary
            print(k, ":", v)    



#Function for option 4. Extract information with regular expressions (email)

r"""
Meaning of the regex code used:

- \S: non-whitespace character. 
- +: repeats the character one or more times
- @: just @
- [.]: just a dot

"""

def info_regex_email(data):
    emails_list = []
    print("\nOption 4. Extract information with regular expressions (email)")
    if isinstance(data,str):   #this treats data as a string     
        for line in data.splitlines():        
            lines_list.append(line.strip())    #adds each line to a list, without whitespaces at the end of the lines  
        for l in lines_list:
            emails_list.extend(re.findall(r"\S+@\S+[.]\S+", l))   #.extend() takes all the findings of findall() and puts them in the list together.
                                                                  #The r makes the regex code a raw string: it is used to prevent Python to understand \S as an escape sequence. 
        if emails_list:    #This means: if there's something in the list, do this
            print("These are the emails that were found in your file: ", emails_list)
        else:
            print("There aren't emails in your file.")
    
    elif isinstance(data, pd.DataFrame): #this treats data as a dataframe
        for i in range(len(data)):    #these three loops let us iterate through each word in each row (in some values there are more than two words, that's why we need a third loop)
            row = data.iloc[i]         #[i] is the number of the row (row index)
            for value in row:
                value = str(value)      #convert each value to a string
                emails_list.extend(re.findall(r"\S+@\S+[.]\S+", value))  #.extend() takes all the findings of findall() and puts them in the list together. 
                                                                 #The r makes the regex code a raw string: it is used to prevent Python to understand \S as an escape sequence. 
        if emails_list:    #This means: if there's something in the list, do this
            print("These are the emails that were found in your file: ", emails_list)
        else:
            print("There aren't emails in your file.")



#Function for option 5. Load as a DataFrame and show basic stats (requirement: CSV file)

def dataframe_basic_stats(data):
    print("\nOption 5. Load as a DataFrame and show basic stats (requirement: CSV file)")
    if isinstance(data,str):   #this treats data as a string 
        print("Sorry, only CSV allowed for this option.")

    elif isinstance(data, pd.DataFrame): #this treats data as a dataframe
        print("These are the basic stats of your CSV file: \n")
        print("- First five rows:\n", data.head(5), "\n") 
        print("- Summary statistics: \n", data.describe(), "\n")  #describe() shows a statistically description of the data in a dataframe
        print("- Number of missing values per column:\n ", data.isna().sum(), "\n")   #.isna() creates a dataframe of booleans (True if missing) and .sum sums the number of missing values in each column 



#Function for option 6. Quit    

def goodbye():
    print("\nOkey then! Goodbye! Have a nice day ^^")
    quit()