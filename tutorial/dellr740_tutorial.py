

# Copyright (c) Meta Platforms, Inc. and affiliates.

# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import json
import sys

from dram_model import Fab_DRAM
from hdd_model  import Fab_HDD
from ssd_model  import Fab_SSD
from logic_model  import Fab_Logic

debug = False

##############################
# Original Dell 740 LCA
##############################
#https://corporate.delltechnologies.com/content/dam/digitalassets/active/en/unauth/data-sheets/products/servers/lca_poweredge_r740.pdf

##############################
# Main Dell R740 integrated circuits
##############################
dellr740_large_ssd = 3840 # GB (3.84 TB x 8 SSD's)
dellr740_ssd       = 400 # GB (400GB x 1 SSD)
dellr740_ssd_dram  = 68 # GB (64 + 4GB ECC)
dellr740_dram      = 36 # GB (32 + 4 ECC GB x 12)
ic_yield           = 0.875

cpu_area = 6.98 #cm^2

##############################
# Estimated process technology node to mimic fairphone LCA process node
##############################
CPU_Logic = Fab_Logic()

SSD_main           = Fab_SSD()
SSD_secondary      = Fab_SSD()
DRAM_SSD_main      = Fab_DRAM()
DRAM_SSD_secondary = Fab_DRAM()
DRAM               = Fab_DRAM()

##############################
# Computing carbon footprint of IC's
##############################
CPU_Logic.set_area(0)
DRAM.set_capacity(0)

DRAM_SSD_main.set_capacity(0)
SSD_main.set_capacity(0)

DRAM_SSD_secondary.set_capacity(0)
SSD_secondary.set_capacity(0)

##################################
# Computing the packaging footprint
##################################
# number of packages
ssd_main_nr         = 12 + 1
ssd_secondary_nr    = 12 + 1
dram_nr             = 18 + 1
cpu_nr              = 2
packaging_intensity = 150 # gram CO2

SSD_main_packaging      = 0
SSD_secondary_packaging = 0
DRAM_packging           = 0
CPU_packaging           = 0

total_packaging = SSD_main_packaging +  \
                  SSD_secondary_packaging + \
                  DRAM_packging + \
                  CPU_packaging

total_packaging = total_packaging / 1000.

##################################
# Compute end-to-end carbon footprints
##################################
SSD_main_count = 8 # There are 8x3.84TB SSD's
SSD_main_co2 = 0
SSD_main_co2 = SSD_main_co2 * SSD_main_count

SSD_secondary_count = 1 # There are 1x400GB SSD's
SSD_secondary_co2 = 0
SSD_secondary_co2 = SSD_secondary_co2 * SSD_secondary_count

DRAM_count = 12 # There are 12 x (32GB+4GB ECC DRAM modules)
DRAM_co2 = 0

CPU_count = 2
CPU_co2   = 0

if debug:
    print("ACT SSD main", SSD_main_co2, "kg CO2")
    print("ACT SSD secondary", SSD_secondary_co2, "kg CO2")
    print("ACT DRAM", DRAM_co2, "kg CO2")
    print("ACT CPU", CPU_co2, "kg CO2")
    print("ACT Packaging", total_packaging, "kg CO2")

print("--------------------------------")
print("ACT SSD main", SSD_main_co2, "kg CO2 vs. LCA 3373 kg CO2")
print("ACT SSD secondary", SSD_secondary_co2, "kg CO2 vs. LCA 64.1 kg CO2")
print("ACT DRAM", DRAM_co2, "kg CO2 vs. LCA 533 kg CO2")
print("ACT CPU", CPU_co2, "kg CO2 vs. LCA 47 kg CO2")
