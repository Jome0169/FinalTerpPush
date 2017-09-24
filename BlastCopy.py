import getopt
import sys
import os
import re
from operator import itemgetter
from datetime import datetime
from DrawGenes import *



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

    RangesFound = {}

    for key, value in NestedDict.iteritems():
        AllVals = []
        for exon in value:
            AllVals.append(int(exon[4]))
            AllVals.append(int(exon[5]))
        Min = min(AllVals)
        Max = max(AllVals)
        Difference = int(Max) - int(Min)
        CreatedRange = [Min,Max,Difference]
        RangesFound[key] = CreatedRange
    
    #THis is a function call to the function below, non nested cause looks bad
    GoodGeneNames = FindScaffoldOverlap(RangesFound)
    FastSet = set(GoodGeneNames)

    FinalDict = {} 
    #Remove non Passing list
    for key, value in NestedDict.iteritems():
        if key in FastSet:
            FinalDict[key] = value
            NewSort = sorted(value, key = lambda x: int(x[4]))
            FinalDict[key] = NewSort
    
    #Compare Average Bit scores
    QScoreStorage = {}
    for key, value in FinalDict.iteritems():
        QQ = TakeAverageBitScore(value)
        QScoreStorage[key] = QQ

    maximum = max(QScoreStorage, key=QScoreStorage.get)

    BestHit =  {}

    for genename, blastscore in FinalDict.iteritems():
        if genename == maximum:
            BestHit[genename] = blastscore

    return BestHit



    


def FindScaffoldOverlap(DicionaryRegions):
    """TODO: Docstring for FindScaffoldOverlap.

    :DicionaryRegions: TODO
    :returns: TODO

    """
    RemoveGenesNameStorage = []
    KeepMe = []
    for genename, range1 in DicionaryRegions.iteritems():
        for samename, range2 in DicionaryRegions.iteritems():
            if samename == genename:
                pass
            else:
                Rrange1 = range(range1[0],range1[1])
                Rrange2 = range(range2[0],range2[1])
                Set1 = set(Rrange1)
                OvLap = Set1.intersection(Rrange2)
                if range1[2] > range2[2]:
                    RemoveGenesNameStorage.append(samename)
                elif range1[2] < range2[2]:
                    RemoveGenesNameStorage.append(genename)

    TestSet = set(RemoveGenesNameStorage)
    for genename, range1 in DicionaryRegions.iteritems():
        if genename not in TestSet:
            KeepMe.append(genename)
    return KeepMe


def TakeAverageBitScore(LisofBlast):
    """takes in a list of blast values and returns the average bit score value.
    Higher is better, and it is an attempt to ID terp regions we are the most
    certain about

    :LisofBlast: TODO
    :returns: TODO

    """
    FinalValue = 0
    TotalNum = len(LisofBlast)


    for item in LisofBlast:
        FinalValue += float(item[7])

    AvgBitScore = (float(FinalValue) / float(TotalNum))
    return AvgBitScore





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
        usage()
        sys.exit(2)
    elif Oflag == None:
        print "Need output file base name to write to "
        usage()
        sys.exit(2)

    StartTime = datetime.now()

    #Function Calls
    GeneLenFreq = []
    ReadInBlast = OpenAndParseBlase(Iflag)
    ScaffoldDict = CreatelistOfDicts(ReadInBlast)
    AppenededGenes = AppendGenesToScafDict(ScaffoldDict, ReadInBlast)
    Z = FilterRedunDict(AppenededGenes)
    for Scaf, GeneDic in Z.iteritems():
        #Below is the variable containing the final set of good location values
        BasiCount = FilterForIdentical(GeneDic)
        DrawGenes(BasiCount, Oflag)
    
    
    

    
    #Speed Things
    EndTime = datetime.now()
    FinalTime = EndTime - StartTime

    print "Total Time %s" % (FinalTime)

if __name__=="__main__":
    main()





