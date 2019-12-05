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
    run_msa_sim(msa_list)
    run_nat_sim()


def run_sim(input_filename, output_filename, display):
    df = pd.read_excel(input_filename)
    progress_bar = Bar(display, max=1+len(df.index), suffix='%(percent)d%%')

    # model of economy which will change over time
    economy_model = {}
    for i in df.index:
        soc_code = df['SOC_CODE'][i]
        starting_employment = df['TOT_EMP'][i]
        job_title = df['OCC_TITLE'][i]
        economy_model[soc_code] = {
            'title': job_title,
            'employed-0': starting_employment,
            'automated-0': 0
        }

    progress_bar.next()

    # run simulation
    for i in df.index: # for every job
        soc_code = df['SOC_CODE'][i]
        growth_rate_key = 'ANNUAL_CHANGE' if input_filename == CLEAN_MERGED_NAT else 'ANNUAL_MEAN_CHANGE'
        growth_rate = df[growth_rate_key][i]
        automation_p = df['AUTO_PROB'][i]
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


def run_nat_sim():
    print_header('Simulating National occupations')
    run_sim(CLEAN_MERGED_NAT, OUTPUT_NAT, 'National Occupations')
    print_success('National results written to ' + OUTPUT_NAT)


def run_msa_sim(msa_list):
    print_header('Simulating MSA occupations')

    for msa in msa_list:
        msa_filename = msa + '.xlsx'
        input_filename = CLEAN_MERGED_MSA + msa_filename
        output_filename = OUTPUT_MSA + msa_filename
        run_sim(input_filename, output_filename, msa)

    print_success('MSA results written to ' + OUTPUT_MSA)


def read_command():
    """
    Read command line arguments.
    """
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Run a simulation for MSA-level and national-level data.')

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
