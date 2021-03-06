
"""This script samples Spc110 in conjunction with gammaTuSC.
"""
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
import IMP.pmi.restraints.stereochemistry
import IMP.pmi.restraints.basic
import IMP.pmi.io.crosslink
import IMP.pmi.restraints.crosslinking
import os,sys

# Imports needed to use ProtocolOutput
import IMP.pmi.mmcif
import ihm
import ihm.location
import ihm.model
import ihm.cross_linkers

###################### SYSTEM SETUP #####################
# Parameters to tweak

nframes = 10000
if '--test' in sys.argv:
    num_frames = 1000

# Topology File
topology_file = "../../scripts/mmcif/topology_dimer.txt"

edc_file =  '../../inputs/xlinks/spc110_1_220_GCN4dimer_rjaz180_edc30mins_q0.01_psm2.txt.INPUT.txt'
dss_file =  '../../inputs/xlinks/spc110_1_220_GCN4dimer_rjaz110_dss3mins_q0.01_psm2.txt.INPUT.txt'

# GTUSC_FLEX_MAX_TRANS = 5.0
# SPC110_FLEX_MAX_TRANS = 4.0 # for nterm region
# Common max trans parameter defined for all beads as the topology reader can only accomodate one max_trans
# This is used in place of the original GTUSC_FLEX_MAX_TRANS and SPC110_FLEX_MAX_TRANS
FLEX_MAX_TRANS = 4.0

# All IMP systems start out with a Model
mdl = IMP.Model()

# Read the topology file for a given state
t = IMP.pmi.topology.TopologyReader(topology_file)

# Create a BuildSystem macro to and add a state from a topology file
bs = IMP.pmi.macros.BuildSystem(mdl)

# Add deposition information
po = IMP.pmi.mmcif.ProtocolOutput(None)

bs.system.add_protocol_output(po)
po.system.title = "Integrative structure and function of the yeast gammaTuSC-Spc110 complex"
# po.system.citations.append(ihm.Citation.from_pubmed_id(000000)) #TODO


bs.add_state(t)

# executing the macro will return the root hierarchy and degrees of freedom (dof) objects
root_hier, dof = bs.execute_macro(max_rb_trans= 1.0,
                                  max_rb_rot= 0.1,
                                  max_bead_trans= FLEX_MAX_TRANS)

# Add Molecules for each component as well as representations
gtusc_mols = []
spc110_mols = []

for mol in root_hier.get_children()[0].get_children():

    if IMP.atom.Molecule(mol).get_name() == "Spc110":
        spc110_mols.append(mol)
    else:
        gtusc_mols.append(mol)

####################### RESTRAINTS #####################
output_objects = [] # keep a list of functions that need to be reported
display_restraints = [] # display as springs in RMF

# Connectivity keeps things connected along the backbone (ignores if inside same rigid body)
crs = []
for mol in root_hier.get_children()[0].get_children():
    cr = IMP.pmi.restraints.stereochemistry.ConnectivityRestraint(mol,scale=4.0)
    cr.add_to_model()
    output_objects.append(cr)
    crs.append(cr)

#now add EV term
# Excluded volume - automatically more efficient due to rigid bodies
evr1 = IMP.pmi.restraints.stereochemistry.ExcludedVolumeSphere(included_objects = spc110_mols,resolution=10)
evr1.set_label('spc110')
evr1.set_weight(1.0)
evr1.add_to_model()
output_objects.append(evr1)

evr2 = IMP.pmi.restraints.stereochemistry.ExcludedVolumeSphere(included_objects = spc110_mols, other_objects=gtusc_mols,resolution=20)
evr2.set_weight(10.0)
evr2.set_label('spc110_gtusc')
evr2.add_to_model()
output_objects.append(evr2)

evr3 = IMP.pmi.restraints.stereochemistry.ExcludedVolumeSphere(included_objects = gtusc_mols,resolution=20)
evr3.set_weight(0.01)
evr3.set_label('gtusc')
evr3.add_to_model()
output_objects.append(evr3)

## Crosslink restraint
## Not using the proxl database loader for now
## spc110-gtusc edc xlinks

