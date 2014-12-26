import sys
import math

def returnAverage(fiveNumbers):
    returnValue = 0
    counter = 0
    count = 0
    averagedReturnValue = 0
<<<<<<< HEAD
    # for number in range(3):
    #     x = fiveNumbers[number]
    #     counter = fiveNumbers.count(x)
    #     if (counter > 3):
    #         returnValue = fiveNumbers[number]
    #         break
    #     if (counter == 3):
    #         averagedReturnValue = fiveNumbers[number]
    #         break
    for number in range(len(fiveNumbers)):
        count += fiveNumbers[number]
        average = (count / 5.0)
    # if returnValue != 0:
    return round(average)
    # elif averagedReturnValue != 0:
    #     return int(round(((average + averagedReturnValue) / 2.0)))
    # else:
    #     return int(round(average))
=======
    for number in range(3):
        x = fiveNumbers[number]
        counter = fiveNumbers.count(x)
        if (counter > 3):
            returnValue = fiveNumbers[number]
            break
        if (counter == 3):
            averagedReturnValue = fiveNumbers[number]
            break
    for number in range(len(fiveNumbers)):
        count += fiveNumbers[number]
        average = (count / 5.0)
    if returnValue != 0:
        return int(returnValue)
    elif averagedReturnValue != 0:
        return int(round(((average + averagedReturnValue) / 2.0)))
    else:
        return int(round(average))
>>>>>>> c0c6234317eae29c6503f61129778321b5a4eef4
