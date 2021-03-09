
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


def add_gtusc_rep(mol,pdbfile,chain,unstructured_bead_size,clr):
    atomic = mol.add_structure(pdbfile,chain_id=chain,offset=0)
    mol.add_representation(atomic, resolutions=[1,20],color = clr)
    mol.add_representation(mol[:]-atomic,resolutions=[unstructured_bead_size],color=clr)
    return mol

def add_spc110_rep(mol,gtusc_pdbfile,gtusc_chain,gtusc_pdb_offset,unstructured_bead_size,clr):
    # two pdbfiles to load Spc110 from: one is the coiled coil region bound to gtusc and the other is the extra coiled coil region    # at C terminus

    gtusc_cc_structure = mol.add_structure(gtusc_pdbfile,chain_id=gtusc_chain,offset=gtusc_pdb_offset)
    # OR translate one of the chains a bit and run like below
    mol.add_representation(gtusc_cc_structure, resolutions=[1,10],color = clr)

    #central_cc_structure = mol.add_structure(central_cc_pdb_file,chain_id=central_cc_chain,offset=central_cc_offset,ca_only=True,soft_check=True)
    #mol.add_representation(central_cc_structure, resolutions=[1,10],color = clr)

    #mol.add_representation(mol[:]-gtusc_cc_structure-central_cc_structure,resolutions=[unstructured_bead_size],color = clr)

    mol.add_representation(mol[:]-gtusc_cc_structure,resolutions=[unstructured_bead_size],color = clr)

    return(mol)

###################### SYSTEM SETUP #####################
# Parameters to tweak

nframes = 10000
if '--test' in sys.argv:
    num_frames = 1000


spc110_seq_file = '../../inputs/sequence/Spc110_GS_1-220_dimer.fasta'

gtusc_seq_file = '../../inputs/sequence/5flz.fasta'

gtusc_pdbfile = '../../inputs/structure/tusc_ref14_110.pdb'


edc_file =  '../../inputs/xlinks/spc110_1_220_GCN4dimer_rjaz180_edc30mins_q0.01_psm2.txt.INPUT.txt'
dss_file =  '../../inputs/xlinks/spc110_1_220_GCN4dimer_rjaz110_dss3mins_q0.01_psm2.txt.INPUT.txt'

GTUSC_FLEX_MAX_TRANS = 5.0

SPC110_FLEX_MAX_TRANS = 4.0 # for nterm region

gtusc_missing_structure_bead_size = 20
spc110_cg_bead_size = 5

# Input sequences
gtusc_seqs = IMP.pmi.topology.Sequences(gtusc_seq_file)

spc110_seqs = IMP.pmi.topology.Sequences(spc110_seq_file)

#TODO change while changing stoichiometry
gtusc_components = {"Spc97":['A'],"Spc98":['B'],"Tub4":['C','D']}
spc110_components = {"Spc110":['E','F'],"Spc110_ccc":['A','B']}
gtusc_colors = {"Spc97":["light sea green"],"Spc98":["blue"],"Tub4":["goldenrod","goldenrod"]}
spc110_colors = {"Spc110":["lime green","lime green"]}

# Setup System and add a State
mdl = IMP.Model()
s = IMP.pmi.topology.System(mdl)

# Add deposition information
po = IMP.pmi.mmcif.ProtocolOutput(None)
s.add_protocol_output(po)
po.system.title = "Integrative structure of the yeast gammaTuSC-Spc110 dimer complex"
# po.system.citations.append(ihm.Citation.from_pubmed_id(000000)) #TODO

st = s.create_state()

# Add Molecules for each component as well as representations
mols = []
gtusc_mols = []

# first for gtusc
for prot in gtusc_components:

    for i,chain in enumerate(gtusc_components[prot]):
        if i==0:
            mol= st.create_molecule(prot,sequence=gtusc_seqs['5FLZ'+chain],chain_id=chain)
            firstmol = mol
        else:
            mol =  firstmol.create_copy(chain_id=chain)

        color = gtusc_colors[prot][i]
        mol = add_gtusc_rep(mol,gtusc_pdbfile,chain,gtusc_missing_structure_bead_size,color)
        mols.append(mol)
        gtusc_mols.append(mol)

# next for Spc110.
spc110_mols = []

for i,chain in enumerate(spc110_components['Spc110']):

    if i==0:
       mol = st.create_molecule('Spc110', sequence=spc110_seqs['Spc110'],chain_id=chain)
    else:
       mol = spc110_mols[0].create_copy(chain_id = chain)

    color = spc110_colors['Spc110'][i]

    (mol) = add_spc110_rep(mol,gtusc_pdbfile,chain,2,spc110_cg_bead_size,color)
    spc110_mols.append(mol)
    mols.append(mol)

