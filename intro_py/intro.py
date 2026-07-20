
# what is python 
""" 
Python is a high-level, interpreted, general-purpose programming language designed for readability and simplicity, allowing developers to write clear and efficient code for a wide range of applications such as web development, data science, automation, and artificial intelligence.
"""

# Why Python is Popular
"""
Python is widely used because it reduces complexity and speeds up development.

Easy to learn: Syntax is close to English
Less code: You can do more with fewer lines
Cross-platform: Runs on Windows, Linux, Mac
Large community: Millions of developers + support
Versatile: Works in web, ML, automation, etc.
"""


# variable in python 
"""
A variable in Python is a named reference to a value stored in memory. It is used to store, access, and manipulate data during program execution.
"""

# Garbage Collection in Python
"""
Garbage Collection in Python is an automatic memory management process that identifies and removes objects from memory when they are no longer referenced by any variable, thereby freeing up memory for future use.

Python mainly uses two mechanisms:
. Reference Counting (Primary Method)

Every object in Python has a reference count (number of variables pointing to it).

Example:
x = 10      # ref count of 10 = 1
y = x       # ref count of 10 = 2

del x       # ref count of 10 = 1
del y       # ref count of 10 = 0 → eligible for deletion

Garbage Collector (Secondary Method)

Reference counting cannot handle circular references, so Python uses a Garbage Collector.

Circular Reference Example:
a = []
b = []

a.append(b)
b.append(a)
a refers to b
b refers to a
Even if you delete a and b, they still reference each other

➡️ Garbage Collector detects this and removes them

"""



