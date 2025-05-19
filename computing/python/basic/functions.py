#!/usr/bin/env python3
"""
This file is part of the Knowledge Journal
See https://github.com/augustodamasceno/knowledge-journal/
(Previously in the adlabs project)
"""
__author__ = "Augusto Damasceno"
__version__ = "1.1"
__copyright__ = "Copyright (c) 2020-2025, Augusto Damasceno."
__license__ = "All rights reserved"

# Python Basic - Functions 

import math


pi = 3.14  # pi is a global variable


def hi():
    """
    A procedure that prints "Hi!"
    :return:
    """
    print('Hi!')


def dist_euclidean(x1, y1, x2, y2):
    """
    Function that calculates the euclidean distance in a dimension of two.
    :param x1: Coordinate x of the first point
    :param y1: Coordinate y of the first point
    :param x2: Coordinate x of the second point
    :param y2: Coordinate y of the second point
    :return: Euclidean distance of the points.
    """
    dist_x = math.pow(x1-x2, 2.0)
    dist_y = math.pow(y1-y2, 2.0)
    return math.sqrt(dist_x+dist_y)


def area_circle(radius):
    """
    Function that calculates the area of a circle.
    :param radius: Circle radius
    :return: Area of the circle
    """
    return 2*pi*math.pow(raio, 2.0)  # Read-only access to the pi global variable


dist_x = 47564168148
print(id(dist_x)) # Compare with id(dist_x) in local scope in dist_euclidean.
win = False
attempt = 1 # Attempt is a global variable.


def inc_attempt():
    global attempt # Write access to the attempt global variable
    attempt += 1


while not win:
    print('Attempt {}\n'.format(attempt))
    radius = input('\nEnter the circle radius: ')
    x = input('Enter the first point dimension 1: ')
    y = input('Enter the second point dimension 2: ')
    dist = dist_euclidean(float(x), float(y), 10.0, 10.0)
    if dist <= float(radius):
        print(  'The bullet hit the target in {} attempts.'.format(attempt) 
			  + '\n\tDistance from the circle radius: {:.4f}\n\n'.format(dist))
        win = True
    else:
        print('Try again!')
        inc_attempt()

fruits = ['orange', 'apple', 'grape']
quantity = 20


def foo(fruits, quantity):
	fruits[1] = 'lemon'
	quantity = 10
	print('Inside the function, fruits id = {}. The fruits:'.format(id(fruits)))
	print(fruits)
	print(  'Inside the function, quantity id' 
	 	  + '= {}. The quantity: {}'.format( id(quantity), quantity ))


print('Outside the function and before calling foo, fruits id = {}. The fruits:'.format(id(fruits)))
print(fruits)
print(  'Outside the function and before calling foo, quantity id' 
	  + '= {}. The quantity: {}'.format( id(quantity), quantity ))
print('------------------------')
foo(fruits, quantity)
print('------------------------')
print('Outside the function and after calling foo, fruits id = {}. The fruits:'.format(id(fruits)))
print(fruits)
print(  'Outside the function and after calling foo, quantity id' 
	  + '= {}. The quantity: {}'.format( id(quantity), quantity ))

