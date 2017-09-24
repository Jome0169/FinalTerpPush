import os 
from sys import argv
import dnaplotlib as dpl
import matplotlib.pyplot as plt
from matplotlib import gridspec
import dnaplotlib as dpl
    
dr = dpl.DNARenderer()
part_renderers = dr.SBOL_part_renderers()
   
 
def ReadBlast(arg1):
    """TODO: Docstring for ReadBlast.

    :arg1: TODO
    :returns: TODO

    """
    CleanedLine = []
    with open(arg1, 'r') as f:
        for line in f:
            Clean = line.strip().split('\t')
            CleanedLine.append(Clean)
    return CleanedLine






def CreateCDSItem(SplitUpLine):
    ListFinals = []
    Base = {'type':'CDS', 'name':'cds', 'fwd':True, 'opts':{'color':(0.5,0.5,0.5), 'x_extent':80}}
    PairsList = []
    for item in SplitUpLine:
        Pairs = [int(item[4]),int(item[5])]
        PairsList.append(Pairs)

    for key, val in Base.iteritems():
        print "THIS KEY", key
        print "THIS IS VALUE", val

    for set1 in PairsList:
        Direction = None
        if set1[0] > set1[1]:
            Direction = False

        elif set1[0] < set1[1]:
            Direction = True


Z = ReadBlast(argv[1])
CreateCDSItem(Z)


sp = {'type':'EmptySpace', 'name':'S1', 'fwd':True, 'opts':{'x_extent':1}}
prom = {'type':'Promoter', 'name':'prom', 'fwd':True}
ins  = {'type':'Insulator', 'name':'ins', 'fwd':True}
ribo_f = {'type':'Ribozyme', 'name':'ribo', 'fwd':True}
rbs_f = {'type':'RBS', 'name':'rbs', 'fwd':True, 'opts':{'color':(0.1,0.1,0.0)}}
cds_f = {'type':'CDS', 'name':'cds', 'fwd':True, 'opts':{'color':(0.5,0.5,0.5), 'x_extent':80}}
term = {'type':'Terminator', 'name':'term', 'fwd':True}


# Create the baseline design
design1 = [sp, prom, ins, ribo_f, rbs_f, cds_f, term, sp]


# Create the figure
fig = plt.figure(figsize=(2.2,0.6))
gs = gridspec.GridSpec(1, 1)
print gs[0]
ax_dna = plt.subplot(gs[0])

## Redender the DNA to axis
start, end = dr.renderDNA(ax_dna, design1, part_renderers)
ax_dna.set_xlim([start, end])
ax_dna.set_ylim([-15,28])
ax_dna.set_aspect('equal')
ax_dna.set_xticks([])
ax_dna.set_yticks([])
ax_dna.axis('off')

# Annotate the design
primer_f_opts = {'color':(1.0,0.0,0.0), 'y_offset':10}
primer_f_opts2 = {'color':(1.0,0.0,0.0), 'y_offset':15}
primer_r_opts = {'color':(1.0,0.0,0.0), 'y_offset':10}
rbs2_f_opts = {'color':(1.0,0.0,0.0), 'x_extent':7.5}
rbs3_f_opts = {'color':(1.0,0.0,0.0), 'x_extent':5}
primer1_f = {'type':'PrimerBindingSite', 'start': cds_f['start'], 'end': cds_f['end'], 'name':'pri1f', 'fwd':True, 'opts':primer_f_opts}
primer2_f = {'type':'PrimerBindingSite', 'start': cds_f['start']+10, 'end': cds_f['end'], 'name':'pri2f', 'fwd':True, 'opts':primer_f_opts2}
primer3_f = {'type':'PrimerBindingSite', 'start': cds_f['start']+50, 'end': cds_f['end'], 'name':'pri3f', 'fwd':True, 'opts':primer_f_opts}
primer4_r = {'type':'PrimerBindingSite', 'start': cds_f['end']-25, 'end': cds_f['end']-35, 'name':'pri4r', 'fwd':False, 'opts':primer_r_opts}
rbs2_f = {'type':'RBS', 'start': cds_f['start']+40, 'end': cds_f['start']+41, 'name':'rbs2f', 'fwd':True, 'opts':rbs2_f_opts}
rbs3_f = {'type':'RBS', 'start': cds_f['start']+70, 'end': cds_f['start']+71, 'name':'rbs3f', 'fwd':True, 'opts':rbs3_f_opts}

# Call the annotate function for the renderer
dr.annotate(ax_dna, part_renderers, primer1_f)
dr.annotate(ax_dna, part_renderers, primer2_f)
dr.annotate(ax_dna, part_renderers, primer3_f)
dr.annotate(ax_dna, part_renderers, primer4_r)
dr.annotate(ax_dna, part_renderers, rbs2_f)
dr.annotate(ax_dna, part_renderers, rbs3_f)

# Update subplot spacing
plt.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)

# Save the figure
fig.savefig('annotate_design.pdf', transparent=True)
fig.savefig('annotate_design.png', dpi=300)

# Clear the plotting cache
plt.close('all')

