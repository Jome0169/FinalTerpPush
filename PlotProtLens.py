from sys import argv
import numpy as np
import random
from matplotlib import pyplot as plt

def OpenAndParseBlase(BlastFile):
    """TODO: Docstring for function.

    :arg1: TODO
    :returns: TODO

    """
    CleanedLined = []
    with open(BlastFile, 'r') as f:
        for line in f:
            if line.startswith('#'):
                pass
            else:
                for line in f:
                    CleanLine = line.strip().split('\t')
                    CleanedLined.append(CleanLine)

    return CleanedLined






TotalList = []
ListOfStarts = []
ListOfEnds = []

Z = OpenAndParseBlase(argv[1])

for item in Z:
    TotalList.append(int(item[1]))
    TotalList.append(int(item[2]))
    ListOfStarts.append(int(item[1]))
    ListOfEnds.append(int(item[2]))



Bins = np.arange(min(TotalList), max(TotalList), 5)





plt.xlim([min(TotalList)-5, max(TotalList)+5])

plt.hist(TotalList, bins=Bins, alpha=0.5)
plt.title('Random Gaussian TotalList (fixed number of Bins)')
plt.xlabel('variable X (20 evenly spaced Bins)')
plt.ylabel('count')

plt.show()




