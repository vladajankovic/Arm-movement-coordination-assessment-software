# Software for arm movement coordination assessment using a computer mouse
This software was developed as a result of my Bachelor Thesis under the mentorship of [Assoc. Prof. Nadica Miljković](https://www.etf.bg.ac.rs/en/faculty/staff/nadica-miljkovic-4323) from the [University of Belgrade - School of Electrical Engineering](https://www.etf.bg.ac.rs/en) defended on September 28, 2023.

### Table of Contents
1. [Introduction](https://github.com/vladajankovic/Software-for-arm-movement-coordination-assessment-using-a-computer-mouse/blob/master/README.md#1-introduction)
2. [Requirements and Installation](https://github.com/vladajankovic/Software-for-arm-movement-coordination-assessment-using-a-computer-mouse/blob/master/README.md#2-requirements-and-installation)
3. [User Interface Overview](https://github.com/vladajankovic/Software-for-arm-movement-coordination-assessment-using-a-computer-mouse/blob/master/README.md#3-user-interface-overview)
4. [Software Features](https://github.com/vladajankovic/Software-for-arm-movement-coordination-assessment-using-a-computer-mouse/blob/master/README.md#4-software-features)
5. [Software Testing Examples](https://github.com/vladajankovic/Software-for-arm-movement-coordination-assessment-using-a-computer-mouse/blob/master/README.md#5-software-testing-examples)
6. [Citing Instruction](https://github.com/vladajankovic/Software-for-arm-movement-coordination-assessment-using-a-computer-mouse/blob/master/README.md#6-citing-instruction)
***
### 1. Introduction
The arm movement coordiantion assessment software represents a version of the Modified Drawing Test (mDT) inspired from [1] and adopted for personal computer. The purpose of mDT is assessment of arm movement coordination of persons who have survived a stroke and are undergoing rehabilitation of upper extremities. The ideal scenario envisions that subject has an assignment to drive a line along a given rectangular path, as fast as and as percise as possible, while supervised by therapists. The size of the path model can be changed and adopted by the subjects' range of motion. The mDT score incorporates speed, smoothness, and percision error metrics of the drawing task. It is important to note that the mDT is not meant for training, only testing. However, future software versions or upgrades can incorporate training sessions as well.
 
GUI of the proposed software metod is designed to be as simple as possible for the users. The software was developed in [Python](https://www.python.org/) v3.8 programming language (Python Software Foundation, Wilmington, DE, USA), with the following list of Python libraries and modules:
+ [Pygame library](https://www.pygame.org/news)
+ [NumPy library](https://numpy.org/)
+ [OS module](https://docs.python.org/3/library/os.html)
+ [Datetime module](https://docs.python.org/3/library/datetime.html)

The program starts with the selection of the appropriate option in the Main Menu by moving the cursor on the screen with the computer mouse. The movements of the cursor on the screen can be slowed down or sped up by pressing certain keys on the keyboard. The cursor sensitivity levels correspond to different sizes of the path models for the mDT. Sensitivity level can be decreased. This way, the software enables a larger size model of the path that corresponds to the user traces. On the other hand, increased sensitivity level leads to lesser range movement to move the cursor, which is equivalent to having a smaller size path model. This is important, because unlike the mDT, which adjusts the model size to the user's range of motion, the software has a fixed model size of the path, determined only by the size and resolution of the monitor screen.

The main feature of the software is the Testing Module, in which users can test their arm movement coordination. To complete the test, the user should trace a line along the middle of the path on the screen and return to the starting position, indicated by a small red square. Afterwards, the software calculates how close the cursor is to the middle of the path (ideal path for drawing a perfect rectangle). The drawing precision score is calculated continuously as a precentage in the range [0, 100]%. When the test is finished, the results are saved and a popup window indicates that the user has completed the test and can restart it or go back to the Main Menu. The test scoring system was inspired by the browser game [Draw a Perfect Circle](https://neal.fun/perfect-circle/) created by [Matt Round](https://mattround.com/).
  
To run the software on a computer, it is not required to have Python and all the dependencies (libraries and modules) installed localy. Executable files for Windows OS and Linux OS are provided using the [PyInstaller](https://pyinstaller.org/en/stable/) tool. The only downside is that executable files created using PyInstaller can be labled as viruses because ***the executables do not have a signed certificate***. Because of that, some antiviruses lable it as a ***FALSE POSITIVE***.

DISCLAIMER: This software repository is provided without any guarantee and it is not intended for medical purposes.

This repository contains:
+ [GUI images](https://github.com/vladajankovic/Arm-movement-coordination-assessment-software/tree/master/GUI%20images) used for the [README](https://github.com/vladajankovic/Arm-movement-coordination-assessment-software/blob/master/README.md) document
+ [python](https://github.com/vladajankovic/Arm-movement-coordination-assessment-software/tree/master/python) folder containing source code
+ GNU GPL (General Public License) Version 3+ [license](https://github.com/vladajankovic/Arm-movement-coordination-assessment-software/blob/master/LICENSE)
+ [README](https://github.com/vladajankovic/Arm-movement-coordination-assessment-software/blob/master/README.md)
+ [download](https://github.com/vladajankovic/Arm-movement-coordination-assessment-software/blob/master/download.md) folder with istallation files for Linux OS and Windows OS

Reference:

[1] Kostić, M. D., & Popović, M. (2013). The modified drawing test for assessment of arm movement quality. Journal of Automatic Control, 21(1), 49-53. [http://dx.doi.org/10.2298/JAC1301049K](http://dx.doi.org/10.2298/JAC1301049K)

***
### 2. Requirements and Installation
Hardware:
+ Computer mouse
+ Keyboard
  + Escape
  + Arrow UP
  + Arrow DOWN
  + Space
  + Enter (Return)
  
Software:
+ Windows OS or Linux OS
  
To run the software **as an executable** follow these steps:
+ Download the appropriate archive based on your OS from the [download.md](https://github.com/vladajankovic/Software-for-arm-movement-coordination-assessment-using-a-computer-mouse/blob/master/download.md) file
+ Extract the archive localy (*e.g.*, Desktop)
+ Run the executable file **main** from the folder.

***
### 3. User Interface Overview
The software consists of three user interfaces:
+ Main Menu
+ Training Module (where users should get familiar with the environment)
+ Draw Test Module
  
The following image represents the Main Menu GUI:
  
![Main Menu](https://github.com/vladajankovic/Software-for-arm-movement-coordination-assessment-using-a-computer-mouse/blob/master/GUI%20images/1.png)
  
The Main Menu consists of three buttons labled "Training", "Draw Test" and "Exit". Using the arrow keys UP and DOWN, user can activate selection of the buttons. Pressing the Enter key will select the current button and pressing the Escape key will exit the software. In the bottom left corner of the screen is the help info on what the keys do when they are pressed. The "Training" button opens the Training Module in which users should familiarize with the software, by selecting the "Draw Test" button the Testing Module opnes, and the "Exit" button will exit the software.

The following image represents the Training Module GUI:

![Training Module](https://github.com/vladajankovic/Software-for-arm-movement-coordination-assessment-using-a-computer-mouse/blob/master/GUI%20images/2.png)

The Training Module is created with the aim to enable user to familiarize with the software environment and the mouse coursor velocity. This module contains various horizontal, vertical, diagonal, and radial lines that enable subject to follow a line or navigate between two lines. In the top left part of the screen is the information panel which explains the action of pressing certain buttons. The user can practice movements with different cursor sensitivity levels to find the optimal level for the Testing Module. The current sensitivity level is displayed in the information panel as a multiplier of the current computer mouse sensitivity. The image shows the value x0.25 which is four times slower than the computer mouse:

![Draw Test Module](https://github.com/vladajankovic/Software-for-arm-movement-coordination-assessment-using-a-computer-mouse/blob/master/GUI%20images/3.png)

The above image represents the "preparation" state of the Draw Test Module. The popup window contains information on how to start the test and the user can change the cursor sensitivity level that best suits themselves. By pressing the Space key or any mouse button, the test begins and the Module goes into the "testing" state:

![Draw Test Module](https://github.com/vladajankovic/Software-for-arm-movement-coordination-assessment-using-a-computer-mouse/blob/master/GUI%20images/4.png)

In the "testing" state, represented by the above image, the user should draw a line by following the middle of the path, represented by a black square frame as percise as possible. A green square in the middle of the frame represents the optimal path and can guide the user during a drawing task to reach high percision score. Failing to follow the optimal path results in lower percision score, and drawing over the . In the top right part of the screen is a stopwatch that measures the elapsed time from the test onset. On the left side of the screen are the information panel that instructs the user on key press actions and the percision score panel that displays the current accuracy or the drawing percision. The user should starts drawing from the red square in a clockwise or counter clockwise direction until the cursor returns to the starting position. When the test is finished, the Module goes into the "end test" state.
  
![Draw Test Module](https://github.com/vladajankovic/Software-for-arm-movement-coordination-assessment-using-a-computer-mouse/blob/master/GUI%20images/5.png)

In the "end test" state, represented in the above image, the stopwatch is stopped, the final accuracy score is calculated, the results are saved localy, and a popup window informs user that the test is completed.
***
### 4. Software Features
The most important feature of this software is the way it saves the test results. When the test is finished, the software makes a screenshot of the entire screen which it saves localy in the ***results*** folder. If the folder does not exist, the software will automatically create it after the screenshot. The resulting image name is created as the date and time when the user finished the test, which is shown in the image below:

![Save](https://github.com/vladajankovic/Software-for-arm-movement-coordination-assessment-using-a-computer-mouse/blob/master/GUI%20images/6.PNG)
***
### 5. Software Testing Examples
The functionalities of the software were tested by anonymous volunteer with four attempts to complete the test. The volunteer signed Informed Consent in accordance with the Code of Ethics at the University of Belgrade and in accordance with the Helsinki Declaration. The image below represents the test results of one volunteer, who simulated the results of a person that cannot perform full range of arm movements:

![Results](https://github.com/vladajankovic/Software-for-arm-movement-coordination-assessment-using-a-computer-mouse/blob/master/GUI%20images/7.png)

The first attempt simulates the beginning of a patients rehabilitation where the patient finds it difficult to draw smooth lines and folow the optimal path, which results in a decreased score. The second and the third attempts simulate the later phases in the rehabilitation process when the patient tries to draw more percise squares, which results in the drawn line inside the path at all times, greater smoothness of the drawn line, and in increased accuracy score. The fourth attempt simulates the final stage of the rehabilitation process in which the patient is able to follow the optimal path but not perfectly.

It should be emphasized that this software is tested in only one healthy volunteer, so its intended purpose for assessment of arm movements in stroke patients is yet to be tested and examined.

### 6. Citing Instruction
If you find this software useful, please cite my Bachelor thesis and this repository as:
+ Janković, V. (2023). Software for assessment of arm movement coordination using a computer mouse. *Bachelor Thesis, University of Belgrade - School of Electrical Engineering*, mentor: Dr. Nadica Miljković.


CONTACT: Vladimir Janković ([http://linkedin.com/in/vladimir-jankovic-22a843197/](http://linkedin.com/in/vladimir-jankovic-22a843197/))
