# Visualization of Branch And Bound

This tool visualizes the Branch And Bound algorithm for solving integer optimization problems.

It is an add-on for my stipendium from the Nassau Central Studies Fund. I developed it in the course of the Operations Research lecture. 
The tool uses the tkinter as a gui building tool. The logic is implemented in python. Packaged with pyinstaller.

## Installation (Windows 10)

1. Download/clone this repository 
2. run "Main.exe" 

*Due to the packaging, all imports must be loaded before the program starts. This causes the program to start very slowly.
Alternatively you can run* `python Main.py` *. This is much faster, but requires a installation of python on the computer*. The .exe works without python.


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
It is also possible to specify a `max, min` function.

### 3:

Here the results are specified. 
If the problem is two-dimensional, images of the visualizations are also inserted.

Unfortunately, a new window must open for this.


## Example of a solving step

![image](https://github.com/user-attachments/assets/ea64bb7a-dfba-434d-89b5-799c29944798)


