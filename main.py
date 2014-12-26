#!/usr/bin/python
# coding=utf-8

# Authors: Anna Hayman, Peter Shultz, Sam Freedman, Sagar Singichetti
# uniqnames: amhayman, pshultz, samjfree, singichs
# Date: December 1, 2014
# Purpose: (Leave that for later)
# Description: (Leave that for later)

import sys
import math
import Tkinter
import weightedAverage
import returnAverage
import parser


"""
Use this function for your testing for bare-bones, and then use it as the driver
for your project extension
"""


def callback(incomeLevel, gpa, testScores, tuitionAndFees, totalAid):
    # Get all of the values
    incomeLevel = incomeLevel.get()
    gpa = gpa.get()
    testScores = testScores.get()
    tuitionAndFees = tuitionAndFees.get()
    totalAid = totalAid.get()

    # Strip family income, tuition cost, and financial aid of commas (that way they are compatible with the dictionaries)
    incomeLevel = incomeLevel.replace(",", "")
    tuitionAndFees = tuitionAndFees.replace(",", "")
    totalAid = totalAid.replace(",", "")

    #At this point, all of the input is parseable with dictionaries. Get all of the dictionaries we need
    #These are lists of dictionaries
    annualIncome = parser.parseCSVFile("annualIncome.csv")
    collegeGPA = parser.parseCSVFile("collegeGPA.csv")
    earningsIncome = parser.parseCSVFile("earningsIncome.csv")
    monthsElapsed = parser.parseCSVFile("monthsElapsed.csv")

    dictionaryList = [annualIncome, collegeGPA, earningsIncome, monthsElapsed]

    #We now need every appropriate row that matches our inputs
    #Example: user inputs 3.31-3.70 as H.S. GPA. We return the '3.31-3.70' value of each dictionary
    gpaListOfLists = [annualIncome[0][gpa], collegeGPA[0][gpa], earningsIncome[0][gpa], monthsElapsed[0][gpa]]
    satListOfLists = [annualIncome[1][testScores], collegeGPA[1][testScores], earningsIncome[1][testScores],
                      monthsElapsed[1][testScores]]
    aidListOfLists = [annualIncome[2][totalAid], collegeGPA[2][totalAid], earningsIncome[2][totalAid],
                      monthsElapsed[2][totalAid]]
    tuitionListOfLists = [annualIncome[3][tuitionAndFees], collegeGPA[3][tuitionAndFees],
                          earningsIncome[3][tuitionAndFees], monthsElapsed[3][tuitionAndFees]]
    familyIncomeListOfLists = [annualIncome[4][incomeLevel], collegeGPA[4][incomeLevel], earningsIncome[4][incomeLevel],
                               monthsElapsed[4][incomeLevel]]


    #Next:
    aggregateScoreAnnualIncome = []
    aggregateScoreCollegeGPA = []
    aggregateScoreEarningsIncome = []
    aggregateScoreMonthsElapsed = []

    aggregateScoreAnnualIncome.append(weightedAverage.weightedAverage(gpaListOfLists[0]))
    aggregateScoreAnnualIncome.append(weightedAverage.weightedAverage(satListOfLists[0]))
    aggregateScoreAnnualIncome.append(weightedAverage.weightedAverage(aidListOfLists[0]))
    aggregateScoreAnnualIncome.append(weightedAverage.weightedAverage(tuitionListOfLists[0]))
    aggregateScoreAnnualIncome.append(weightedAverage.weightedAverage(familyIncomeListOfLists[0]))

    aggregateScoreCollegeGPA.append(weightedAverage.weightedAverage(gpaListOfLists[1]))
    aggregateScoreAnnualIncome.append(weightedAverage.weightedAverage(satListOfLists[1]))
    aggregateScoreCollegeGPA.append(weightedAverage.weightedAverage(aidListOfLists[1]))
    aggregateScoreCollegeGPA.append(weightedAverage.weightedAverage(tuitionListOfLists[1]))
    aggregateScoreCollegeGPA.append(weightedAverage.weightedAverage(familyIncomeListOfLists[1]))

    aggregateScoreEarningsIncome.append(weightedAverage.weightedAverage(gpaListOfLists[2]))
    aggregateScoreAnnualIncome.append(weightedAverage.weightedAverage(satListOfLists[2]))
    aggregateScoreEarningsIncome.append(weightedAverage.weightedAverage(aidListOfLists[2]))
    aggregateScoreEarningsIncome.append(weightedAverage.weightedAverage(tuitionListOfLists[2]))
    aggregateScoreEarningsIncome.append(weightedAverage.weightedAverage(familyIncomeListOfLists[2]))

    aggregateScoreMonthsElapsed.append(weightedAverage.weightedAverage(gpaListOfLists[3]))
    aggregateScoreAnnualIncome.append(weightedAverage.weightedAverage(satListOfLists[3]))
    aggregateScoreMonthsElapsed.append(weightedAverage.weightedAverage(aidListOfLists[3]))
    aggregateScoreMonthsElapsed.append(weightedAverage.weightedAverage(tuitionListOfLists[3]))
    aggregateScoreMonthsElapsed.append(weightedAverage.weightedAverage(familyIncomeListOfLists[3]))

    annualIncomeTotalScore = returnAverage.returnAverage(aggregateScoreAnnualIncome)
    collegeGPATotalScore = returnAverage.returnAverage(aggregateScoreCollegeGPA)
    earningsIncomeTotalScore = returnAverage.returnAverage(aggregateScoreEarningsIncome)
    monthsElapsedTotalScore = returnAverage.returnAverage(aggregateScoreMonthsElapsed)

    if monthsElapsedTotalScore == 1:
        monthsElapsedTotalScore = "1 to 9"
    elif monthsElapsedTotalScore == 2:
        monthsElapsedTotalScore = "10 to 18"
    elif monthsElapsedTotalScore == 3:
        monthsElapsedTotalScore = "19 to 27"
    elif monthsElapsedTotalScore == 4:
        monthsElapsedTotalScore = "28 to 36"
    elif monthsElapsedTotalScore == 5:
        monthsElapsedTotalScore = "37 to 45"
    elif monthsElapsedTotalScore == 6:
        monthsElapsedTotalScore = "46 to 54"
    elif monthsElapsedTotalScore == 7:
        monthsElapsedTotalScore = "55 to 63"
    elif monthsElapsedTotalScore == 8:
        monthsElapsedTotalScore = "64 to 72"

    if collegeGPATotalScore == 1:
        collegeGPATotalScore = "0 to 0.5"
    elif collegeGPATotalScore == 2:
        collegeGPATotalScore = "0.6 to 1.5"
    elif collegeGPATotalScore == 3:
        collegeGPATotalScore = "1.6 to 2.0"
    elif collegeGPATotalScore == 4:
        collegeGPATotalScore = "2.1 to 2.5"
    elif collegeGPATotalScore == 5:
        collegeGPATotalScore = "2.6 to 3.0"
    elif collegeGPATotalScore == 6:
        collegeGPATotalScore = "3.1 to 3.3"
    elif collegeGPATotalScore == 7:
        collegeGPATotalScore = "3.4 to 3.7"
    elif collegeGPATotalScore == 8:
        collegeGPATotalScore = "3.8 to 4.0"

    if earningsIncomeTotalScore == 1:
        earningsIncomeTotalScore = "$1 to $3,000"
    elif earningsIncomeTotalScore == 2:
        earningsIncomeTotalScore = "$3,001 to $5,000"
    elif earningsIncomeTotalScore == 3:
        earningsIncomeTotalScore = "$5,001 to $6,500"
    elif earningsIncomeTotalScore == 4:
        earningsIncomeTotalScore = "$6,501 to $8,000"
    elif earningsIncomeTotalScore == 5:
        earningsIncomeTotalScore = "$8,001 to $9,700"
    elif earningsIncomeTotalScore == 6:
        earningsIncomeTotalScore = "$9,701 to $12,500"
    elif earningsIncomeTotalScore == 7:
        earningsIncomeTotalScore = "$12,501 to $14,300"
    elif earningsIncomeTotalScore == 8:
        earningsIncomeTotalScore = "$14,301+"

    if annualIncomeTotalScore == 1:
        annualIncomeTotalScore = "$0 to $5,000"
    elif annualIncomeTotalScore == 2:
        annualIncomeTotalScore = "$5,001 to $15,000"
    elif annualIncomeTotalScore == 3:
        annualIncomeTotalScore = "$15,001 to $35,000"
    elif annualIncomeTotalScore == 4:
        annualIncomeTotalScore = "$35,001 to $50,000"
    elif annualIncomeTotalScore == 5:
        annualIncomeTotalScore = "$50,001 to $75,000"
    elif annualIncomeTotalScore == 6:
        annualIncomeTotalScore = "$75,001 to $90,000"
    elif annualIncomeTotalScore == 7:
        annualIncomeTotalScore = "$90,001 to $150,000"
    elif annualIncomeTotalScore == 8:
        annualIncomeTotalScore = "$150,000+"

