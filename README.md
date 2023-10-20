# Software-for-hand-movement-coordination-assessment-using-a-computer-mouse
**The software was developed as a result of my bachelor's thesis under the mentorship of [dr Nadica Miljkovic](https://automatika.etf.bg.ac.rs/en/department-personnel/98-english/content/faculty/615-phd-nadica-miljkovi%C4%87).**
***
### Table of Contents
1. [Introduction](https://github.com/vladajankovic/Software-for-hand-movement-coordination-assessment-using-a-computer-mouse/blob/master/README.md#1-introduction)
2. [Requirements and installation](https://github.com/vladajankovic/Software-for-hand-movement-coordination-assessment-using-a-computer-mouse/blob/master/README.md#2-requirements-and-installation)
3. [User interface overview](https://github.com/vladajankovic/Software-for-hand-movement-coordination-assessment-using-a-computer-mouse/blob/master/README.md#3-user-interface-overview)
4. [Software features](https://github.com/vladajankovic/Software-for-hand-movement-coordination-assessment-using-a-computer-mouse/blob/master/README.md#4-software-features)
5. [Software testing examples](https://github.com/vladajankovic/Software-for-hand-movement-coordination-assessment-using-a-computer-mouse/blob/master/README.md#5-software-testing-examples)
***
### 1. Introduction
The hand movement coordiantion assessment software represents a version of the [***Modified Drawing Test***](https://www.researchgate.net/publication/270468778_The_modified_drawing_test_for_assessment_of_arm_movement_quality) (*mDT*) for personal computers. The purpose of the *mDT* is for examining the hand movement coordination of patients, who have survived a stroke and are rehabilitating their upper extermites (arms). The patient is required to draw a line along a given rectangular path, as fast and percise as possible, while supervised by therapists. The size of the path model is determined by the patients range of motion. The *mDT* score is determined by the speed, smoothness and percision error metrics. It is important to note that the *mDT* is not meant for training, only testing.  
 
The hand movement coordiantion assessment software is implemented for training and testing patients during rehabilitation. Its GUI is designed to be as simple as possible for the user/patient. The software was developed in Python, using mostly the pygame library for creating and implementing simple GUIs, user interactions, event processing...  
A list of all Python libraries and modules used in developing the software:
+ [Pygame library](https://www.pygame.org/news)
+ [NumPy library](https://numpy.org/)
+ [OS module](https://docs.python.org/3/library/os.html)
+ [Datetime module](https://docs.python.org/3/library/datetime.html)

Training and testing is conducted by first selecting the appropriate option in the main menu and moving the cursor on the screen. The cursor on the screen is moved by moving the computer mouse and can be slowed down or sped up by pressing certain keys on the keyboard. The cursor sensitivity levels corresponds to different sizes of the path models for the *mDT*. A smaller sensitivity level leads to more mouse movement required to move the cursor on the screen a certain distance. That is equivalent to having a larger size model of the path that the patient traces. On the other hand, a larger sensitivity level leads to les mouse movement required to move the cursor, which is equivalent to having a smaller size path model. This is important because unlike the *mDT*, which adjusts the model size to the patients range of motion, the software has a fixed model size of the path, determined only by the size and resolution of the monitor screen.

The main feature of the software is the testing module, in which the user/patient can test their hand movement coordination. To complete the test, the user/patient must trace a line along the middle of the path on the screen and return to the starting position, indicated by a small red square. The test calculates how close the cursor is to the middle of the path. The drawing precision score is calculated continuously as a precentage in the range [0, 100] %. When the test is finished, the results are saved and a popup window indicates that the user has completed the test and can restart it or go back to the main menu. The test scoring system was inspired by the browser game [***Draw a Perfect Circle***](https://neal.fun/perfect-circle/) created by [Matt Round](https://mattround.com/).
  
To run the software on a computer, it is not required to have Python and all the dependencies (libraries and modules) installed localy. Executable files for Windows OS and Linux OS are provided using the PyInstaller tool. The only downside is that executable files created using PyInstaller can be labled as viruses because ***the executables do not have a signed certificate***, which requires paying. Because of that, some antiviruses lable it as a ***FALSE POSITIVE***.

***
### 2. Requirements and installation
Hardware:
+ Computer mouse
+ Keyboard
  + Escape
  + Arrow UP
  + Arrow DOWN
  + Space
  + Return
  
Software: Windows OS or Linux OS  
To install the software, simply download the appropriate archive for your OS, unpack it and run the executable file in the folder.
***
### 3. User interface overview

***
### 4. Software features

***
### 5. Software testing examples
