# Authors: Peter Shultz, Sam Freedman, Anna Hayman, Sagar Singichetti
# uniqnames: pshultz, samjfree, amhayman, singichs
# Date: December 1, 2014
# Purpose: Implement standard calculations that are integral to the study of statistics
# Description: Functions to calculate mean, variance, standard deviation, and median.

import sys
import math
import csv
import measures

"""
Requires: data is a list of numbers
Modifies: nothing
Effects: returns the average of the numbers in data
"""


def mean(data):
    # Code written by Peter Shultz

    # Returns the sum of the data divided by the float of the length of the list

    return (sum(data) / float(len(data)) )  #float is used to ensure no integer division occurs


"""
Requires: data is a list of numbers
Modifies: nothing
Effects: returns the variance of the numbers in data. an explanation of how to
	calculate variance is in the spec
"""


def variance(data):
    # Code written by Peter Shultz

    # Declaring and initializing some variables
    differenceOfEachPoint = 0
    differenceOfEachSquared = 0
    summationOfSquaredDifferences = 0


    #Iterates through each element
    for element in data:

        #Finds the difference of the average and each specific point in the data set
        differenceOfEachPoint = (element - mean(data))
        #print differenceOfEachPoint

        #Square each difference
        differenceOfEachSquared = math.pow(differenceOfEachPoint, 2)
        #print differenceOfEachSquared


        #Add the squared differences together

        summationOfSquaredDifferences = differenceOfEachSquared + summationOfSquaredDifferences

    return (summationOfSquaredDifferences / len(data))


"""
Requires: data is a list of numbers
Modifies: nothing
Effects: returns the standard deviation of the numbers in data
"""


def stdev(data):
    # Code written by Peter Shultz

    # From the spec: stdev is "calculated by taking the square root of the variance of a data set."
	return math.sqrt(variance(data))


'''
Requires: data is a list of numbers
Modifies: data
Effects: returns the median of the numbers in data. be careful that when you use
	this function, that the order of the objects in data will be modified.
	therefore, any lists that are passed to data must be able to be changed
'''


def median(data):
    # Code written by Peter Shultz

    # Initial response: the note in the RMEs regarding Effects seems a little strange.
    #I will attempt something nonetheless

    lowMiddleValue = 0
    highMiddleValue = 0
    middleValue = 0

    #Sort the elements in data
    data.sort()

    #Acquire the number of elements within the list
    numberOfElements = len(data)

    #If there are an even number of elements within the list
    if numberOfElements % 2 == 0:

        #Get the values of the two middle elements
        lowMiddleValue = data[numberOfElements / 2 - 1]
        highMiddleValue = data[numberOfElements / 2]

        #Return the average of these two middle elements
        return (lowMiddleValue + highMiddleValue) / float(2)

    #If there are an odd number of elements within the list
    else:

        #Return the middle element
        return data[numberOfElements / 2]


