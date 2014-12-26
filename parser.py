import csv
import sys


def parseCSVFile(fileName):
    # Helpful variables
    returnList = []

    with open(fileName, 'rU') as readInFile:

        #Create dictionaries for each of five inputs

        GPADictionary = dict()
        SATDictionary = dict()
        tuitionDictionary = dict()
        aidDictionary = dict()
        familyIncomeDictionary = dict()

        #Other helpful variables
        counter = 1
        valueList = []

        for row in readInFile:
            row = row.strip()
            row = row.split(',')
            if counter >= 1 and counter <= 8:

                #Add each to GPADictionary
                key = row[0]
                valueList = [float(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6]), float(row[7]), float(row[8])]
                GPADictionary[key] = valueList
                counter += 1


            elif counter >= 9 and counter <= 16:
                key = row[0]
                valueList = [float(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6]), float(row[7]), float(row[8])]
                SATDictionary[key] = valueList
                counter += 1


            elif counter >= 17 and counter <= 24:

                if row[0] == "VOID":
                    '''Do nothing'''
                    counter += 1

                else:
                    key = row[0]
                    valueList = [float(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6]), float(row[7]), float(row[8])]
                    aidDictionary[key] = valueList
                    counter += 1

            elif counter >= 25 and counter <= 32:

                if row[0] == "VOID":
                    '''Do nothing'''
                    counter += 1

                else:
                    key = row[0]
                    valueList = [float(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6]), float(row[7]), float(row[8])]
                    tuitionDictionary[key] = valueList
                    counter += 1

            elif counter >= 33 and counter <= 40:
                key = row[0]
                valueList = [float(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6]), float(row[7]), float(row[8])]
                familyIncomeDictionary[key] = valueList
                counter += 1

    returnList = [GPADictionary, SATDictionary, aidDictionary, tuitionDictionary, familyIncomeDictionary]
    return returnList
