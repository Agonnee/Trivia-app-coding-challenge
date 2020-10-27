#Handle Imports
import json
import random
import os

#Defining classes


#change directory to that of the script
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#Parsing the JSON file for the question generator
with open('Apprentice_TandemFor400_Data.json') as f:
  data = json.load(f)

print(data)
input("what now")

#Welcome to the Trivia Quiz


#Generating questions for the quiz


#asking the user the questions 1 at a time


#single answer multiple choice


#Display correct answer after submission


#Resulting Score, play again prompt
