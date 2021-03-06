# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2014 Bryant E. McDonnell
#
# Licensed under the terms of the BSD2 License
# See LICENSE.txt for details
# -----------------------------------------------------------------------------

# Local imports
import pyswmm
from pyswmm import Simulation
from pyswmm.tests.data import MODEL_WEIR_SETTING_PATH


def test_use_1():
    pyswmm.lib.use("swmm5.dll")
    sim = Simulation(MODEL_WEIR_SETTING_PATH)

def test_use_2():
    pyswmm.lib.use("swmm5")
    sim = Simulation(MODEL_WEIR_SETTING_PATH)

def test_use_3():
    try:
        pyswmm.lib.use("fakedll.dll")
    except:
        pass

def test_use_4():
    try:
        pyswmm.lib.use("fakedll")
    except:
        pass

