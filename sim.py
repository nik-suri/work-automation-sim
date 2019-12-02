import sys
import pandas as pd

VERBOSE_SEPARATOR = '-----------------------------------'


def main():
    args = read_command( sys.argv[1:] )
    run_sim(args.time_steps, args.verbose)


def run_sim(time_steps, verbose):
    # read data
    auto_susceptibility_df = pd.read_excel('clean_data_files/automation_susceptibility.xlsx')
    if verbose:
        print('AUTOMATION SUSCEPTIBILITY DATAFRAME')
        print(auto_susceptibility_df)
        print(VERBOSE_SEPARATOR)

    employment_df = pd.read_excel('clean_data_files/sf_employment.xlsx')
    if verbose:
        print('EMPLOYMENT DATAFRAME')
        print(employment_df)
        print(VERBOSE_SEPARATOR)

    employment_proj_df = pd.read_excel('clean_data_files/sf_employment_projections.xlsx')
    if verbose:
        print('EMPLOYMENT PROJECTIONS DATAFRAME')
        print(employment_proj_df)
        print(VERBOSE_SEPARATOR)

    employment_full_df = employment_df.merge(employment_proj_df, on='SOC_CODE')
    if verbose:
        print('FULL EMPLOYMENT DATAFRAME')
        print(employment_full_df)
        print(VERBOSE_SEPARATOR)

    full_df = employment_full_df.merge(auto_susceptibility_df, on='SOC_CODE')
    if verbose:
        print('FULL SIMULATION DATAFRAME')
        print(full_df)
        print(VERBOSE_SEPARATOR)

    # model of economy which will change over time
    economy_model = {}
    for i in full_df.index:
        soc_code = full_df['SOC_CODE'][i]
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
            soc_code = full_df['SOC_CODE'][i]
            growth_rate = full_df['ANNUAL_MEAN_CHANGE'][i]

            """
            ASSUMPTION: THIS IS THE PROBABILITY THAT THE OCCUPATION WILL BE COMPLETELY AUTOMATED IN time_step YEARS
            We will calculate a quadratic fit for this value to determine the number of jobs that should be converted after 1 year
            """
            automation_p = full_df['AUTO_PROB'][i]
            adjusted_auto_p = (automation_p / time_steps ** 2) * t ** 2
            print(adjusted_auto_p)

            job_data = economy_model[soc_code]
            curr_econ_size, curr_automated = job_data['employed'], job_data['automated']

            new_econ_size = round((1 + growth_rate) * curr_econ_size)
            automated_conversion = round(adjusted_auto_p * new_econ_size)
            new_automated = curr_automated + automated_conversion

            job_data['employed'] = new_econ_size - automated_conversion
            job_data['automated'] = new_automated

        print("time step " + str(t) + " completed")

    # print output
    economy_df = pd.DataFrame(economy_model).T
    economy_df.to_excel('sim_output.xlsx')
    print("final jobs after " + str(time_steps) + " time steps written to 'sim_output.xlsx'")


def read_command(argv):
    """
    Read command line options.
    """
    from optparse import OptionParser

    parser = OptionParser()

    parser.add_option('-t', '--time-steps', dest='time_steps', default=10, type='int',
                      help='time steps to run simulation for')
    parser.add_option('-v', '--verbose', dest='verbose',
                      default=False, action='store_true',
                      help='run with verbose output')

    options, otherjunk = parser.parse_args(argv)
    if len(otherjunk) != 0:
        raise Exception('Command line input not understood: ' + str(otherjunk))

    return options


if __name__ == "__main__":
    main()
