import sys
import pandas as pd
from config import *
from util import *


def main():
    args = read_command()
    msa_list = CA_MSA_MAP.keys() if args.run_all else args.MSAs
    run_sim(msa_list, args.time_steps, args.verbose)


def run_sim(msa_list, time_steps, verbose):
    for msa in msa_list:
        msa_filename = msa + '.xlsx'
        merged_filename = CLEAN_FILES + CLEAN_MERGED + msa_filename
        output_filename = OUTPUT_FILES + msa_filename

        msa_df = pd.read_excel(merged_filename)
        if verbose:
            print('DATAFRAME FOR ' + msa)
            print(msa_df)
            print(OUTPUT_SEPARATOR)

        # model of economy which will change over time
        economy_model = {}
        for i in msa_df.index:
            soc_code = msa_df['SOC_CODE'][i]
            starting_employment = msa_df['TOT_EMP'][i]
            job_title = msa_df['OCC_TITLE'][i]
            economy_model[soc_code] = {
                'employed': starting_employment,
                'automated': 0,
                'title': job_title
            }

        # run simulation
        for t in range(time_steps):
            for i in msa_df.index:
                soc_code = msa_df['SOC_CODE'][i]
                growth_rate = msa_df['ANNUAL_MEAN_CHANGE'][i]

                """
                ASSUMPTION:
                THIS IS THE PROBABILITY THAT THE OCCUPATION WILL BE COMPLETELY AUTOMATED IN time_step YEARS
                We will calculate a quadratic fit for this value to determine the number of jobs that should be converted after each year
                """
                automation_p = msa_df['AUTO_PROB'][i]
                adjusted_auto_p = (automation_p / time_steps ** 2) * t ** 2

                job_data = economy_model[soc_code]
                curr_econ_size, curr_automated = job_data['employed'], job_data['automated']

                new_econ_size = round((1 + growth_rate) * curr_econ_size)
                automated_conversion = round(adjusted_auto_p * new_econ_size)
                new_automated = curr_automated + automated_conversion

                job_data['employed'] = new_econ_size - automated_conversion
                job_data['automated'] = new_automated

            print("Time step " + str(t) + " completed")

        # print output
        economy_df = pd.DataFrame(economy_model).T
        economy_df.to_excel(output_filename)

        print_success('Final employment distributions after ' + str(time_steps) + ' time steps written to "' + output_filename + '"')
        print(OUTPUT_SECTION_END)


def read_command():
    """
    Read command line arguments.
    """
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Run a simulation.')

    parser.add_argument('MSAs', metavar='MSA', nargs='*',
                        help='an MSA (metropolitan statistical area) to compute employment/automation for')
    parser.add_argument('-a', '--all', dest='run_all',
                        default=False, action='store_true',
                        help='run the simulation for all MSAs')
    parser.add_argument('-t', '--time-steps', dest='time_steps', default=10, type=int,
                        help='time steps to run simulation for')
    parser.add_argument('-v', '--verbose', dest='verbose',
                        default=False, action='store_true',
                        help='run with verbose output')

    args = parser.parse_args()

    if len(args.MSAs) == 0 and not args.run_all:
        parser.error('Must specify which MSAs to simulate or pass the --all flag')

    if len(args.MSAs) != 0 and args.run_all:
        print_warning('Running script with flag --all. Ignoring any positional MSA arguments.')

    return args


if __name__ == "__main__":
    main()
