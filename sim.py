import sys
import pandas as pd

# simulation parameters
GROWTH_RATE = 0.1
AUTOMATION_RATE = 0.2


def main():
    args = read_command( sys.argv[1:] )
    time_steps = args.time_steps

    run_sim(time_steps)


def run_sim(time_steps):
    # read data
    auto_susceptibility_df = pd.read_excel('clean_data_files/automation_susceptibility.xlsx', sheet_name='Sheet1')
    print(auto_susceptibility_df)

    msa_employment_df = pd.read_excel('clean_data_files/sf_employment.xlsx', sheet_name='Sheet1')
    print(msa_employment_df)

    # build models

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
        if occ_code in automation_p:
            current_job_employment = msa_employment_df['TOT_EMP'][i]
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

    # run simulation
    for t in range(time_steps):
        for job in automation_p.keys():
            job_data = economy_model[job]
            curr_econ_size, curr_automated = job_data['employed'], job_data['automated']

            new_econ_size = round((1 + GROWTH_RATE) * curr_econ_size)
            automated_conversion = round(automation_p[job] * AUTOMATION_RATE * new_econ_size)
            new_automated = curr_automated + automated_conversion

            job_data['employed'] = new_econ_size - automated_conversion
            job_data['automated'] = new_automated

        print("time step " + str(t) + " completed")

    # print output
    economy_df = pd.DataFrame(economy_model).T
    economy_df.to_excel('output.xlsx', sheet_name='Sheet1')
    print("final jobs after " + str(time_steps) + " time steps written to 'output.xlsx'")


def read_command(argv):
    """
    Read command line options.
    """
    from optparse import OptionParser

    parser = OptionParser()

    parser.add_option('-t', '--time-steps', dest='time_steps', default=10, type='int',
                      help='time steps to run simulation for')

    options, otherjunk = parser.parse_args(argv)
    if len(otherjunk) != 0:
        raise Exception('Command line input not understood: ' + str(otherjunk))

    return options


if __name__ == "__main__":
    main()
