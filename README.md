
# First Steps with Python

This tutorial gets you started with the **Anaconda** Python programming environment.

## Background

There are (at least) four ways to use Python in Anaconda

* the **editor** in Spyder
* the **IPython** interactive console
* the **Anaconda Prompt** (a terminal)
* **Jupyter Notebooks** (not covered in this tutorial)

All four work in slightly different ways, which can be confusing. 
The purpose of this guide is to give you clear usage instructions.

### 1. How to execute a single Python command?

    IPython         : type the command + <ENTER>

    Editor          : type + select the command + <SHIFT + ENTER>

    Anaconda Prompt : python

### 2. How to run a Python script?

    IPython         : %run my_script.py

    Editor          : <F5>

    Anaconda Prompt : python script.py

### 3. How to display the contents of variable `x`?

    IPython         : x

    Editor          : print(x)

    Anaconda Prompt : -

### 4. In which directory is my code executed?

    IPython         : pwd

    Editor          : same location as your code (F5)
                      or the current path in

    Anaconda Prompt : pip install pillow

### 5. Changing directories

In IPython and the prompt, you can type:

* `ls` or `dir` show you files in the current directory. 
* `cd path` to change to the directory `path`
* `cd ..` to change one directory up

### 6. What else can I do?

    IPython         : view previous commands: %hist

    Editor          : save the program to a file

    Anaconda Prompt : install Python packages with:
                      pip install pillow

---- 

## Exercises

### 1. Install Anaconda

Get it from [www.anaconda.com/download/](https://www.anaconda.com/download/)

**if it does not work:** 

* Install Python 3.6 from [www.python.org](http://www.python.org)
* Install **Pillow** from the command line: `pip install pillow`

### 2. Run the example programs

* *easy:* `dice.py` 
* *medium:* `warhol.py`
* *hard:* `logo.py`

### 3. Modify a program

Change one of the programs to create your own image.

----

## License

The source code is (c) 2017 Dr. Kristian Rother
(see https://github.com/krother/python_showcase)

Published under the conditions of the MIT License
