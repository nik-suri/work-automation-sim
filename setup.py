import os
from config import *

# clean_data_files/
if not os.path.exists(CLEAN_EMPLOYMENT_MSA):
    os.makedirs(CLEAN_EMPLOYMENT_MSA)

if not os.path.exists(CLEAN_PROJECTIONS_REGIONAL):
    os.makedirs(CLEAN_PROJECTIONS_REGIONAL)

if not os.path.exists(CLEAN_PROJECTIONS_MSA):
    os.makedirs(CLEAN_PROJECTIONS_MSA)

if not os.path.exists(CLEAN_MERGED_MSA):
    os.makedirs(CLEAN_MERGED_MSA)

# sim_outputs/
if not os.path.exists(OUTPUT_MSA):
    os.makedirs(OUTPUT_MSA)

# graphs/
if not os.path.exists(GRAPH_SOC_NAT):
    os.makedirs(GRAPH_SOC_NAT)

for msa in CA_MSA_MAP.keys():
    msa_soc_dir = GRAPH_SOC + msa
    if not os.path.exists(msa_soc_dir):
        os.makedirs(msa_soc_dir)

print('Directory setup complete.')
