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

    def test_gtusc_monomer(self):
        """Test monomer simulations"""
        os.chdir(os.path.join(TOPDIR, 'scripts/sample'))
        p = subprocess.check_call(["python", "sample_gtusc_110mono_1-220GCN4_nointra110xlinks.py", "--test"])

    def test_gtusc_tetramer(self):
        """Test tetramer simulations"""
        os.chdir(os.path.join(TOPDIR, 'scripts/sample'))
        p = subprocess.check_call(["python", "sample_gtusc_110tetramer_1-220GCN4_nointra110xlinks.py", "--test"])


if __name__ == '__main__':
    unittest.main()
