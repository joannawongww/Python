# Python

## Exercise 1.1
### Tasks
- Install Python on Windows
- Create and manage virtual environments
- Use pip to install and manage packages

Step 1: Install Python 3.8.7 on system
- https://www.python.org/downloads/release/python-387/ 

Step 2: Set up a new virtual environment named 'cf-python-base'
- `mkvirtualenv cf-python-base`

Step 3: Install Visual Studio Code
- Create a script named 'add.py' that adds up 2 numbers that the user enters
- `a = int(input('Enter first number'))`
- `b = int(input('Enter second number'))`
- `c = a + b`
- To print value of c to screen: `print(c)`

Step 4: Set up IPython in virtual environment "cf-python-base"
- ` pip install ipython `
- Verify installation by launching iPython shell with `ipython`

Step 5a: Export requirement file
- `workon cf-python-base`
- `pip freeze > requirements.txt`

Step 5b: Create new environment called "cf-python-copy" & install packages from the requirements.txt file generated from Step 5a.
- `mkvirtualenv cf-python-copy`
- `pip install -r requirements.txt`

