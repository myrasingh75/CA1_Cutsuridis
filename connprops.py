# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 21:13:10 2020

@author: mbezaire
"""

W = 2

Pcell2Pcell_weight = 0.001*W
Pcell2Pcell_delay = 1

Bcell2Pcell_weight = 0.02*W
Bcell2Pcell_delay = 1
Pcell2Bcell_weight = 0.0005 *W
Pcell2Bcell_delay = 1
Bcell2Bcell_weight = 0.001*W
Bcell2Bcell_delay = 1
Bcell2BScell_weight = 0.02*W
Bcell2BScell_delay = 1
Bcell2OLMcell_weight = 0.0*W
Bcell2OLMcell_delay = 1

AAcell2Pcell_weight = 0.04*W
AAcell2Pcell_delay = 1
Pcell2AAcell_weight = 0.0005*W
Pcell2AAcell_delay = 1

BScell2Pcell_weight = 0.002*W
BScell2Pcell_delay = 1
BScell2BScell_weight = 0.002	*W # Parameter not set in original code
BScell2BScell_delay = 1	# Parameter not set in original code
BScell2Pcell_GABAB_weight = 0.0004*W
BScell2Pcell_delay = 1
Pcell2BScell_weight = 0.0005*W
Pcell2BScell_delay = 1
BScell2Bcell_weight = 0.01*W
BScell2Bcell_delay = 1

OLMcell2Pcell_weight = 0.04*W
OLMcell2Pcell_GABAB_weight = 0.0004*W
OLMcell2Pcell_delay = 1
OLMcell2Bcell_weight = 0.01*W
OLMcell2Bcell_delay = 1
Pcell2OLMcell_weight = 0.00005*W
Pcell2OLMcell_delay = 1
OLMcell2Bcell_weight = 0.0*W
OLMcell2Bcell_delay = 1