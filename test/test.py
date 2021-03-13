#!/usr/bin/env python
import unittest
import os
import shutil
import sys
import subprocess

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

if __name__ == '__main__':
    unittest.main()
