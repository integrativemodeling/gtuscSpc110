#!/usr/bin/env python
import unittest
import os
import shutil
import sys
import subprocess
import ihm.reader


TOPDIR = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), '..'))


class Tests(unittest.TestCase):

    def test_gtusc_dimer(self):
        """Test dimer simulations"""
        os.chdir(os.path.join(TOPDIR, 'scripts/sample'))
        p = subprocess.check_call(["python", "sample_gtusc_110dimer_1-220GCN4_nointra110xlinks.py", "--test"])

        # require that the number of frames is present
        total_num_lines_stat_files = 0

        for i in range(6):
            f = open("output/stat."+str(i)+".out")

            total_num_lines_stat_files += len(f.readlines())

            f.close()

        self.assertEqual(total_num_lines_stat_files,1006)

        # require that output files were produced
        for i in range(6):
            os.unlink("output/rmfs/"+str(i)+".rmf3")

            os.unlink("output/stat."+str(i)+".out")

            os.unlink("output/stat_replica."+str(i)+".out")



    def test_gtusc_monomer(self):
        """Test monomer simulations"""
        os.chdir(os.path.join(TOPDIR, 'scripts/sample'))
        p = subprocess.check_call(["python", "sample_gtusc_110mono_1-220GCN4_nointra110xlinks.py", "--test"])

        # require that the number of frames is present
        total_num_lines_stat_files = 0

        for i in range(6):
            f = open("output/stat."+str(i)+".out")

            total_num_lines_stat_files += len(f.readlines())

            f.close()

        self.assertEqual(total_num_lines_stat_files,1006)

        # require that output files were produced
        for i in range(6):
            os.unlink("output/rmfs/"+str(i)+".rmf3")

            os.unlink("output/stat."+str(i)+".out")

            os.unlink("output/stat_replica."+str(i)+".out")

    def test_gtusc_tetramer(self):
        """Test tetramer simulations"""
        os.chdir(os.path.join(TOPDIR, 'scripts/sample'))
        p = subprocess.check_call(["python", "sample_gtusc_110tetramer_1-220GCN4_nointra110xlinks.py", "--test"])

        # require that the number of frames is present
        total_num_lines_stat_files = 0

        for i in range(6):
            f = open("output/stat."+str(i)+".out")

            total_num_lines_stat_files += len(f.readlines())

            f.close()

        self.assertEqual(total_num_lines_stat_files,1006)

        # require that output files were produced
        for i in range(6):
            os.unlink("output/rmfs/"+str(i)+".rmf3")

            os.unlink("output/stat."+str(i)+".out")

            os.unlink("output/stat_replica."+str(i)+".out")

    def test_mmcif_monomer(self):
        """Test generation of monomer mmCIF output"""
        os.chdir(os.path.join(TOPDIR, 'scripts', 'mmcif'))
        if os.path.exists('gtusc_Spc110_monomer.cif'):
            os.unlink('gtusc_Spc110_monomer.cif')
        # Potentially override methods that need network access
        env = os.environ.copy()
        env['PYTHONPATH'] = \
            os.path.join(TOPDIR, 'test', 'mock') + ':' \
            + env.get('PYTHONPATH', '')
        _ = subprocess.check_call(
            ["python", "archive_110mono_1-220GCN4_nointra110xlinks.py"],
            env=env)
        # Check output file
        self._check_mmcif_file('gtusc_Spc110_monomer.cif')

    def _check_mmcif_file(self, fname):
        with open(fname) as fh:
            s, = ihm.reader.read(fh)
        self.assertEqual(len(s.citations), 0)
        self.assertEqual(len(s.software), 2)
        self.assertEqual(len(s.orphan_starting_models), 5)
        # Should be 1 state
        self.assertEqual(len(s.state_groups), 1)
        state1, = s.state_groups[0]
        # Should be 1 model
        self.assertEqual(sum(len(x) for x in state1), 1)
        # Check # of spheres and atoms in each model
        m = state1[0][0]
        self.assertEqual(len(m._spheres), 2143)
        self.assertEqual(len(m._atoms), 0)
        # Should be 1 ensemble
        self.assertEqual([e.num_models for e in s.ensembles], [1621])
        # Just two restraints - crosslinks
        xl1, xl2 = s.restraints
        self.assertEqual(len(xl1.experimental_cross_links), 44)
        self.assertEqual(len(xl1.cross_links), 57)
        self.assertEqual(len(xl2.experimental_cross_links), 42)
        self.assertEqual(len(xl2.cross_links), 46)


if __name__ == '__main__':
    unittest.main()
