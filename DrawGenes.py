"""The purpose of this file is to Draw isolated possibly fractioned
    genes from the same proteins. This has been done during the terpenoid
    project headed by Pablo Mendieta and Erin Colier Zans"""
    
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio.Graphics import GenomeDiagram
from reportlab.lib.units import cm




def DrawGenes(DictOfProt, OutputFlag):
    """Function that creates bins based off number of genes 

    :arg1: TODO
    :returns: TODO

    """
    StartEnd = []
    for genename, BlastList in DictOfProt.iteritems():
        StartEnd.append(BlastList[0][4])
        StartEnd.append(BlastList[-1][5])
        CreateRanges(BlastList)



    gdd = GenomeDiagram.Diagram('Test Diagram')
    gdt_features = gdd.new_track(1, greytrack=False)
    gds_features = gdt_features.new_set()
   
    for genename, BlastList in DictOfProt.iteritems():
        for item in BlastList:
            feature = SeqFeature(FeatureLocation(int(item[4]),int(item[5])), strand=None)
            gds_features.add_feature(feature, name="Strandless", label=True)

    #Add three features to show the strand options,
    #feature = SeqFeature(FeatureLocation(25, 125), strand=+1)
    #gds_features.add_feature(feature, name="Forward", label=True)
    #feature = SeqFeature(FeatureLocation(150, 250), strand=None)
    #gds_features.add_feature(feature, name="Strandless", label=True)
    #feature = SeqFeature(FeatureLocation(275, 375), strand=-1)
    #gds_features.add_feature(feature, name="Reverse", label=True)

    
    gdd.draw(format='linear', pagesize=(30*cm,4*cm), fragments=1,
                     start=int(StartEnd[0]), end=int(StartEnd[1]))
    
    Outputname = str(OutputFlag) + ".pdf"
    gdd.write(Outputname, "pdf")


def CreateRanges(ListofBlast):
    for item in ListofBlast:
        print item
  
    


