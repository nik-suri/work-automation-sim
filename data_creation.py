import pandas as pd
import math

# clean employment data
# msa_employment_df = pd.read_excel('raw_data_files/oesm18ma/MSA_M2018_dl.xlsx', sheet_name='MSA_dl')
# msa_filtered = msa_employment_df.query('AREA_NAME == "San Francisco-Oakland-Hayward, CA" and TOT_EMP != "**"')[['OCC_CODE', 'TOT_EMP', 'OCC_TITLE']]
# msa_filtered.to_excel('clean_data_files/sf_employment.xlsx', sheet_name='Sheet1')
# print(msa_filtered)
# print("employment data written to sf_employment.xlsx")

# clean local projection data
oak_proj_df = pd.read_excel('raw_data_files/alltb6/oak$OccProj.xlsx', sheet_name='Sheet1')
oak_proj_filtered = oak_proj_df[['SOC Code', 'Percent-age Change 2016-2026']]
annual_rates = oak_proj_filtered['Percent-age Change 2016-2026'].add(1).pow(0.1).sub(1)
oak_proj_added = oak_proj_filtered.assign(annual_change=annual_rates)[['SOC Code', 'annual_change']]
print(oak_proj_added)
