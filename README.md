# CPE 1040 Stack Class in Python

Programming assignment for CPE 1040 on implementing a `Stack` class in Python

## Resources
1. Working with Python [classes](http://introtopython.org/classes.html)
2. [Stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type) abstract data type

## Requirements
1. (30 points) You have the skeleton of the Stack class in [stack.py](stack.py). Implement a generic stack using a Python list and completed the three mandatory methods:
   - constructor `__init__`
   - `push`
   - `pop`
2. (10 points) By completing the provided `test_` methods, test the correctness of the generic stack from [main.py](main.py):
   - using integers (e.g. `5`)
   - using floating-point numbers (e.g. `3.14`)
   - using strings (e.g. `alchemy`)
3. (10 points) By completing the provided `test_all` method, test that you can push arbitrary data types and your Stack would take them. _Remember that Python's list object takes all comers._
4. (50 points) Restrict the `Stack` class to accept data of only a single type:
   - add a single argument to the constructor `__init__` (after the mandatory `self`), called `sample`
   - using code similar to the [exception.py](exception.py) example, add code to `push` to check if the value being pushed has the same type as `sample` and faise a `ValueError` with the appropriate message, if not
   - re-run your `test_all` and verify it correctly rejects pushes of the wrong type
5. (BONUS) Correctly implement a subclass `IntStack` which only works for integer pushes:
   - subclass from `Stack`
   - the `__init__` constructor should take no arguments (except the default `self`)
   - `push` should reject all values except integers
   - in [main.py](main.py), write a test method `safe_test_int`, which tries to push values of various types like `test_all`, but catches `ValueError` exceptions in a `try...except` block, so the program runs to completion instead of being terminated on a rejected push 
   
## Submission
1. Fork the [assignment repository](https://github.com/ivogeorg/cpe1040-stack-class.git).
2. Clone+open in PyCharm.
3. Implement and test in PyCharm, committing your changes often.
4. When done, push to your remote on Github.
5. Submit the Google Classroom [assignment](https://classroom.google.com/u/0/c/Mjc4NzMyMzI1MTda/a/MzUxNTQyODE0Mzha/details), including a comment with the URL of your repository on Github.
