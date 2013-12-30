# Name: ...
# Evergreen Login: ...
# Computer Science Foundations
# Programming as a Way of Life
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math                     # makes the math.sqrt function available


###
### Problem 1
###

print "Problem 1 solution follows:"

def compute_roots(a, b, c):
    root1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)  # computes first square root
    root2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)  # computes second square root
    return root1, root2

print compute_roots(1, -5.86, 8.5408)

###
### Problem 2
###

print "Problem 2 solution follows:"



###
### Problem 3
###

print "Problem 3 solution follows:"

# ... write your code and comments here (and remove this line)


###
### Collaboration
###

# ... List your collaborators and other sources of help here (websites, books, etc.),
# ... as a comment (on a line starting with "#").


###
### Reflection
###

# ... Write how long this assignment took you, including doing all the readings
# ... and tutorials linked to from the homework page. Did the readings, tutorials,
# ... and lecture contain everything you needed to complete this assignment?
