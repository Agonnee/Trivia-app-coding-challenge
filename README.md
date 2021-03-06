# Trivia-app-coding-challenge

An app that can be used to study or learn trivia!

## To Run:

1. Ensure Python 3 is installed on your computer, if not download Python 3 at https://www.python.org/
2. Ensure the .json data file and Trivia-app.py are in the same folder/directory on your computer.
3. Run the Trivia-app.py file.

## To Use:

1. Once running you will be welcomed to the Trivia Quiz and asked how many questions you'd like to be asked.
2. Reply to each question prompt with the associated number to the answer you'd like to submit.
3. Once completed you will be given your score and asked if you'd like to play again!
4. Enjoy!


## Data Format:

To add further data, or a separate questions list requires .json files formatted as shown below. The file must be added to the directory, and the name of the file must be changed in the open statement in Trivia-app.py.

[
  {
    "question": "What is the first letter of the Alphabet?",
    "incorrect": ["B", "C", "D"],
    "correct": "A"
  },
]


## Additional Features to add:

Graphical User Interface to increase read ability and User experience.

A timer, to record time to answer metrics and provide user with performance statistics

A user friendly method to switch .json files if necessary in the future.

The ability to accept other files types and parse the questions from them.

A user friendly method to create questions instead of hand typing .json as described above.

A High Scores list, organized by what files were used to generate the quiz.

A Unit test of some kind to automate testing as additional features are added.

## Known Issues:

Ensuring Python 3 is installed and all files from this repository are located in the same directory should allow this to run.

The only python libraries imported are those contained within Python itself.

No currently known issues.






