# Authors: Sam Freedman, Peter Shultz, Anna Hayman, Sagar Singichetti
# uniqnames: samjfree, pshultz, amhayman, singichs
# Date: 12/1/14
# Purpose: parse a CSV file, retrieve a certain value from the dictionary, or retrieve an attribute from every key-value
# Description: eecsCsv.py has three functions: parsCSVFile() will make a dictionary out of a CSV file; retrieveValue() will retrieve a particular value given a dictionary, key, and particular entry; retrieveEntireAttribute() will return a list of every attribute across a dictionary

import sys
import csv


def parseCSVFile(fileName):
	"""
    This function reads in a CSV file and stores the values therein in a
    dictionary. The key in the key-value pair is one of the entries in the
    table, and the value is a list of the entries (which are themselves lists)
    associated with that value in the table.

    For the purposes of the bare-bones, the key is the name of the storm, and
    the values stored in the list are as follows:
    name, date, time, system_status, lat, lon, wind, pressure
    The types of these values for the purposes of grading of core functionality
    are:
    str, str, str, str, float, float, int, int

    When you are writing your own function to read in your specific file, you
    can set the types to whatever you see fit.

    For the purposes of your extension, you will need to modify this code so
    that it works for your data set. You can decide what the key and values are,
    but make sure you choose your key wisely.

    In any event, this function will return the dictionary that is built by
    parsing the CSV file.

    Requires: fileName contains the name of the CSV file
    Modifies: nothing
    Effects: See the above.
    """

	# We need an array holding the values of each row after a row that has "A"


	returnDictionary = dict()
	listOfLists = []
	counter = 1
	key = ''

	with open(fileName, 'rb') as hurdatFile:
		for row in hurdatFile:
			row = row.split(',')
			if (row[0][0] == 'A'):
				returnDictionary[key] = listOfLists
				key = row[1].strip()
				listOfLists = []
			elif (row[0][0] == '2'):
				row = [x.strip(' ') for x in row] #Get rid of trailing and leading whitespaces
				row.pop(2)
				row.pop()
				row.insert(0, key)
				row[4] = float(row[4])
				row[5] = float(row[5])
				row[6] = int(row[6])
				row[7] = int(row[7])
				listOfLists.append(row)

	returnDictionary[key] = listOfLists
	returnDictionary.pop('', None)

	#    str, str, str, str, float, float, int, int


	return returnDictionary





def retrieveValue(dictionary, key, entry):
	"""
    This function retrieves an entry from the list of entries in the dictionary
    for a given key and position in the list for the key.

    Requires: dictionary is the dictionary built in parseCSVFile, key is the
    key from which we want to fetch values, and entry is the index of the
    entry we wish to fetch

    Modifies: nothing
    Effects: retrieves a single entry from the list of entries in the dictionary
        such that entry holds the position in the list of entries, and that key
        is the key from which we wish to fetch it
    """

	return dictionary[key][entry]




"""
Requires: dictionary holds a dictionary created by parseCSVFile
	columnNo holds the index of the attribute we wish to create a list from
Modifies: nothing
Effects: returns a list of the values in the column specified by columnNo
"""


def retrieveEntireAttribute(dictionary, columnNo):


	returnList = []

	valuesList = dictionary.values()

	for value in valuesList:
		for eachList in value:
			returnList.append(eachList[columnNo])

	return returnList

