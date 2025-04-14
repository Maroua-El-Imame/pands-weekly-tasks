# plottask.py
# this program when run, displays 
# a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2. 
# a plot of the function  h(x)=x**3 in the range 0 to 10,

# Author : Maroua EL imame


# import modules
import numpy as np
import matplotlib.pyplot as plt

# generate random numbers corresponding to 1000 values with a mean of 5 and standard deviation of 2 and assigne a value 'randomNumbers'
randomNumbers = np.random.normal(loc=5, scale=2, size=1000)

# random.normal() method to get a normal data distribution.
# loc   (Mean) where the peak of the bell exists.
# scale (Standard Deviation) how flat the graph distribution should
# size - The shape of the returned array.

# I used the resource below to learn more about the normal distributio
# url: https://www.w3schools.com/python/numpy/numpy_random_normal.asp

# I was able to read documentation and get an understanding of the diferent parameters of plots and hitogram method through the links below. 
# https://matplotlib.org/stable/tutorials/pyplot.html
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html


# the following code will generate a histogram with specified parameters.
# x: The data to be plotted.
# bins=50: The number of bins.
# density=True: Normalize the histogram.
# facecolor='g': Set the color of the bars to green.
# alpha=0.75: Set the transparency of the bars.


# values  to be plotted 
randomNumbers

# create a histogram of random numbers previously generated
#n, bins, patches = plt.hist(randomNumbers, 45, density=True, facecolor='purple', alpha=0.45)

# method used to display Multiple Plots
# https://www.w3schools.com/Python/matplotlib_subplot.asp

# 1st plot 
plt.subplot(1, 2, 1)
plt.hist(randomNumbers, 45,density= True,facecolor='tab:brown', edgecolor ='k', alpha=0.8) 
# I added a grid for easy lecture of corresponding point
plt.grid(True, alpha=0.5)

# values to be plotted
x = np.arange(0,10,1)
y = x**3

# create a plot 
plt.subplot(1, 2, 2)
plt.plot(x,y, c='tab:brown', alpha=0.8) 
# I added a grid for easy lecture of corresponding point
plt.grid(True, alpha=0.5)


# method used to display Multiple Plots
# https://www.w3schools.com/Python/matplotlib_subplot.asp

# show
plt.show()





