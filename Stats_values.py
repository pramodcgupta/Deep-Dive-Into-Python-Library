import numpy as np
from scipy import stats

def getInput():

    lst = []

    # number of elements as input
    n = int(input(' '))

    # iterating till the range
    for i in range(0, n):
        ele = float(input())

        lst.append(ele)

    arr=np.array(lst)

    return arr

def stats_values(arr):
    # Calculate the mean
    mean = round(np.mean(arr), 2)

    # Calculate the median
    median = round(np.median(arr), 2)

    # Calculate the std
    std = round(np.std(arr), 2)

    # Calculate the variance
    var = round(np.var(arr), 2)

    # Calculate the mode
    mode = stats.mode(arr)
    mode=round(mode[0][0],2)


    # First quartile (Q1)
    Q1 = np.percentile(arr, 25, interpolation='midpoint')

    # Third quartile (Q3)
    Q3 = np.percentile(arr, 75, interpolation='midpoint')

    # Interquaritle range (IQR)
    IQR = round(Q3 - Q1,2)

    ## Print Descriptive statistics
    print('Mean: ', str(mean))
    print('median: ', str(median))
    print('std: ', str(std))
    print('variance: ', str(var))
    print('mode: ', str(mode))
    print('Interquaritle: ', str(IQR))

if __name__ == "__main__":
    arr=getInput()
    stats_values(arr)