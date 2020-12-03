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
        """Test model building"""
        os.chdir(os.path.join(TOPDIR, 'scripts/sample'))
        p = subprocess.check_call(["python", "sample_gtusc_dimer.py", "--test"])
        # todo: assert outputs, run analysis


if __name__ == '__main__':
    unittest.main()
