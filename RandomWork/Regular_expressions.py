#!/usr/bin/env python
# coding: utf-8
# Author : Narendra.b.sinappa


# Regular expressions
# Meta characters are used to define the patterns "[] . ^ $ * + ? {} () \ | "
import re
# Choose the pattern that your looking for....
pattern = "^N.w$"
string = input("Enter the string : ")
result = re.match(pattern,string)
if result:
    print("yes")
else:
    print("No")
    
    
# check if there is integer between the given string
pattern = "\d"
string = input("enter the string : ")
result = re.findall(pattern,string)
result = re.split(pattern,string)
print(result)


# search for alphnumeric character [a-zA-Z0-9_]
pattern = "\w"
string = input("enter the string : ")
result = re.findall(pattern,string)
print(result)
# replace all the apphanumeric characters into a special character ex : %%$%*&
replace = "*"
result = re.sub(pattern,replace,string)
print(result)



# search for non alphanumeric character
pattern = "\W"
string = input("enter the string : ")
result = re.findall(pattern,string)
# Replace all special characters with a space " "
replaceSTR = " "
result = re.sub(pattern,replaceSTR,string)
print(result)


#search for white space and replace it with "_"
pattern = "\s"
string = input("enter the string : ")
result = re.findall(pattern,string)
print(result)
# Replace all special characters with a space " "
replaceSTR = "_"
result = re.sub(pattern,replaceSTR,string)
print(result)


# check if the sentence is starting with a particular string/word
pattern = "\Athe"
string = input("enter the string : ")
result = re.match(pattern,string)
if result:
    print("yes")
else : 
    print("no")
    


# check if the word starting with specified string 
pattern = "\bpython"
string = input("enter the string : ")
result = re.search(pattern,string)
if result:
    print("yes")
else : 
    print("no")
    
# check if the string has both the specified characters..

pattern = "a|b"
string = input("enter the string : ")
result = re.match(pattern,string)
if result:
    print("yes")
else : 
    print("no")
    
# check if the string has atleast 3 continuous numbers and at most 4 numbers...
pattern = "[0-9]{3,4}"
string = "python2548 scripting 14588951"
result = re.findall(pattern,string)
print(result)


# check if the string has number followed by the word "python"

pattern = "(0|1|2|3|4|5|6|7|8|9)python"
string = "1python"
result = re.match(pattern,string)
if result:
    print("yes")
else:
    print("no")

    
# check if the character is repeated 2 or three times continuously in a word/given string
pattern = "a{2,3}"
string = "aaa bc aa cd aaaa"
result = re.findall(patter,string)
print(result)










