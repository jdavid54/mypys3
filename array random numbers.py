'''
python
How to Create Multidimensional Arrays in Python
Posted on: February 25, 2021 by Ariessa Norramli


In this article, you will learn how to create multidimensional arrays in Python.

In this example, you will be creating 1-dimensional, 2-dimensional, and 3-dimensional arrays.

Create Multidimensional Arrays in Python
In order to create multidimensional arrays, you can use the numpy.random.randn() method.
'''
# Import numpy module
import numpy as np 
   
# Create 1D array named 'a' with 4 random values 
a = np.random.randn(4)

# Create 2D Array named 'b' with 4 random values
b = np.random.randn(2, 2) 

# Create 3D Array named 'c' with 8 random values     
c = np.random.randn(2, 2 ,2) 

# Display array named 'a'
print("1D Array named 'a' with 4 random values : \n", a); 
# 1D Array named 'a' with 4 random values : 
# [ 0.7610706  -0.17719692 -0.82679301 -0.77078355]

# Display array named 'b'
print("2D Array named 'b' with 4 random values : \n", b); 
# 2D Array named 'b' with 4 random values : 
# [[ 0.02434673  0.91250619]
#  [ 0.83150441 -0.36243897]]

# Display array named 'c'
print("3D Array named 'c' with 8 random values : \n", c); 
# 3D Array named 'c' with 4 random values : 
# [[[-1.08693709 -0.88007873]
#   [-0.43909493 -0.31530899]]
#
#  [[-2.12054687 -0.06806256]
#   [-0.99278326 -1.83572125]]]