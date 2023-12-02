# Student names:
* 1)	Kulaphong Jitareerat, 67761544
* 2)	Nijiati Abulizi, 59764100

# Quizzer App

The Quizzer App is a software package designed to conduct quizzes. It comprises two sub-packages:

**Sub-package #1**: User Interface/Quiz Manager

This is the front end of the app where users interact with the system and manage quizzes:

**Module1**: User interface
-	Handles main menu
-	Greets the user
-	Displays the menu

**Module2**: Flow control

-	Displays a list of available quizzes
-	Handles the selection process
-	Starts the quiz
-	Manages the flow of questions and answers during a quiz session
-	Displays and save the results at the end of a quiz

**Sub-package #2**: Creates quiz objects from databases gathered from free online sources and communicates with the sub-package #1.

**Module1**: Parsing questions from databases to quiz objects
-	Retrieve questions from databases such as JSON
-	Parses quizzes

File: quizparser.py  
```class JSONQuizParser```: is used for importing quiz data from JSON file.   
Functions:   
1. import_data(quizpath)  
	The function takes the JSON file path and then opens/loads the data into a dictionary, which is the output of the function.
2. create_question_obj(data)  
	The function takes the quiz data dictionary (output of the function ```import_data(quizpath)```), and returns the question objects that contain information for use during the quiz session.
3. parse_quiz(quizpath)  
	The main function that calls others for extracting the quiz data from the JSON file and creates a quiz object.  

**Module2**: Creates quiz objects
-	Defines quiz properties such as questions, answers
-	Enables to take the quiz
-	Keeps track of the participant’s score
-	Times the quiz duration for each participant

File: quiz.py  
```class Quiz```: contains all information for the quiz session, including questions, answers, and points.  
Functions:  
1. print_header(idx)  
	The function takes ```idx```, which is the number of the question, and prints the header of each question.
2. print_results(quiztaker)  
	The function takes a quiz to visualize the user's name for printing the user results.  
3. take_quiz()  
	The function runs the quiz session after the user selects the quiz to take.
4. cal_score()  
	The function calculates the score of the quiz session. Calculating the score is divided into two parts: calculating the question's score and extra score, which is related to the user's time spending on each question. For the extra score, if the user answers correctly, they will get an extra 5 points for answering within 1 second. Otherwise, they will get the ratio of 5 over the time spent (in seconds). If they answer incorrectly, they will not get the extra score.

```class Question```: stores all the question information for running the quiz session.       

```class QuestionTF```: stores the True or False question type. This object is used when the program is waiting for the user's answer.  
Functions:  
1. ask()  
	The function prints the True/False question information to the users and gets a response from them.

```class QuestionMC```: stores the Multiple Choice question type. This object is used when the program is waiting for the user's answer.   
Functions:   
1. ask()  
	The function prints the Multiple Choice question information to the users and gets a response from them.  

```class Answer```: stores the answers of each question.   


Overall, the package is a cohesive system for conducting quizzes efficiently, tracking performance, and managing quiz content.