kw_edc = IMP.pmi.io.crosslink.CrossLinkDataBaseKeywordsConverter()
kw_edc.set_protein1_key("PROTEIN1")
kw_edc.set_protein2_key("PROTEIN2")
kw_edc.set_residue1_key("POSITION1")
kw_edc.set_residue2_key("POSITION2")
xldb_edc = IMP.pmi.io.crosslink.CrossLinkDataBase(kw_edc)
xldb_edc.create_set_from_file(edc_file)

xlr_edc = IMP.pmi.restraints.crosslinking.CrossLinkingMassSpectrometryRestraint(root_hier=root_hier,CrossLinkDataBase=xldb_edc,length=18.0,label="XLEDC",filelabel='edc',resolution=1,slope=0.03)

xlr_edc.add_to_model()
xlr_edc.set_weight(15.0)
output_objects.append(xlr_edc)
display_restraints.append(xlr_edc)
dof.get_nuisances_from_restraint(xlr_edc) # needed to sample the nuisance particles (noise params)

#DSS xlinks
kw_dss= IMP.pmi.io.crosslink.CrossLinkDataBaseKeywordsConverter()
kw_dss.set_protein1_key("PROTEIN1")
kw_dss.set_protein2_key("PROTEIN2")
kw_dss.set_residue1_key("POSITION1")
kw_dss.set_residue2_key("POSITION2")
xldb_dss = IMP.pmi.io.crosslink.CrossLinkDataBase(kw_dss)
xldb_dss.create_set_from_file(dss_file)

xlr_dss = IMP.pmi.restraints.crosslinking.CrossLinkingMassSpectrometryRestraint(root_hier=root_hier,CrossLinkDataBase=xldb_dss,length=28.0,label="XLDSS",filelabel='dss',resolution=1,slope=0.03)

xlr_dss.add_to_model()
xlr_dss.set_weight(15.0)
output_objects.append(xlr_dss)
display_restraints.append(xlr_dss)
dof.get_nuisances_from_restraint(xlr_dss) # needed to sample the nuisance particles (noise params)

# Add distance restraint to make Spc110 termini stay close together
dsr = IMP.pmi.restraints.basic.DistanceRestraint(tuple_selection1=(222,222,"Spc110",0),tuple_selection2=(222,222,"Spc110",1),distancemax=5,distancemin=0,root_hier=root_hier)
dsr.add_to_model()
output_objects.append(dsr)

####################### SAMPLING #####################
# First shuffle the system
# fixing the coiled-coil that is bound to gtusc
spc110_nterm_beads = []

for cp in [0,1]:
    spc110_nterm_beads+= IMP.atom.Selection(root_hier,molecule='Spc110',copy_index=cp,residue_indexes=range(0,163)).get_selected_particles()

IMP.pmi.tools.shuffle_configuration(spc110_nterm_beads,max_translation=50)

# above 4 code lines are meant to replace the following lines
# IMP.pmi.tools.shuffle_configuration([spc110_mols[0][0:163],spc110_mols[1][0:163]],max_translation=50)
# fixing the coiled-coil that is bound to gtusc

# Quickly move all flexible beads into place
dof.optimize_flexible_beads(100)

# Run replica exchange Monte Carlo sampling
mc1=IMP.pmi.macros.ReplicaExchange0(mdl,
                                    root_hier=root_hier,                          # pass the root hierarchy
                                    crosslink_restraints=display_restraints,                     # will display like XLs
                                    monte_carlo_temperature = 1.0,
                                    replica_exchange_minimum_temperature = 1.0,
                                    replica_exchange_maximum_temperature = 2.5,
                                    num_sample_rounds = 1,
                                    monte_carlo_sample_objects=dof.get_movers(),  # pass MC movers
                                    global_output_directory='output/',
                                    output_objects=output_objects,
                                    monte_carlo_steps=10,
                                    number_of_frames=nframes,
                                    number_of_best_scoring_models=10,
                                    test_mode=True)

mc1.execute_macro()

po.finalize()

s = po.system

import ihm.dumper
with open('initial.cif', 'w') as fh:
    ihm.dumper.write(fh, [s])
for r in s.restraints:
    if isinstance(r, ihm.restraint.CrossLinkRestraint):
        print("XL-MS dataset at:", r.dataset.location.path)
        print("Details:", r.dataset.location.details)

edc,dss = [r for r in s.restraints
               if isinstance(r, ihm.restraint.CrossLinkRestraint)]
