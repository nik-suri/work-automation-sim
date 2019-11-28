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

    employment_df = pd.read_excel('clean_data_files/sf_employment.xlsx', sheet_name='Sheet1')
    print(employment_df)

    employment_proj_df = pd.read_excel('clean_data_files/sf_employment_projections.xlsx', sheet_name='Sheet1')
    print(employment_proj_df)

    employment_full_df = employment_df.merge(employment_proj_df, left_on='OCC_CODE', right_on='SOC_CODE')
    print(employment_full_df)

    full_df = employment_full_df.merge(auto_susceptibility_df, left_on='OCC_CODE', right_on='SOC code')
    print(full_df)
    print(full_df.columns)

    # model of economy which will change over time
    economy_model = {}
    for i in full_df.index:
        soc_code = full_df['OCC_CODE'][i]
        starting_employment = full_df['TOT_EMP'][i]
        job_title = full_df['OCC_TITLE'][i]
        economy_model[soc_code] = {
            'employed': starting_employment,
            'automated': 0,
            'title': job_title
        }

    # run simulation
    for t in range(time_steps):
        for i in full_df.index:
            soc_code = full_df['OCC_CODE'][i]
            automation_p = full_df['Probability'][i]
            growth_rate = full_df['ANNUAL_MEAN_CHANGE'][i]

            job_data = economy_model[soc_code]
            curr_econ_size, curr_automated = job_data['employed'], job_data['automated']

            new_econ_size = round((1 + growth_rate) * curr_econ_size)
            automated_conversion = round(automation_p * AUTOMATION_RATE * new_econ_size)
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
