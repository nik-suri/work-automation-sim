import pandas as pd

msa_employment_df = pd.read_excel('raw_data_files/oesm18ma/MSA_M2018_dl.xlsx', sheet_name='MSA_dl')
msa_filtered = msa_employment_df.query('AREA_NAME == "San Francisco-Oakland-Hayward, CA" and TOT_EMP != "**"')[['OCC_CODE', 'TOT_EMP', 'OCC_TITLE']]
msa_filtered.to_excel('clean_data_files/sf_employment.xlsx', sheet_name='Sheet1')
print(msa_filtered)
print("employment data written to sf_employment.xlsx")