<<<<<<< HEAD
    photo = Tkinter.PhotoImage(file=r"blue.gif")
    cv = Tkinter.Canvas()

    cv.create_image(0, 0, image=photo, anchor='s')
=======
    #photo = Tkinter.PhotoImage(file=r"blue.gif")
    cv = Tkinter.Canvas()

    #cv.create_image(0, 0, image=photo, anchor='s')
>>>>>>> c0c6234317eae29c6503f61129778321b5a4eef4
    cv.pack(side='bottom', fill='both', expand='yes')



    var = Tkinter.StringVar()
    openingLabel = Tkinter.Label(cv, text="After complex statistical analyses, we have determined the following:", bg='white', font=("HelveticaNeue", 20))
    message = Tkinter.Label(cv, text='Your predicted GPA while in college:', bg='white')
    message2 = Tkinter.Label(cv, text='Your anticipated earnings in college:', bg='white')
    message3 = Tkinter.Label(cv, text='The forecasted number of months until you receive your first degree:', bg='white')
    message4 = Tkinter.Label(cv, text='Your estimated annual income post-graduation:', bg='white')

    openingLabel.pack(pady=0, side='top')
    message.pack(pady=0, side='top')
    var.set(collegeGPATotalScore)
    output = Tkinter.Label(cv, text=var.get(), bg='white', font=("HelveticaNeue", 16))
    output.pack(pady=0, side='top')

    message2.pack(pady=0, side='top')
    var.set(earningsIncomeTotalScore)
    output2 = Tkinter.Label(cv, text=var.get(), bg='white', font=("HelveticaNeue", 16))
    output2.pack(pady=0, side='top')

    message3.pack(pady=0, side='top')
    var.set(monthsElapsedTotalScore)
    output3 = Tkinter.Label(cv, text=var.get(), bg='white', font=("HelveticaNeue", 16))
    output3.pack(pady=0, side='top')

    message4.pack(pady=0, side='top')
    var.set(annualIncomeTotalScore)
    output4 = Tkinter.Label(cv, text=var.get(), bg='white', font=("HelveticaNeue", 16))
    output4.pack(pady=0, side='top')




