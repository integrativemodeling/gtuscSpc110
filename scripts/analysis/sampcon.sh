#!/bin/bash

# gtusc_spc110dimer
python ~/imp-sampcon/pyext/src/exhaust.py  -n spc110dimer_1_220GCN4 -su Spc110 -amb -dt 20.0 -d density_custom.txt

# gtusc_spc110monomer
python ~/imp-sampcon/pyext/src/exhaust.py -n spc110monomer_1_220GCN4 -su Spc110 -m cpu_omp -c 8 -g 5.0 -dt 20.0 -d density_custom.txt

# lateral_gtusc_spc110tetramer
python ~/imp-sampcon/pyext/src/exhaust.py -n spc110tetramer_1_220GCN4 -su Spc110 -amb -m cpu_omp -c 8 -g 5.0 -dt 20.0 -d density_custom.txt
