#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 18:14:20 2021

@author: singhmy
"""


import matplotlib.pyplot as plt
import numpy as np

simname = 'full1'
num_pyr = 100

fstem = "pyresults/" + simname
all_spks = np.loadtxt("{}_spt.dat".format(fstem),skiprows=1)

# get pyramidal cells only (spks)
        
spks = [all_spks[i,1] for i in range(len(all_spks)) if all_spks[i,1] < num_pyr]


unique, frequency = np.unique(spks,  return_counts = True)

num_silent = num_pyr - len(unique)

hist,bins  = np.histogram(frequency,frequency.max(),(1,frequency.max()))
plt.hist(hist, bins)