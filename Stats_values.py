import numpy as np
from scipy import stats

def stats_values():
    lst = []

    # number of elements as input
    n = int(input(' '))

    # iterating till the range
    for i in range(0, n):
        ele = float(input())

        lst.append(ele)

    arr = np.array(lst)

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
    IQR = round((Q3 - Q1),2)

    return mean, median,std, var,mode, IQR

if __name__ == "__main__":
    mean, median,std, var,mode, IQR = stats_values()
    ## Print Descriptive statistics
    print(mean)
    print(median)
    print(std)
    print(var)
    print(mode)
    print(IQR)

