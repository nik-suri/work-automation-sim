import pandas as pd
import matplotlib.pyplot as plt
from config import *
from util import *

def main():
    args = read_command()
    print(args)

    if args.nat:
        graph_national()
        if args.soc: graph_soc(args.soc)

    if args.msa:
        msa_list = CA_MSA_MAP.keys() if args.msa == 'all' else args.msa
        graph_msa(msa_list)
        if args.soc: graph_soc(args.soc)


def graph_soc(soc_list):
    print(soc_list)


def graph_aggregate(input_filename, output_filename, displayName):
    df = pd.read_excel(input_filename, index_col=0)

    del df['title']
    s = df.sum()

    employed_keys = ['employed-' + str(i) for i in range(11)]
    automated_keys = ['automated-' + str(i) for i in range(11)]

    data = []
    for e_k, a_k in zip(employed_keys, automated_keys):
        data.append([s[e_k], s[a_k]])
    df_growth = pd.DataFrame(data, columns=['employed', 'demand'])

    ax = df_growth.plot.area()
    ax.set_title(displayName)
    ax.get_figure().savefig(output_filename)
    plt.show()


def graph_msa(msa_list):
    for msa in msa_list:
        in_f = OUTPUT_MSA + msa + '.xlsx'
        out_f = GRAPH_MSA + msa
        graph_aggregate(in_f, out_f, msa + ' Employment')


def graph_national():
    graph_aggregate(OUTPUT_NAT, GRAPH_NAT, 'National Employment')


def read_command():
    """
    Read command line arguments.
    """
    from argparse import ArgumentParser

    parser = ArgumentParser(description=('Graph data output by the simulation. '
                                         'Default behavior is to graph everything, save it to '
                                         + GRAPH_FILES +
                                         ', and not display the files upon completion. '
                                         'Use options to specify what to graph. '
                                         'Use the --soc option to clarify which '
                                         'occupations to graph at a given level of '
                                         'granularity.'))

    parser.add_argument('--nat', dest='nat',
                        default=False, action='store_true',
                        help='graph national-level employment')
    parser.add_argument('--msa', metavar='MSA', dest='msa', nargs='*',
                        help=('MSA codes to graph MSA-level employment. '
                              'Pass \'all\' to this flag to graph all MSAs.'))
    parser.add_argument('--soc', metavar='SOC', dest='soc', nargs='*',
                        help=('Occupational SOC codes to graph single '
                              'occupation employment. Pass \'all\' to '
                              'this flag to graph all occupations.'))
    parser.add_argument('--save', dest='save',
                        default=False, action='store_true',
                        help='save files to ' + GRAPH_FILES)

    args = parser.parse_args()

    if all([not args.soc, not args.nat, not args.msa]):
        print_warning(('No data granularity options specified. '
                       'Proceeding to graph all SOC codes over '
                       'national, MSA, and individual-level '
                       'data.'))
        args.nat = True
        args.msa = 'all'
        args.soc = 'all'

    if all([args.soc, not args.nat, not args.msa]):
        print_warning(('Only SOC code(s) specified. Proceeding '
                       'to graph specified SOC code(s) over '
                       'national, MSA, and individual-level data.'))
        args.nat = True
        args.msa = 'all'

    if args.msa and args.msa[0] == 'all':
        args.msa = 'all'

    if args.soc and args.soc[0] == 'all':
        args.soc = 'all'

    return args


if __name__ == '__main__':
    main()
