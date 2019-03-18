# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 11:48:26 2019

@author: ANONYME
"""
# importing the numpy librarie 
import numpy as np
 
array_2d = np.array(([3,5,4],[2,8,6],[-6,7,9],[0,1,-6]))

array_2d

array_2d[:1,:2]

array_2d[:3,:3]
#create an array from 1 to 9 
arr = np.arange(1,10)

arr
#we create an boolean array
bool_array = arr >5

bool_array

arr[bool_array]
#here we use reshape() methode to convert a simple array to 2D array 
arr_2d = np.arange(50).reshape(10,5)

arr_2d
#this is an indexing
arr_2d[3:5,1:3]

