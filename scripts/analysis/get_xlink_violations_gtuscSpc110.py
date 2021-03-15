#!/usr/bin/env python

from __future__ import print_function
import os,sys
import subprocess

import string
import numpy

def get_models_from_file(fil):
    
    lst = []
    
    fl = open(fil,'r')
    for ln in fl.readlines():
        lst.append(int(ln.strip()))
    fl.close()
    return lst 

def get_model_identity_from_file(model_id_file):
    
    model_ids = {}
    # runid,replicaid and frameid tuple for each model
    
    fl = open(model_id_file,'r')
    for ln in fl.readlines():
        if ln.startswith('Model'):
            continue

        fields=ln.strip().split()
    
        model_ids[int(fields[0])] = (int(fields[1]),int(fields[2]),int(fields[3]))
   

    fl.close()
    
    return model_ids
    
    
class Violations(object):

    def __init__(self, threshold):

        self.violation_threshold  = threshold 
        self.violation_counts = {}  # dictionary with a key per restraint
    
    def get_number_violated_restraints(self, frame_out,rst_keyword):
        num_violated = 0

        stat_lines = frame_out.strip().split('\n')

        minimum_xlink_distances={}
        
        for ln in stat_lines:

            if not ln.startswith(rst_keyword):
                continue

            [rst,value] = ln.strip().split()
          
            # need to handle ambiguous restraints 
            items = rst.split('|')
            
            (prot1,pos1,prot2,pos2) = items[3:7]
                     
            if '.' in prot1:
                protonly1 = prot1.split('.')[0]  # separate the protein name from copy number
            else:
                protonly1 = prot1
            if '.' in prot2:
                protonly2 = prot2.split('.')[0]   # separate the protein name from copy number
            else:
                protonly2=prot2
            
            if  (protonly1,pos1,protonly2,pos2) in minimum_xlink_distances: # update with current copy's distance
                minimum_xlink_distances[(protonly1,pos1,protonly2,pos2)]=min(minimum_xlink_distances[(protonly1,pos1,protonly2,pos2)],float(value))
            else: # add a new entry 
                minimum_xlink_distances[(protonly1,pos1,protonly2,pos2)]=float(value)
            
        # finally update violation counts from the model
        for xl in minimum_xlink_distances:       
            if minimum_xlink_distances[xl] > self.violation_threshold: 
                
                num_violated += 1
                if not xl in self.violation_counts:
                    self.violation_counts[xl] = 1
                else:
                    self.violation_counts[xl] += 1
        return num_violated

cluster_models_file = sys.argv[1]
model_id_file = sys.argv[2]
xltype = sys.argv[3]

model_indices = get_models_from_file(cluster_models_file)
model_ids = get_model_identity_from_file(model_id_file)

if xltype == "EDC":
    keyword = "CrossLinkingMassSpectrometryRestraint_Distance_|XLEDC"
    Analysis = Violations(25.0)
elif xltype == "DSS":
    keyword = "CrossLinkingMassSpectrometryRestraint_Distance_|XLDSS"
    Analysis = Violations(35.0)

for mdl in model_indices:
    
    (run,rep,frame) = model_ids[mdl]
   
    stat_file_line_command = subprocess.Popen(["/home/shruthi/imp-clean/build/setup_environment.sh","python","/home/shruthi/imp-clean/imp/modules/pmi/pyext/src/process_output.py","-f","run."+str(run)+"/output/stat."+str(rep)
+".out","-n",str(frame+1)],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    frame_out,frame_err = stat_file_line_command.communicate()
    
  

    num_violated_in_model = Analysis.get_number_violated_restraints(frame_out,keyword)

num_violated_in_all_models = 0

for rst in Analysis.violation_counts:
    if Analysis.violation_counts[rst] == len(model_indices): # violated in all models
        num_violated_in_all_models+=1
        print("Violated ",rst)

print("Number of crosslinks violated in all models",num_violated_in_all_models)

