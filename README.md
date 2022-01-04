# Sonderleistung - Visualisierung des BranchAndBoundVerfahrens

This tool is an add-on for my stipendium from the Nassau Central Studies Fund. I developed it in the course of the Operations Research lecture. 
The tool uses the tkinter as a gui building tool. The logic is implemented in python. Packaged with pyinstaller.

## Installation (Windows 10)

1. git clone https://github.com/SamuelBorn/ProcessNodeNetwork.git
2. run "Main.exe" 


## Usage

The GUI is split into 3 parts.

### 1:

Enter the key data of your problem. This includes:
* Number of variables
* Number of constraints
* Should integer points be specified later?
* Which selection rule should be used

### 2:

Input of the constraints. Here we enter the numbers of the problem. There is a text field for each variable in each constraint.
In addition, we can choose between `<=, =, =>`.
It is also possible to specify a maximization function.

### 3:

Here the results are specified. Unfortunately, a new window must open for this.
If the problem is two-dimensional, images of the visualizations are also inserted.



