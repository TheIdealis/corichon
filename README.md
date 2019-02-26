cornichon - Save and load classes in python
------------

# Introduction

When performing numerical calculations in Python, it often comes in handy to structure the data into classes and - of course - save them for later use. Although `pickle` might be an option, there is a huge downside to it. As soon as the data is saved, you can no longer add further functionally to the class, e.g., functions for visualization.
`cornichon` is trying to solve that problem by pickling only the data of every class and restoring the structure of the project recursively during the loading process.

# Installation

Just execute
```
pip install .
```
No other packages are required.

# Basic usage

Just add the `save_all` and `load_all` - function to every class and subclass.
```python
from gherkin import save_all, load_all

class foo:
    # ...
    save_all = save_all
    load_all = load_all

class bar:
    def __init(self):
        self.foo = foo()
    # ...
    save_all = save_all
    load_all = load_all

B = bar()
B.save_all('filename')
B.load_all('filename')
```
