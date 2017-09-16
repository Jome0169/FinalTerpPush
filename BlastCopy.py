import getopt
import sys
import os
import re
from operator import itemgetter
from datetime import datetime



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


def CreatelistOfDicts(LinesOfblast):
    ScaffDict = {}
    for line in LinesOfblast:
        if line[3] not in ScaffDict:
            ScaffDict[line[3]] = []
        else:
            pass

    return ScaffDict


def AppendGenesToScafDict(DictScaf, BlastLines):
    """TODO: Docstring for AppendGenesToScafDict.

    :DictScaf: TODO
    :BlastLines: TODO
    :returns: TODO

    """

    for line in BlastLines:
        DictScaf[line[3]].append(line)

    return DictScaf

def FilterRedunDict(arg1):
    """TODO: Docstring for FilterRedunDict.

    :arg1: TODO
    :returns: TODO

    """

    ListOfKeys = arg1.keys()    
    FilteredDict = {}
    for i in ListOfKeys:
        FilteredDict[i] = {}

    for key, value in arg1.iteritems():
        for list1 in value:
            if list1[0] not in FilteredDict[list1[3]]:
                FilteredDict[list1[3]][list1[0]] = []
                FilteredDict[list1[3]][list1[0]].append(list1)

            elif list1[0] in FilteredDict[list1[3]]:
                FilteredDict[list1[3]][list1[0]].append(list1)
    return FilteredDict


def FilterForIdentical(NestedDict):

    GeneRanges = {}
    for gene, listofhits in NestedDict.iteritems():
        ScaffPosition = []
        for blast in listofhits:
            ScaffPosition.append([])
            





def usage():
    print "The purpose of this file is to Draw isolated possibly fractioned \
    genes from the same proteins. This has been done during the terpenoid \
    project headed by Pablo Mendieta and Erin Colier Zans"
    


def main():

    Iflag = None
    Oflag = None

    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:o:h", ["input", "output", "help"])

    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
       if opt in ("-i", "-input"):
           Iflag = arg
       elif opt in ("-o", "-output"):
           Oflag = arg
       elif opt in  ("-h", "-help"):
           usage()
           sys.exit(2)
       else:
           print "Unhandeled options %s" % (otps)


    if Iflag == None:
        print "Need Input metric file from picard tools"
    elif Oflag == None:
        print "Need output file base name to write to "

    StartTime = datetime.now()

    #Function Calls
    ReadInBlast = OpenAndParseBlase(Iflag)
    ScaffoldDict = CreatelistOfDicts(ReadInBlast)
    AppenededGenes = AppendGenesToScafDict(ScaffoldDict, ReadInBlast)
    Z = FilterRedunDict(AppenededGenes)
    for Scaf, GeneDic in Z.iteritems():
        FilterForIdentical(GeneDic)

    
    #Speed Things
    EndTime = datetime.now()
    FinalTime = EndTime - StartTime

    print "Total Time %s" % (FinalTime)

if __name__=="__main__":
    main()





