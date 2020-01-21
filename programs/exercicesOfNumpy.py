#we import the numpy librarie
import numpy as np

#Question 1
#Create an array of 20 zero 
np.zeros(20)

#Question 2
#Create an array of 15 ones 
np.ones(15)

#Question 3
#Create an array of 15 of any number of your choice 
np.ones(15)*3

#Question 4
#Create an array of integer from any number to any number of your choice 
np.arange(15,85)

#Question 5
#Create an array of all the even number between two number
np.arange(10,50,2)

#Question 6
#Create a 4 x 4 matrix with values ranging from 0 to 15 
np.arange(16).reshape(4,4)

#Question 7
#Create 4 x 4 idendity matrix 
np.eye(4)

#Question 8
#Generate a random number between 0 and 1 
np.random.rand(1)

#Question 9
#Generate an array of 15 random number
np.random.randn(15)

#Question 10
#Create an array of 10 linearly spaced point between 0 and 3 
np.linspace(0,3,10)

#Question 11
#Create a 5 x 5 matrix from 1 to 25
mat = np.arange(1,26).reshape(5,5)
mat

#Question 12
#Give the number of 20 
mat[3,4]

#Question 13
#Give the Column number 3
mat[:,2]

#Question 14
#Give the line number 2
mat[2,:]

#Question 15
#Get the sum of all the matrix values
mat.sum()

#Question 16
#Get the standar deviation of the values in the matrix
mat.std()

#Question 17
#Get the sum of all the columns in the matrix
mat.sum(axis=0)

#Question 18
#Get the sum of all the lines in the matrix 
mat.sum(axis=1)
































