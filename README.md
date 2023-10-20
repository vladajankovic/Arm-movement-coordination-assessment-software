# Software for arm movement coordination assessment using a computer mouse
**This software was developed as a result of my bachelor's thesis under the mentorship of [dr Nadica Miljkovic](https://automatika.etf.bg.ac.rs/en/department-personnel/98-english/content/faculty/615-phd-nadica-miljkovi%C4%87).**
***
### Table of Contents
1. [Introduction](https://github.com/vladajankovic/Software-for-arm-movement-coordination-assessment-using-a-computer-mouse/blob/master/README.md#1-introduction)
2. [Requirements and installation](https://github.com/vladajankovic/Software-for-arm-movement-coordination-assessment-using-a-computer-mouse/blob/master/README.md#2-requirements-and-installation)
3. [User interface overview](https://github.com/vladajankovic/Software-for-arm-movement-coordination-assessment-using-a-computer-mouse/blob/master/README.md#3-user-interface-overview)
4. [Software features](https://github.com/vladajankovic/Software-for-arm-movement-coordination-assessment-using-a-computer-mouse/blob/master/README.md#4-software-features)
5. [Software testing examples](https://github.com/vladajankovic/Software-for-arm-movement-coordination-assessment-using-a-computer-mouse/blob/master/README.md#5-software-testing-examples)
***
### 1. Introduction
The arm movement coordiantion assessment software represents a version of the [***Modified Drawing Test***](https://www.researchgate.net/publication/270468778_The_modified_drawing_test_for_assessment_of_arm_movement_quality) (*mDT*) for personal computers. The purpose of the *mDT* is for examining the arm movement coordination of patients, who have survived a stroke and are rehabilitating their upper extermites (arms). The patient is required to draw a line along a given rectangular path, as fast and percise as possible, while supervised by therapists. The size of the path model is determined by the patients range of motion. The *mDT* score is determined by the speed, smoothness and percision error metrics. It is important to note that the *mDT* is not meant for training, only testing.  
 
The arm movement coordiantion assessment software is implemented for training and testing patients during rehabilitation. Its GUI is designed to be as simple as possible for the user/patient. The software was developed in Python, using mostly the pygame library for creating and implementing simple GUIs, user interactions, event processing...  
Here is the list of all Python libraries and modules used in developing the software:
+ [Pygame library](https://www.pygame.org/news)
+ [NumPy library](https://numpy.org/)
+ [OS module](https://docs.python.org/3/library/os.html)
+ [Datetime module](https://docs.python.org/3/library/datetime.html)

Training and testing is conducted by first selecting the appropriate option in the Main Menu and moving the cursor on the screen. The cursor on the screen is moved by moving the computer mouse and can be slowed down or sped up by pressing certain keys on the keyboard. The cursor sensitivity levels corresponds to different sizes of the path models for the *mDT*. A smaller sensitivity level leads to more mouse movement required to move the cursor on the screen a certain distance. That is equivalent to having a larger size model of the path that the patient traces. On the other hand, a larger sensitivity level leads to les mouse movement required to move the cursor, which is equivalent to having a smaller size path model. This is important because unlike the *mDT*, which adjusts the model size to the patients range of motion, the software has a fixed model size of the path, determined only by the size and resolution of the monitor screen.

The main feature of the software is the Testing Module, in which the user/patient can test their arm movement coordination. To complete the test, the user/patient must trace a line along the middle of the path on the screen and return to the starting position, indicated by a small red square. The test calculates how close the cursor is to the middle of the path. The drawing precision score is calculated continuously as a precentage in the range [0, 100] %. When the test is finished, the results are saved and a popup window indicates that the user has completed the test and can restart it or go back to the Main Menu. The test scoring system was inspired by the browser game [***Draw a Perfect Circle***](https://neal.fun/perfect-circle/) created by [Matt Round](https://mattround.com/).
  
To run the software on a computer, it is not required to have Python and all the dependencies (libraries and modules) installed localy. Executable files for Windows OS and Linux OS are provided using the [PyInstaller](https://pyinstaller.org/en/stable/) tool. The only downside is that executable files created using PyInstaller can be labled as viruses because ***the executables do not have a signed certificate***, which requires paying. Because of that, some antiviruses lable it as a ***FALSE POSITIVE***.

***
### 2. Requirements and installation
Hardware:
+ Computer mouse
+ Keyboard
  + Escape
  + Arrow UP
  + Arrow DOWN
  + Space
  + Enter (Return)
  
Software: Windows OS or Linux OS  
To install the software, simply download the appropriate archive for your OS, unpack it and run the executable file in the folder.
***
### 3. User interface overview
The software consists of 3 user interfaces:
+ Main Menu
+ Training Module
+ Draw Test Module
  
The following image represents the Main Menu GUI:
  
![Main Menu](https://github.com/vladajankovic/Software-for-arm-movement-coordination-assessment-using-a-computer-mouse/blob/master/GUI%20images/1.png)
  
The Main Menu consists of 3 buttons labled "Training", "Draw Test" and "Exit". Using the arrow keys UP and DOWN changes the select option of the buttons. Pressing the Enter key will select the current button and pressing the Escape key will exit the software. In the bottom left corner of the screen is the help info on what the keys do when they are pressed. Selecting the "Training" button moves the user to the Training Module, selecting the "Draw Test" button moves the user to the Testing Module and selecting the "Exit" button will exit the software.

The following image represents the Training Module GUI:

![Training Module](https://github.com/vladajankovic/Software-for-arm-movement-coordination-assessment-using-a-computer-mouse/blob/master/GUI%20images/2.png)

The Training Module is created for the user/patient to practice repetitive arm movement which is an effective way of arm rehabilitation based on muscle memory. This Module contains various horizontal, vertical, diagonal and radial lines that help the user/patient with arm movement in many different paths by following a line or moving in between two lines. In the top left part of the screen is the information panel which explains the action of pressing certain buttons. The user/patient can practice arm movement with different cursor sensitivity levels to find the optimal level to use in the Testing Module. The current sensitivity level is displayed in the information panel as a multiplier of the current computer mouse sensitivity. The image shows the value x0.25 which is 4 times slower than the computer mouse.

The following images represent the Draw Test Module GUIs:

![Draw Test Module](https://github.com/vladajankovic/Software-for-arm-movement-coordination-assessment-using-a-computer-mouse/blob/master/GUI%20images/3.png)

The above image represents the "preparation" state of the Draw Test Module. The popup window contains information on how to start the test and the user/patient can change the cursor sensitivity level that best suits him/her. By pressing the Space key or any mouse button, the test begins and the Module goes into the "testing" state.

![Draw Test Module](https://github.com/vladajankovic/Software-for-arm-movement-coordination-assessment-using-a-computer-mouse/blob/master/GUI%20images/4.png)

In the "testing" state, represented by the above image, the user/patient is tasked to draw a line by following the middle of the path, represented by a black square frame as percise as possible. A green square in the middle of the frame represents the optimal path and can help the user/patient in drawing by following it which results in a higher percision score. Failing to follow the optimal path results in lower percision score, and drawing over the . In the top right part of the screen is a stopwatch that measures the elapsed time sice starting the test. On the left side of the screen are the information panel, that tells the user/patient what key press results in what action, and the percision score panel, that shows the current accuracy or drawing percision. The user/patient starts from the red square and draws clockwise or counter clockwise until the cursor returns to the starting position. When the test is finished, the Module goes into the "end test" state.
  
![Draw Test Module](https://github.com/vladajankovic/Software-for-arm-movement-coordination-assessment-using-a-computer-mouse/blob/master/GUI%20images/5.png)

In the "end test" state, represented by the above image, the stopwatch is stopped, the final accuracy score is calculated, the results are saved localy and a popup window is shows that the user has completed the test.
***
### 4. Software features
The biggest feature of this software is the way it saves the test results. When the test is finished, the software makes a screenshot of the entire screen which it saves localy in the ***results*** folder. If the folder doesnt exist, the software will automatically create it after the screenshot. The software names the images of the test results as the date and time when the user/patient finished the test, which is shown in the image below.

![Save](https://github.com/vladajankovic/Software-for-arm-movement-coordination-assessment-using-a-computer-mouse/blob/master/GUI%20images/6.PNG)
***
### 5. Software testing examples
The functionalities of the software were tested by anonymous volunteers. Each volunteer was given 4 attempts to complete the test. The image below represents the test results of one volunteer, who simulated the results of a person who survived a stroke and is in rehabilitation.

![Results](https://github.com/vladajankovic/Software-for-arm-movement-coordination-assessment-using-a-computer-mouse/blob/master/GUI%20images/7.png)

The first attempt simulates the beginning of a patients rehabilitation where the patient finds it difficult to draw smooth lines and folow the optimal path, which results in a lower score. The second and third attempt simulate the later phases in the rehabilitation process when the patient tries to draw more percise after each attempt, which results in the line drawn staying inside the path at all times, greater smoothness of the drawn line and a higher accuracy score. The fourth attempt simulates the final stage of the parients rehabilitation process in which the patient is able to follow the optimal path but not perfectly. At this point the doctors and therapists can assume that most, if not all, of the patients arm muscle functionalities are restored.
