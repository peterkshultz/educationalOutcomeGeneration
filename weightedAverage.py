#Authors: Anna Hayman, Sam Freedman, Sagar Singichetti, Peter Shultz
#uniqnames: amhayman, samjfree, singichs, pshultz

import sys
import math
import copy


def weightedAverage(percentages):
    copiedList = copy.copy(percentages)
    sortedList = sorted(percentages)
    rowSum = 0
    for i in range(8):
<<<<<<< HEAD
        rowSum += ( copiedList[i] * (i + 1) )
    weightedAvg = rowSum / 100.0
    #distance = []
    # for j in range(8):
    #     distance.append(abs(weightedAvg - copiedList[j]))
    # sortedDistance = sorted(distance)
    # for j in range(8):
    #         if (sortedDistance[0] == distance[j]):
    #             column = j
    return round(weightedAvg)
=======
        rowSum += ( sortedList[i] * (i + 1) )
    weightedAvg = (rowSum / 36.0)
    distance = []
    for j in range(8):
        distance.append(abs(weightedAvg - copiedList[j]))
    sortedDistance = sorted(distance)
    for j in range(8):
            if (sortedDistance[0] == distance[j]):
                column = j
    return column
>>>>>>> c0c6234317eae29c6503f61129778321b5a4eef4
