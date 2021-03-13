# Integrative model of the γTuSC-Spc110 complex

This repository pertains to the integrative model of the  γTuSC-Spc110 complex based on data from cryo-EM, chemical crosslinking, and X-ray crystallography.

The repository contains input data, scripts for modeling and results including bead models and localization probability density maps. It uses
[IMP](https://integrativemodeling.org) (*Integrative Modeling Platform*).

## Folder structure:
1) [inputs](inputs/) : contains all the input data used for modeling such as PDB files and crosslink files.
2) [scripts](scripts/) : scripts to prep input files, perform sampling, and analysis are provided.
3) [results](results/) : contains the models and localization densities of the top cluster.
4) [test](test/) : scripts for testing the sampling

## Protocol:

### Simulations
There are three independent simulations:
1) Modeling of one copy of γTuSC bound to Spc110 dimer : `gtusc_spc110dimer` or `dimer`
2) Modeling of one copy of γTuSC bound to Spc110 monomer : `gtusc_spc110monomer` or `monomer`
4) Modeling of two copies of laterally associated γTuSC bound to one Spc110 dimer each : `lateral_gtusc_spc110tetramer` or `tetramer`

### Sampling
To run the sampling, run modeling scripts like this
```
mpirun -np 6 $IMP python scripts/sample/sample_SCRIPTNAME.py prod
```
where `$IMP` is the setup script corresponding to the IMP installation directory (omit for binary installation) \
and `SCRIPTNAME` can be, for example, `gtusc_110dimer_1-220GCN4_nointra110xlinks` for the `dimer` simulations.

50 production runs were performed in the above manner for each of the simulations.

### Analysis

Good scoring models were selected using `imp-sampcon` as shown in `scripts/analysis/get_gsms.sh`

Sampling exhaustiveness tests were performed using `imp-sampcon` as shown in `scripts/analysis/sampcon.sh`

Crosslink violations were analyzed using `scripts/analysis/get_xlink_violations_gtuscSpc110.py`

## Results

For each of the simulations, the following files are in the [results](results/) directory
* `cluster_center_model.rmf3` : representative bead model of the major cluster
* `densities_session.py` : to view the localization densities (.mrc files)
*  `crosslink_violations_*.txt` : list of violated crosslinks


## Information
_Author(s)_: Shruthi Viswanath

_Date_: Dec 2nd, 2020

_License_: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
This work is licensed under the Creative Commons Attribution-ShareAlike 4.0
International License.

_Last known good IMP version_: [![build info](https://integrativemodeling.org/systems/35/badge.svg?branch=master)](https://integrativemodeling.org/systems/) [![build info](https://integrativemodeling.org/systems/35/badge.svg?branch=develop)](https://integrativemodeling.org/systems/)

_Testable_: Yes.

_Parallelizeable_: Yes

_Publications_:
 - Brilot, Axel F., Andrew Lyon, Alex Zelter, Shruthi Viswanath, Alison Maxwell, Michael J. MacCoss, Eric G. Muller, Andrej Sali, Trisha N. Davis, and David A. Agard. "CM1-driven assembly and activation of Yeast γ-Tubulin Small Complex underlies microtubule nucleation." bioRxiv (2020).
