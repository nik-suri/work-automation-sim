import pandas as pd
from config import *

df = pd.read_excel(OUTPUT_NAT, index_col=0)
top_employed = df.sort_values(by='employed-10', ascending=False).head(1)
print(top_employed)

employed_keys = ['employed-' + str(i) for i in range(11)]
automated_keys = ['automated-' + str(i) for i in range(11)]

data = []
for e_k, a_k in zip(employed_keys, automated_keys):
    data.append([top_employed[e_k][0], top_employed[a_k][0]])
df_growth = pd.DataFrame(data, columns=['employed', 'demand'])
print(df_growth)
print(df_growth.columns)

df_growth.plot.area().get_figure().savefig('test')
