import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from config import *
from util import *

def main():
    args = read_command()
    print(args)

    if args.nat:
        graph_national(args.socs)

    graph_msa(args.msas, args.socs)


def graph_soc(socs, input_filename, output_filename):

        if args.soc: graph_soc(args.soc, GRAPH_NAT_SOC + soc_row['title'][0])
    df = pd.read_excel(input_filename, index_col=0)

    for soc in socs:
        if soc not in df.index:
            print(OUTPUT_ERROR)
            print_error(soc + ' not found in ' + input_filename)
            continue

        # compute the aggregation for this SOC - extract the row we want
        soc_row = df.loc[[soc]]
        print(soc_row)

        employed_keys = ['employed-' + str(i) for i in range(11)]
        automated_keys = ['automated-' + str(i) for i in range(11)]

        data = []
        for e_k, a_k in zip(employed_keys, automated_keys):
            data.append([soc_row[e_k][0], soc_row[a_k][0]])
        df_growth = pd.DataFrame(data, columns=['employed', 'demand'])

        ax = df_growth.plot.area()
        ax.set_title(soc + ': ' + soc_row['title'][0])
        ax.set_ylim(0,175000)
        ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
        ax.get_figure().savefig(output_filename)
        plt.show()


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


def graph_msa(msas, socs):
    for msa in msas:
        in_f = OUTPUT_MSA + msa + '.xlsx'
        out_f = GRAPH_MSA + msa
        graph_aggregate(in_f, out_f, msa + ' Employment')
        graph_socs(socs)


def graph_national(socs):
    graph_aggregate(OUTPUT_NAT, GRAPH_NAT, 'National Employment')
    graph_socs(socs)


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
    parser.add_argument('--msa', metavar='MSA', dest='msas', nargs='*',
                        help='MSA codes to graph MSA-level employment')
    parser.add_argument('--all-msa', dest='all_msa',
                        default=False, action='store_true',
                        help='graph all aggregated MSAs')
    parser.add_argument('--soc', metavar='SOC', dest='socs', nargs='*',
                        help=('Graph specified occupations over specified '
                              'levels of granularity.'))
    parser.add_argument('--all-soc', dest='all_soc',
                        default=False, action='store_true',
                        help='graph all occupations')
    parser.add_argument('--save', dest='save',
                        default=False, action='store_true',
                        help='save files to ' + GRAPH_FILES)
    parser.add_argument('--scale', dest='scale',
                        default=-1, action='store',
                        help=('set the y-axis scale limit for graphs. '
                              'Default is to auto-scale graphs.'))

    args = parser.parse_args()

    """
    If user has specified:
        - all msa
    overwrite args.msas with resulting
    """
    if args.all_msa:
        print_warning('Specified --all-msa. Graphing all aggregated MSAs.')
        args.msas = CA_MSA_MAP.keys()

    """
    If user has specified:
        - all soc
    overwrite args.socs with resulting
    """
    if args.all_soc:
        print_warning('Specified --all-soc. Graphing all occupations.')
        args.socs = SOC_LIST

    """
    If user has not specified:
        - nat
        - msas
        - socs
    set all granularity
    """
    if not args.nat and not args.msas and not args.socs:
        print_warning(('No data granularity options specified. '
                       'Proceeding to graph all SOC codes over '
                       'national, MSA, and individual-level '
                       'data.'))
        args.nat = True
        args.msas = CA_MSA_MAP.keys()
        args.socs = SOC_LIST

    """
    If user has specified:
        - socs
    But not:
        - nat
        - msas
    set all granularity with those socs
    """
    if args.socs and not args.nat and not args.msas:
        print_warning(('Only SOC code(s) specified. Proceeding '
                       'to graph specified SOC code(s) over '
                       'national, MSA, and individual-level data.'))
        args.nat = True
        args.msas = CA_MSA_MAP.keys()

    """
    If we make it through these cases and these are still None
    """
    if not args.msas:
        args.msas = []

    if not args.socs:
        args.socs = []

    return args


if __name__ == '__main__':
    main()
