# Authors: Sagar Singichetti, Sam Freedman, Anna Hayman, Peter Shultz
# uniqnames: singichs, samjfree, amhayman, pshultz
# Date: December 5, 2014
# Purpose: Create a sample covariance and a correlation matrix
# Description: There exist two functions within diagnostics.py: singleSampleCovariance(), which returns a sample covariance, and correlationMatrix(), which returns a correlation matrix

import sys
import math
import eecsCsv
import measures

"""
Requires: xVals is a list of all of the values for the first random variable
	yVals is a list of all of the values for the second random variable
	meanX is the average of all of the values in xVals
	meanY is the average of all of the values in yVals
Modifies: nothing
Effects: returns the sample covariance between xVals and yVals
"""


def singleCovariance(xVals, yVals, meanX, meanY):
	N = len(xVals)
	total = 0
	for index in range(N):
		Scov = (xVals[index] - meanX) * (yVals[index] - meanY)
		total += Scov
	Scov = total * (1.0 / (N))
	return Scov


"""
Requires: dictionary is a dictionary built by parseCSVFile
		inclusionList is the same length as all of the entries in dictionary
		for each entry in inclusionList, the value is 1 if that entry is to be
			included in the correlation matrix, and 0 if it is not
Modifies: nothing
Effects: returns a list of lists, holding the correlation matrix for the
	selected entries
"""


def correlationMatrix(dictionary, inclusionList):

	sizeInclusion = len(inclusionList)
	collectionRV = []
	corrMatrix = []
	tempMatrix = []

	for i in range(0, sizeInclusion):

		if (inclusionList[i] == 1):

			collectionRV.append(eecsCsv.retrieveEntireAttribute(dictionary, i))

	for j in range(len(collectionRV)):

		for k in range((len(collectionRV))):

			temp = singleCovariance(collectionRV[j], collectionRV[k], measures.mean(collectionRV[j]), measures.mean(collectionRV[k]))

			tempMatrix.append(temp / (measures.stdev(collectionRV[j]) * measures.stdev(collectionRV[k])))

	corrMatrix.append(tempMatrix)

	return corrMatrix
