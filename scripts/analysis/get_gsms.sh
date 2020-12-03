#!/bin/bash

# gtusc_spc110dimer
python ~/imp-sampcon/pyext/src/select_good.py -rd ./ -rp run. -sl "CrossLinkingMassSpectrometryRestraint_Distance_|XLDSS" "CrossLinkingMassSpectrometryRestraint_Distance_|XLEDC" ExcludedVolumeSphere_gtusc ExcludedVolumeSphere_spc110 ExcludedVolumeSphere_spc110_gtusc ConnectivityRestraint_None
-pl Total_Score -alt 0.9 0.88 0.0 0.0 0.0 -99.9 -aut 1.0 1.0 14.77 30.75 7.46 2.3 -mlt 0.0 0.0 0.0 0.0 0.0 0.0 -mut 35.0 25.0 0.0 0.0 0.0 0.0 -e

# gtusc_spc110monomer
python ~/imp-sampcon/pyext/src/select_good.py -rd ./ -rp run. -sl "CrossLinkingMassSpectrometryRestraint_Distance_|XLDSS" "CrossLinkingMassSpectrometryRestraint_Distance_|XLEDC" ExcludedVolumeSphere_gtusc ExcludedVolumeSphere_spc110 ExcludedVolumeSphere_spc110_gtusc
ConnectivityRestraint_None -pl Total_Score -alt 0.80 0.65 0.0 0.0 0.0 -99.9 -aut 1.0 1.0 15.87 2.87 2.78 1.17 -mlt 0.0 0.0 0.0 0.0 0.0 0.0 -mut 35.0 25.0 0.0 0.0 0.0 0.0 -e

# lateral_gtusc_spc110tetramer
python ~/imp-sampcon/pyext/src/select_good.py -rd ./ -rp run. -sl "CrossLinkingMassSpectrometryRestraint_Distance_|XLDSS" "CrossLinkingMassSpectrometryRestraint_Distance_|XLEDC" ExcludedVolumeSphere_spc110_gtusc -pl Total_Score -alt 0.9 0.8 0.0
-aut 1.0 1.0 5.64 -mlt 0.0 0.0 0.0 -mut 35.0 25.0 0.0 -e
