#import getopt
import sys
import os
import re
from operator import itemgetter
from datetime import datetime


import dnaplotlib as dpl
dr = dpl.DNARenderer()




def BlastParser(BlastFile):
    """TODO: Docstring for BlastParser.

    :BlastFile: TODO
    :returns: TODO

    """
    ReturnedBlastFile = {}

    with open(BlastFile, 'r') as f:
        for line in f:
            Cleaned_Line = line.strip.split('\t')




def usage():
    print "The purpose of this file is to Draw isolated possibly fractioned
    genes from the same proteins. This has been done during the terpenoid
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
    List1 = OpenFile(Iflag)
    Final = sortoutput(List1)
    WriteToFile(Oflag, Iflag, Final)
    
    #Speed Things
    EndTime = datetime.now()
    FinalTime = EndTime - StartTime

    print "Total Time %s" % (FinalTime)

if __name__=="__main__":
    main()





