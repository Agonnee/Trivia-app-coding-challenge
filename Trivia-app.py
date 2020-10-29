# Handle Imports
import json
import random
import os
import sys

# Defining classes


class A_Question():
    # Creates Questions from imported JSON
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.answers = self.incorrect + [str(self.correct)]
        random.shuffle(self.answers)


class TheQuiz(list):
    def __init__(self, singles=None):
        self.singles = singles
            
    # Generating questions for the quiz
    @classmethod
    def create_thequiz(cls, dataset, how_many):
        singles = []
        for single in dataset[0:int(how_many)]:
            singles.append(A_Question(**single))
        return cls(singles)


# change directory to that of the script
os.chdir(os.path.dirname(__file__))
# Importing JSON file for the question generator
with open('Apprentice_TandemFor400_Data.json',encoding='utf-8') as f:
    dataset = json.load(f)


def run_the_quiz():
    random.shuffle(dataset)

    # Welcome to the Trivia Quiz
    print("----------------------------\nWelcome to the Trivia Quiz!\n----------------------------\n\nHopefully this will help you get better at answering questions!")
    begin_prompt = True
    how_many = ""
    while begin_prompt == True:
        standard_round = input("\nWould you like to play a standard round of Trivia? (y/n)  ").lower()
        if standard_round == "y":
            how_many = 10
            begin_prompt = False
        elif standard_round == "n":
            custom_round = input("\nWould you like a custom round? (y/n)  ").lower()
            if custom_round == "y":
                how_many = input("\nHow many questions would you like?  ")
                while str(type(how_many)) != "<class 'int'>":
                    try:
                        how_many = int(how_many)
                    except ValueError:
                        print("\nI'm sorry, I don't recognize that answer.")
                        how_many = input("\nHow many questions would you like?  ")
                    else:
                        begin_prompt = False
            elif custom_round == "n":
                print("\nHave a nice day!")
                sys.exit()
            else:
                print("\nI'm sorry, I don't recognize that answer.")
        else:
            print("\nI'm sorry, I don't recognize that answer.")

    qz = TheQuiz.create_thequiz(dataset, how_many)

    number_right = 0
    number_total = (len(qz.singles))
    quest_num = 0

    # asking the user the questions 1 at a time

    for i in range(len(qz.singles)):
        quest_num += 1
        print ("\nQuestion {}.\n".format(quest_num), qz.singles[i].question, "\n")
        num = 0
        # single answer multiple choice
        for j in qz.singles[i].answers:
            num += 1
            print ("{}.".format(num), j)
        try:
            checker = abs(int(input("\nAnswer: ")))                           
        except ValueError:
            print("\nThat's not a valid answer! \nPlease only enter an answer in the valid range of answers.\n The answer was {}\n".format(qz.singles[i].correct))
        else:
            try:                
                # Display correct answer after submission
                if checker == 0:
                    print("\nThat's not a valid answer! \nPlease only enter an answer in the valid range of answers.\n The answer was {}\n".format(qz.singles[i].correct))
                elif qz.singles[i].answers[checker-1] == qz.singles[i].correct:
                    number_right +=1
                    print("\nYou're Right!\n\n")
                else:
                    print("\nSorry, the right answer was {}\n\n".format(qz.singles[i].correct))
            except IndexError:
                print("\nThat's not a valid answer! \nPlease only enter an answer in the valid range of answers.\n The answer was {}\n".format(qz.singles[i].correct))
            
    # Resulting Score, play again prompt
    print("Congrats! Your score was: {}/{}".format(number_right, number_total))

run_the_quiz()

while True:
    play_again = input("Do you want to play again? (y/n):  ").lower()
    if play_again == "y":
        run_the_quiz()
    elif play_again == "n":
        break
    else:
        print("Sorry, that's not y or n, please try again.")
