# Quizzer App

## BuildStamp
[![Build Status](https://app.travis-ci.com/Nijat27/Quizzer.svg?branch=main)](https://app.travis-ci.com/Nijat27/Quizzer)

The Quizzer App is a software package designed to conduct quizzes. It comprises two sub-packages:

## **Sub-package #1**: User Interface/Quiz Manager (Folder Name: quizuiflowcontrol)

This is the front end of the app where users interact with the system and manage quizzes:

### **Module1**: User interface
-	Handles main menu
-	Greets the user
-	Displays the menu

#### File: main_menu.py
```class QuizApp```: is used to manage the Quiz Application user interface and flow.

#### Functions
1. `__init__`: Initializes the QuizApp.
2. `run`: Starts the main application loop.
3. `display_welcome_message`: Displays a welcome message.
4. `ask_user_name`: Asks the user to input their name.
5. `main_menu`: Displays the main menu and processes user input.
6. `show_menu_options`: Shows the available menu options.
7. `display_error_message`: Displays an error message for invalid selections.
8. `exit_app`: Exits the application.
9. `list_quizzes`: Lists all available quizzes.
10. `take_quiz`: Handles the logic of taking a quiz.


### **Module2**: Flow control

-	Displays a list of available quizzes
-	Handles the selection process
-	Starts the quiz
-	Manages the flow of questions and answers during a quiz session
-	Displays and save the results at the end of a quiz

#### File: quizmanager.py:
```class QuizManager```: is used to manages the quizzes, including listing, taking, and saving results of quizzes

#### Functions
1. `__init__`: Initializes the QuizManager.
2. `_build_quiz_list`: Builds a list of quizzes from JSON files.
3. `list_quizzes`: Lists all available quizzes.
4. `take_quiz`: Facilitates taking a quiz.
5. `print_results`: Prints the results of the quiz.
6. `save_results`: Saves the quiz results to a file.

## **Sub-package #2**: Creates quiz objects from databases gathered from free online sources and communicates with the sub-package #1. (Folder name: quizutils)

### **Module1**: Parsing questions from databases to quiz objects
-	Retrieve questions from databases such as JSON
-	Parses quizzes

#### File: quizparser.py  
```class JSONQuizParser```: is used for importing quiz data from JSON file.

#### Functions:   
1. `import_data`: The function takes the JSON file path and then opens/loads the data into a dictionary, which is the output of the function.
2. `create_question_obj`: The function takes the quiz data dictionary (output of the function ```import_data```), and returns the question objects that contain information for use during the quiz session.
3. `parse_quiz`: The main function that calls others for extracting the quiz data from the JSON file and creates a quiz object.  

### **Module2**: Creates quiz objects
-	Defines quiz properties such as questions, answers
-	Enables to take the quiz
-	Keeps track of the participant’s score
-	Times the quiz duration for each participant

#### File: quiz.py  
```class Quiz```: contains all information for the quiz session, including questions, answers, and points.  

#### Functions:  
1. `print_header`: The function takes ```idx```, which is the number of the question, and prints the header of each question.
2. `print_results`: The function takes a quiz to visualize the user's name for printing the user results.  
3. `take_quiz`: The function runs the quiz session after the user selects the quiz to take.
4. `cal_score`: The function calculates the score of the quiz session. Calculating the score is divided into two parts: calculating the question's score and extra score, which is related to the user's time spending on each question. For the extra score, if the user answers correctly, they will get an extra 5 points for answering within 1 second. Otherwise, they will get the ratio of 5 over the time spent (in seconds). If they answer incorrectly, they will not get the extra score.

```class Question```: stores all the question information for running the quiz session.       

```class QuestionTF```: stores the True or False question type. This object is used when the program is waiting for the user's answer.  
Functions:  
1. `ask`: The function prints the True/False question information to the users and gets a response from them.

```class QuestionMC```: stores the Multiple Choice question type. This object is used when the program is waiting for the user's answer.   
Functions:   
1. `ask`: The function prints the Multiple Choice question information to the users and gets a response from them.  

```class Answer```: stores the answers of each question.   

Overall, the package is a cohesive system for conducting quizzes efficiently, tracking performance, and managing quiz content.

# Getting Started

## To start using the Quiz App, follow these steps:

### Prerequisites

- Ensure you have Python installed on your system. The application has been tested with Python 3.9 and higher.

### Quiz App Installation and Usage Guide

There are two methods to install the Quiz App:

### Method 1: Using pip

**Easy Guide to QuizzerApp: Install & Explore Key Features!**
Start the video by clicking on the following YouTube thumbnail
[![img/thumbnail.png](img/thumbnail.png)](https://youtu.be/BP4dj7hiOCI)

You can install the Quiz App directly using pip by running the following command:

```bash
pip install quizzerapp
```
#### Running the App

After installing through pip, you can run the application as a Python module from any location in your terminal or command prompt:

```bash
python -m Quizzer
```

### Method 2: Cloning or Downloading the Repository

1. Clone or download the Quiz App repository to your local machine.
2. Navigate to the app directory in your terminal or command prompt.

#### Running the App

- Execute the application by running the following command:

```bash
python main.py
```

## Using the Quiz App

Once the app is running, you will be greeted with a welcome message and prompted to enter your name.

### Main Menu

The main menu offers the following options:

- **List Quizzes (L):** Displays a list of available quizzes.
- **Take a Quiz (T):** Allows you to select and take a quiz.
- **Exit the App (E):** Exits the application.

### Taking a Quiz

1. Select the option to take a quiz.
2. Enter the quiz number you wish to attempt.
3. Answer the questions as they appear.
4. Upon completion, your results will be displayed.

### Viewing Quiz Results

- After completing a quiz, your results are displayed on the screen, showing your score and the number of correct answers.

## Troubleshooting

To test the Quizzer app, you can run the following code:
```bash
python3 unittest_main.py
```
This test conducts unit tests each of the four modules.

If you encounter any issues:

- Check that you are using a compatible Python version.
- Ensure the JSON files for quizzes are correctly formatted and located in the 'Quizzes' folder.
- Ensure the JSON files for quizzes are correctly formatted and located in the 'db_quizzes' folder.
- Review any error messages in the console for guidance.

## Test Coverage
![img/coverage_test1.png](img/coverage_test1.png)

## Contributing

Contributions to the Quiz App are welcome. Please feel free to fork the repository, make changes, and submit pull requests.

## License

# Student names:
* 1)	Kulaphong Jitareerat, 67761544
* 2)	Nijiati Abulizi, 59764100
