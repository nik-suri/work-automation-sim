import pandas as pd

auto_susceptibility_df = pd.read_excel('automation_susceptibility.xlsx', sheet_name='Sheet1')
print(auto_susceptibility_df)

msa_employment_df = pd.read_excel('oesm18ma/MSA_M2018_dl.xlsx', sheet_name='SF_MSA')
print(msa_employment_df)

# keyed by job SOC code
# value is probability of automation
automation_p = {}
for i in auto_susceptibility_df.index:
    soc_code = auto_susceptibility_df['SOC code'][i]
    p = auto_susceptibility_df['Probability'][i]
    automation_p[soc_code] = p

# keyed by job SOC code
# value is [current_employment, current_automation]
economy_model = {}
for i in msa_employment_df.index:
    occ_code = msa_employment_df['OCC_CODE'][i]
    current_job_employment = msa_employment_df['TOT_EMP'][i]
    if occ_code in automation_p and current_job_employment != "**":
        job_title = msa_employment_df['OCC_TITLE'][i]
        economy_model[occ_code] = {
            'employed': current_job_employment,
            'automated': 0,
            'title': job_title
        }


# find keys in automation_p not in economy_model
delete_keys = []
for job in automation_p.keys():
    if job not in economy_model:
        delete_keys.append(job)

# delete keys in automation_p not in economy_model
for job in delete_keys:
    del automation_p[job]

# simulation parameters
time_steps = 10
growth_rate = 0.1
auto_rate = 0.2

for t in range(time_steps):
    for job in automation_p.keys():
        job_data = economy_model[job]
        curr_econ_size, curr_automated = job_data['employed'], job_data['automated']

        new_econ_size = round((1 + growth_rate) * curr_econ_size)
        automated_conversion = round(automation_p[job] * auto_rate * new_econ_size)
        new_automated = curr_automated + automated_conversion

        job_data['employed'] = new_econ_size - automated_conversion
        job_data['automated'] = new_automated

    print("time step " + str(t) + " completed")

economy_df = pd.DataFrame(economy_model).T
economy_df.to_excel('output.xlsx', sheet_name='Sheet1')
print("final jobs after " + str(time_steps) + " time steps written to 'output.xlsx'")
