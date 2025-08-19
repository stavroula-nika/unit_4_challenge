# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can find my tasks among all my notes
I want to check if a line from my notes includes the string `#TODO`.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python


    """


    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a valid input
Returns a string
"""
find_task(notes)=> str

"""
Given a valid '#todo' in notes
Returns a string
"""
find_task(notes)=> 'todo found!'

"""
Given a valid '#todo' not in notes
Returns a string
"""
find_task(notes)=> 'todo not found!'

"""
"""
Given an empty string 
It throws an error
"""
to_do('') => throws an error

"""
Given a None value
It throws an error
"""
to_do(None) => throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE


"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""


Ensure all test function names are unique, otherwise pytest will ignore them!
