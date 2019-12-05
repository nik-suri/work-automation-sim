import sys
import pandas as pd
from progress.bar import Bar
from config import *
from util import *

# simulation parameters
TIME_STEPS = 10


def main():
    args = read_command()
    msa_list = CA_MSA_MAP.keys() if args.run_all else args.MSAs
    run_sim(msa_list)


def run_sim(msa_list):
    print_header('Simulating MSA occupations')

    for msa in msa_list:
        msa_filename = msa + '.xlsx'
        merged_filename = CLEAN_FILES + CLEAN_MERGED + msa_filename
        output_filename = OUTPUT_FILES + msa_filename

        msa_df = pd.read_excel(merged_filename)

        # model of economy which will change over time
        economy_model = {}
        for i in msa_df.index:
            soc_code = msa_df['SOC_CODE'][i]
            starting_employment = msa_df['TOT_EMP'][i]
            job_title = msa_df['OCC_TITLE'][i]
            economy_model[soc_code] = {
                'title': job_title,
                'employed-0': starting_employment,
                'automated-0': 0
            }

        progress_bar = Bar(msa, max=len(msa_df.index))

        # run simulation
        for i in msa_df.index: # for every job
            soc_code = msa_df['SOC_CODE'][i]
            growth_rate = msa_df['ANNUAL_MEAN_CHANGE'][i]
            automation_p = msa_df['AUTO_PROB'][i]
            for t in range(TIME_STEPS): # calculate every time step
                adjusted_auto_p = (automation_p / TIME_STEPS ** 2) * t ** 2

                job_data = economy_model[soc_code]
                employed_key, automated_key = 'employed-' + str(t), 'automated-' + str(t)
                n_employed, n_automated = job_data[employed_key], job_data[automated_key]

                new_demand = round((1 + growth_rate) * (n_employed + n_automated))
                automated_conversion = round(adjusted_auto_p * new_demand)

                next_employed_key, next_automated_key = 'employed-' + str(t + 1), 'automated-' + str(t + 1)
                job_data[next_employed_key] = new_demand - automated_conversion
                job_data[next_automated_key] = automated_conversion

            progress_bar.next()

        progress_bar.finish()

        # write output
        economy_df = pd.DataFrame(economy_model).T
        economy_df.to_excel(output_filename)
        print_success('MSA results written to ' + OUTPUT_FILES)


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

    args = parser.parse_args()

    if len(args.MSAs) == 0 and not args.run_all:
        parser.error('Must specify which MSAs to simulate or pass the --all flag')

    if len(args.MSAs) != 0 and args.run_all:
        print_warning('Running script with flag --all. Ignoring any positional MSA arguments.')

    return args


if __name__ == "__main__":
    main()