edc.linker = ihm.cross_linkers.edc
dss.linker = ihm.cross_linkers.dss

last_step = s.orphan_protocols[-1].steps[-1]
print(last_step.num_models_end)
last_step.num_models_end = 500000 #10,000 models per run and 50 independent runs (6 cores per run)


protocol = po.system.orphan_protocols[-1]
analysis = ihm.analysis.Analysis()
protocol.analyses.append(analysis)
analysis.steps.append(ihm.analysis.ClusterStep(
                      feature='RMSD', num_models_begin=500000,
                      num_models_end=2840))
mg = ihm.model.ModelGroup(name="Cluster 0")

po.system.state_groups[-1][-1].append(mg)

e = ihm.model.Ensemble(model_group=mg,
                       num_models=2840,
                       post_process=analysis.steps[-1],
                       name="Cluster 0",
                       clustering_method='Density based threshold-clustering',
                       clustering_feature='RMSD',
                       precision='18.6'
                       )
po.system.ensembles.append(e)

Uniprot={'Spc97.0':'P38863',
         'Spc98.0':'P53540',
         'Tub4.0':'P53378',
         'Tub4.1':'P53378',
         'Spc110.0':'P32380',
         'Spc110.1':'P32380'}

for prot, entry in Uniprot.items():
     ref = ihm.reference.UniProtSequence.from_accession(entry)

     if prot.startswith('Tub4'):
         ref.Alignment(seq_dif=[ihm.reference.SeqDif(58,ihm.ChemComp(code='S'),ihm.ChemComp(code='C')),
          ihm.reference.SeqDif(288,ihm.ChemComp(code='G'),ihm.ChemComp(code='C'))])

     po.asym_units[prot].entity.references.append(ref)



m1 = IMP.Model()
inf1 = RMF.open_rmf_file_read_only('../../results/gtusc_spc110dimer/cluster_center_model.rmf3')
h1 = IMP.rmf.create_hierarchies(inf1, m1)[0]

for state in h1.get_children():
    comp={}
    for component in state.get_children():
            part1={}
            for i,leaf in enumerate(IMP.core.get_leaves(component)):
                p=IMP.core.XYZ(leaf.get_particle())
                part1[p.get_name()]=p.get_coordinates()
            comp[component.get_name()]=part1
del h1

for state in root_hier.get_children():
    #comp2={}
    for component in state.get_children():
            #part2={}
            for i,leaf in enumerate(IMP.core.get_leaves(component)):
                p=IMP.core.XYZ(leaf.get_particle())
                if 'Residue' in p.get_name():
                    name=p.get_name().split('_')[1]
                else:
                    name=p.get_name()
                p.set_coordinates(comp[component.get_name()][name])
                #part2[name]=p.get_coordinates()
            #comp2[component.get_name()]=part2

model = po.add_model(e.model_group)
print (e.model_group)

repo = ihm.location.Repository(doi="10.5281/zenodo.4584458", root="../..",
                  top_directory="gtuscSpc110-main",
                  url="https://zenodo.org/record/4584458/files/gtuscSpc110-main.zip")

loc_density_list={'Spc97.0':['Spc97'],
         'Spc98.0':['Spc98'],
         'Tub4.0':['Tub4'],
         'Tub4.1':['Tub4'],
         'Spc110.0':['Spc110.0-1-163','Spc110.0-164-203','Spc110.0-204-220'],
         'Spc110.1':['Spc110.1-1-163','Spc110.1-164-203','Spc110.1-204-220']}

for prot in loc_density_list:

      asym = po.asym_units[prot]

      for domain_density in loc_density_list[prot]:
          loc = ihm.location.OutputFileLocation('../../results/gtusc_spc110dimer/'+domain_density+'.mrc')
          den = ihm.model.LocalizationDensity(file=loc, asym_unit=asym)
          e.densities.append(den)

po.system.update_locations_in_repositories([repo])

po.finalize()
with open('gtusc_Spc110_dimer.cif', 'w') as fh:
    ihm.dumper.write(fh, [po.system])

import ihm.reader
with open('gtusc_Spc110_dimer.cif') as fh:
    s, = ihm.reader.read(fh)
print(s.title, s.restraints, s.ensembles, s.state_groups)