##  calling System.build() creates all States and Molecules (and their representations)
##  Once you call build(), anything without representation is destroyed.
##  You can still use handles like molecule[a:b], molecule.get_atomic_residues() or molecule.get_non_atomic_residues()
##  However these functions will only return BUILT representations
root_hier = s.build()

# Setup degrees of freedom
#  The DOF functions automatically select all resolutions
#  Objects passed to nonrigid_parts move with the frame but also have their own independent movers.
dof = IMP.pmi.dof.DegreesOfFreedom(mdl)

# Move regions of gTuSC with unknown structure
gtusc_unstructured = []
for mol in gtusc_mols:
    gtusc_unstructured.append(mol.get_non_atomic_residues())

dof.create_flexible_beads(gtusc_unstructured,max_trans = GTUSC_FLEX_MAX_TRANS)

# DOF for Spc110
for i,mol in enumerate(spc110_mols):
   # create a rigid body for each helix

   # create floppy movers for the unstructured part
   dof.create_flexible_beads(spc110_mols[i].get_non_atomic_residues(),max_trans = SPC110_FLEX_MAX_TRANS)
   #get_non_atomic_residues is a set earlier before build, after that it returns built representations.

   dof.create_super_rigid_body(spc110_mols[i].get_non_atomic_residues(),name="spc110_NTD_srb")

#dof.create_rigid_body([spc110_mols[0][229:276],spc110_mols[1][229:276]],max_trans = 1.0 ,max_rot = 0.2,name="central_cc")

####################### RESTRAINTS #####################
output_objects = [] # keep a list of functions that need to be reported
display_restraints = [] # display as springs in RMF

# Connectivity keeps things connected along the backbone (ignores if inside same rigid body)
crs = []
for mol in mols:
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
#IMP.pmi.tools.shuffle_configuration([spc110_mols[0][0:163],spc110_mols[1][0:163],spc110_mols[0][203:276],spc110_mols[1][203:276]],max_translation=30)
IMP.pmi.tools.shuffle_configuration([spc110_mols[0][0:163],spc110_mols[1][0:163]],max_translation=50)
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
with open('initial_dimer.cif', 'w') as fh:
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

lpep = ihm.LPeptideAlphabet()

# sequence taken from PDB 5flz, differs from canonical UniProt
tub4_seq_dif_details = "Sequence matches that of PDB 5flz"
tub4_seq_dif = [ihm.reference.SeqDif(58, lpep['S'], lpep['C'], details=tub4_seq_dif_details),
                   ihm.reference.SeqDif(288, lpep['G'], lpep['C'], details=tub4_seq_dif_details)]

for prot, entry in Uniprot.items():
     ref = ihm.reference.UniProtSequence.from_accession(entry)

     if prot.startswith('Tub4'):
         ref.alignments.append(ihm.reference.Alignment(seq_dif = tub4_seq_dif))

     if prot.startswith('Spc110'):
         ref.alignments.append(ihm.reference.Alignment(db_begin=1,db_end=220,entity_begin=3,entity_end=222))

     po.asym_units[prot].entity.references.append(ref)

m = IMP.Model()
inf1 = RMF.open_rmf_file_read_only('../../results/gtusc_spc110dimer/cluster_center_model.rmf3')
h = IMP.rmf.create_hierarchies(inf1, m)[0]
IMP.rmf.link_hierarchies(inf1,[h])
IMP.rmf.load_frame(inf1,RMF.FrameID(0))
m.update()

# for state in h1.get_children():
#     comp={}
#     for component in state.get_children():
#             part1={}
#             for i,leaf in enumerate(IMP.core.get_leaves(component)):
#                 p=IMP.core.XYZ(leaf.get_particle())
#                 part1[p.get_name()]=p.get_coordinates()
#             comp[component.get_name()]=part1
# del h1
#
# for state in root_hier.get_children():
#     #comp2={}
#     for component in state.get_children():
#             #part2={}
#             for i,leaf in enumerate(IMP.core.get_leaves(component)):
#                 p=IMP.core.XYZ(leaf.get_particle())
#                 if 'Residue' in p.get_name():
#                     name=p.get_name().split('_')[1]
#                 else:
#                     name=p.get_name()
#                 p.set_coordinates(comp[component.get_name()][name])
#                 #part2[name]=p.get_coordinates()
#             #comp2[component.get_name()]=part2

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
