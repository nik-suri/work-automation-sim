import pandas as pd
from config import *

# get all MSA dataframes
dfs = []
msa_names = []
for msa in CA_MSA_MAP.keys():
    f = OUTPUT_MSA + msa + '.xlsx'
    df = pd.read_excel(f, index_col=0)[['automated-10']]
    df = df.rename(columns={'automated-10': 'automated'})
    dfs.append(df)
    msa_names.append(msa)

# merge all dfs together on SOC with only automated-10 column
# sort this in descending order
merged_df = dfs[0]
for i in range(1, len(dfs)):
    merged_df = merged_df.merge(dfs[i], left_index=True, right_index=True)
    merged_df['automated'] = merged_df['automated_x'] + merged_df['automated_y']
    del merged_df['automated_x']
    del merged_df['automated_y']

sorted_df = merged_df.sort_values(by='automated', ascending=False).head(5)
print(sorted_df)

# get number of automated for each SOC in each MSA
data = []
for df in dfs:
    row_data = []
    for code in sorted_df.index:
        row_data.append(df['automated'][code])
    data.append(row_data)

table_df = pd.DataFrame(data, columns=sorted_df.index, index=msa_names)
print(table_df)
