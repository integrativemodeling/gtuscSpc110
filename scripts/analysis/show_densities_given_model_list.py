 
import IMP
import RMF
import IMP.atom
import IMP.rmf
import IMP.pmi
import IMP.pmi.tools
import IMP.pmi.topology
import IMP.pmi.dof
import IMP.pmi.macros
import IMP.pmi.restraints
import os,sys

def get_sample_identity(idfile_A, idfile_B):
    # whether a run belongs to run1 or run2
    sampleA_models=[]
    sampleB_models=[]

    with open(idfile_A, 'r') as f:
        for line in f:
            mod = line.split("/")[-1]
            sampleA_models.append(int(mod.strip("\n").split(" ")[1]))
    f.close()
    
    with open(idfile_B, 'r') as f:
        for line in f:
            mod = line.split("/")[-1]
            sampleB_models.append(int(mod.strip("\n").split(" ")[1]))
    return sampleA_models, sampleB_models

def parse_custom_ranges(ranges_file):
   
    fl = open(ranges_file, 'r')
    density_custom_ranges = fl.readlines()[0].strip()
    exec(density_custom_ranges)
       
    fl.close()
    
    return density_custom_ranges

model_list_file = sys.argv[1]
precision_cutoff = float(sys.argv[2]) # precision threshold for calculating resolution of the MRC
path_to_mrcs=sys.argv[3]
density_custom_file=sys.argv[4]
dimer=sys.argv[5]

density_custom_ranges=parse_custom_ranges(density_custom_file) 

sampleA_models,sampleB_models = get_sample_identity('Identities_A.txt','Identities_B.txt')

# Setup macro

gmd = IMP.pmi.analysis.GetModelDensity(custom_ranges=density_custom_ranges,resolution=precision_cutoff)

mlf = open(model_list_file,'r')

for ln in mlf.readlines():
    model = IMP.Model()
    
    model_id = int(ln.strip())
    
    if model_id in sampleA_models:
        path_to_models="./sample_A/"
    elif model_id in sampleB_models:
        path_to_models="./sample_B/"
    else:
        print "Check model ID"
       
    curr_rmf = path_to_models+"/"+ln.strip()+".rmf3"
    
    inf = RMF.open_rmf_file_read_only(curr_rmf)
    h = IMP.rmf.create_hierarchies(inf, model)[0]
    
    gmd.add_subunits_density(h)
    
mlf.close()
gmd.write_mrc(path=path_to_mrcs)
