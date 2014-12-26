# Authors: Anna Hayman, Peter Shultz, Sam Freedman, Sagar Singichetti
# uniqnames: amhayman, pshultz, samjfree, singichs
# Date: December 13, 2014
# Purpose: 
# Description:

import sys
import csv

'''
The data structure for parseCSVFile will go as follows:

parseCSVFile will return a list that holds multiple dictionaries. Each dictionary will represent output and will have either 6, 7, or
8 key-value pairs. The key will be the ranges of the various input data: GPA, SAT score, tuition cost, total aid, family income.
The value pairs will be a list of eight values, each value representing percentages.
'''


def parseCSVFile(fileName):
	# Helpful variables
    returnList = []

    with open(fileName, 'rb') as readInFile:

		# Create dictionary for each of five inputs

		GPADictionary = dict()
		SATDictionary = dict()
		tuitionDictionary = dict()
		aidDictionary = dict()
		familyIncomeDictionary = dict()


		# Other helpful variables
		counter = 1
		valueList = []

		for row in readInFile:
			row = row.split(',')

			if counter >= 1 and counter <= 8:
				# Add each to GPADictionary, with the first value in the row being the key, the rest becoming a list, then a value
				key = row[0].strip()
				valueList = [row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]]
				GPADictionary[key] = valueList

			if counter >= 9 and counter <= 16:
				# Add each to SATDictionary
				key = row[0].strip()
				valueList = [row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]]
				SATDictionary[key] = valueList

			if counter >= 17 and counter <= 24:
				# Add each to aidDictionary
				if row[0] == 'VOID':
				    #Do nothing
				else:
					key = row[0].strip()
					valueList = [row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]]
					aidDictionary[key] = valueList

			if counter >= 25 and counter <= 32:
				# Add each to tuitionDictionary
				if row[0] == 'VOID':
				#Do nothing
				else:
					key = row[0].strip()
					valueList = [row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]]
					tuitionDictionary[key] = valueList

			if counter >= 33 and counter <= 40:
				# Add each to familyIncomeDictionary
				key = row[0].strip()
				valueList = [row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]]
				familyIncomeDictionary[key] = valueList

			# Increment the counter
			counter += 1
	returnList = [GPADictionary, SATDictionary, aidDictionary, tuitionDictionary, familyIncomeDictionary]

