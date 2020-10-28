#Handle Imports
import json
import random
import os

#Defining classes
class Singleton:

    def __init__(self, prompt, wrongs, right):
        self.prompt = prompt
        self.wrongs = wrongs
        self.right = right

    @property
    def answers():
        self.wrongs.append(self.right)
        self.wrongs.sort()

class TheQuiz:
    def __init__(self, singles=None):
        self.singles = singles

#Generating questions for the quiz
    @classmethod
    def create_thequiz(cls, dataset):
        singles = []
        for single in dataset[0:10]:
            for key in single.keys():
                singles.append(Singleton(single['question'], single['incorrect'], single['correct']))
            return cls(singles)

#change directory to that of the script
os.chdir(os.path.dirname(__file__))


#Parsing the JSON file for the question generator
with open('Apprentice_TandemFor400_Data.json') as f:
  dataset = json.load(f)

random.shuffle(dataset)

##print(data[0])

##for qstn in dataset[0:10]:
##    for v in qstn.values():
##        print(v)




##print(qz)
##print(qz.singles)
print(str(qz.singles[0]))

#Welcome to the Trivia Quiz
qz = TheQuiz.create_thequiz(dataset)


#asking the user the questions 1 at a time


#single answer multiple choice


#Display correct answer after submission


#Resulting Score, play again prompt


input("what now")  #Holding console open for informational purposes