def main(argv):
    root = Tkinter.Tk()

<<<<<<< HEAD
    photo = Tkinter.PhotoImage(file=r"blue.gif")
    cv = Tkinter.Canvas()
    # cv.pack(side='top', fill='both', expand='yes')
    cv.create_image(0, 0, image=photo, anchor='nw')
=======
    #photo = Tkinter.PhotoImage(file=r"blue.gif")
    cv = Tkinter.Canvas()
    # cv.pack(side='top', fill='both', expand='yes')
    #cv.create_image(0, 0, image=photo, anchor='nw')
>>>>>>> c0c6234317eae29c6503f61129778321b5a4eef4




    # width x height + x_offset + y_offset:
    root.title("Predictive Capability")
    root.geometry("1440x870+30+30")

    # Declare and initialize primary values as strings
    variableIncomeLevel = Tkinter.StringVar(root)
    variableHSGPARange = Tkinter.StringVar(root)
    variableATScores = Tkinter.StringVar(root)
    variableTuitionAndFees = Tkinter.StringVar(root)
    variableTotalAid = Tkinter.StringVar(root)

    #Initialize primary value with value we would like
    variableIncomeLevel.set("Enter your parents' income level:")
    variableHSGPARange.set("Enter your high school GPA:")
    variableATScores.set("Enter your SAT score (1600 point scale):")
    variableTuitionAndFees.set("Enter the full tuition of your university:")
    variableTotalAid.set("Enter the total amount of financial aid you are receiving:")

    #Make the label for the window, comboBoxes, and buttons
    titleLabel = Tkinter.Label(cv, text="                                        Predicting Educational Outcomes Through Statistical Methods                                        ", bg='white', font=("HelveticaNeue", 32))
    incomeLevelBox = Tkinter.OptionMenu(cv, variableIncomeLevel, "$0-$5,000", "$5,001-$15,000", "$15,001-$35,000",
                                        "$35,001-$50,000", "$50,001-$75,000", "$75,001-$90,000", "$90,001-$150,000",
                                        "$150,001+")
    gpaLevelBox = Tkinter.OptionMenu(cv, variableHSGPARange, "0-0.50", "0.51-1.50", "1.51-2.00", "2.01-2.50",
                                     "2.51-3.00", "3.01-3.30", "3.31-3.70", "3.71-4.0+")
    ATScoresBox = Tkinter.OptionMenu(cv, variableATScores, "400-640", "641-800", "801-960", "961-1080", "1081-1200",
                                     "1201-1360", "1361-1440", "1441+")
    tuitionAndFeesBox = Tkinter.OptionMenu(cv, variableTuitionAndFees, "$1-$7,000", "$7,001-$14,000", "$14,001-$21,000",
                                           "$21,001-$28,000", "$28,001-$35,000", "$35,001-$42,000", "$42,001+")
    totalAidBox = Tkinter.OptionMenu(cv, variableTotalAid, "$0-$7,000", "$7,001-$14,000", "$14,001-$21,000",
                                     "$21,001-$28,000", "$28,001-$35,000", "$35,001+")


    # var = Tkinter.StringVar()
    # var.set(annualIncomeTotalScore)
    # output = Tkinter.Label(cv, textvariable=var.get(), bg='yellow')
    # var.set(collegeGPATotalScore)
    # output2 = Tkinter.Label(cv, textvariable=var.get(), bg='yellow')
    # var.set(earningsIncomeTotalScore)
    # output3 = Tkinter.Label(cv, textvariable=var.get(), bg='yellow')
    # var.set(monthsElapsedTotalScore)
    # output4 = Tkinter.Label(cv, textvariable=var.get(), bg='yellow')
    #
    # message = Tkinter.Label(cv, text='Your predicted college GPA:', bg='yellow')
    # message2 = Tkinter.Label(cv, text='Your predicted earnings in college:', bg='yellow')
    # message3 = Tkinter.Label(cv, text='Your predicted number of months until you receive your first degree:', bg='yellow')
    # message4 = Tkinter.Label(cv, text='Your predicted annual income post graduation', bg='yellow')

    predictiveButton = Tkinter.Button(cv, text="Run Statistical Analysis",
                                      command=lambda: callback(variableIncomeLevel, variableHSGPARange,
                                                               variableATScores, variableTuitionAndFees,
                                                               variableTotalAid))


    #Pack, pack, pack and canvas layout

    cv.pack(fill='both', expand=-1)
    titleLabel.pack(pady=20, side='top')
    incomeLevelBox.pack(padx=7, pady=5, side='top')
    gpaLevelBox.pack(padx=7, pady=5, side='top')
    ATScoresBox.pack(padx=7, pady=5, side='top')
    tuitionAndFeesBox.pack(padx=7, pady=5, side='top')
    totalAidBox.pack(padx=7, pady=5, side='top')
    predictiveButton.pack(padx=0, pady=20, side='top')

    # incomeLevelBox.pack(anchor='n')
    # gpaLevelBox.pack(anchor='n')
    # ATScoresBox.pack(anchor='n')
    # tuitionAndFeesBox.pack(anchor='n')
    # totalAidBox.pack(anchor='n')
    # predictiveButton.pack(anchor='w')


    root.mainloop()

# Similarly, do not place any code below them
if __name__ == "__main__":
<<<<<<< HEAD
    main(sys.argv)
=======
    main(sys.argv)
>>>>>>> c0c6234317eae29c6503f61129778321b5a4eef4
