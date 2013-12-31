# -*- coding: cp1252 -*-
# Name: David Bryant
# Evergreen Login: dbryant17
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

print ''

###
### Problem 2
###

print "Problem 2 solution follows:"

import hw1_test

print hw1_test.a
print hw1_test.b
print hw1_test.c
print hw1_test.d
print hw1_test.e
print hw1_test.f

print ''

###
### Problem 3
###

print "Problem 3 solution follows:"

print ((hw1_test.a and hw1_test.b) or (not hw1_test.c) and not (hw1_test.d or hw1_test.e or hw1_test.f))

print ''

###
### Collaboration
###
### I got help from Barbara Bryant and David Yee on figuring out what
### homework to do and how to use Github
###

###     6. Modules — Python v2.7.6 documentation - http://docs.python.org/2/tutorial/modules.html

###
### Reflection
###

###     The assignment took a little while to get started because I had to make
###     I knew what I was doing, which I did not at first (mostly in reference
###     to the importing) but when I got it I finished pretty quickly. The
###     website helped me with most everything except the importing, for which
###     I had to look at the python documentation. It was a simple issue, but
###     I didn't realize that python would just look into the current directory.
