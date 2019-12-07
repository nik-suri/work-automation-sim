import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from config import *
from util import *

def main():
    args = read_command()

    opts = {
        'save': args.save,
        'scale': args.scale,
        'display': args.display
    }

    print_header('Graphing Data')

    if args.nat:
        in_f = OUTPUT_NAT
        out_f = GRAPH_NAT
        displayName = 'National Employment'
        soc_path = GRAPH_SOC_NAT
        graph(in_f, out_f, displayName, soc_path, args.socs, opts)

    for msa in args.msas:
        in_f = OUTPUT_MSA + msa + '.xlsx'
        out_f = GRAPH_MSA + msa
        displayName = msa + ' Employment'
        soc_path = GRAPH_SOC + msa + '/'
        graph(in_f, out_f, displayName, soc_path, args.socs, opts)


def graph_socs(in_df, soc_path, socs, opts, progress_bar):
    df = in_df.copy()

    for soc in socs:
        if soc not in df.index:
            print(OUTPUT_ERROR)
            print_error(soc + ' not found')
            progress_bar.next()
            continue

        # compute the aggregation for this SOC - extract the row we want
        soc_row = df.loc[[soc]]

        employed_keys = ['employed-' + str(i) for i in range(11)]
        automated_keys = ['automated-' + str(i) for i in range(11)]

        data = []
        for e_k, a_k in zip(employed_keys, automated_keys):
            data.append([soc_row[e_k][0], soc_row[a_k][0]])
        df_growth = pd.DataFrame(data, columns=['employed', 'demand'])

        ax = df_growth.plot.area()
        ax.set_title(soc + ': ' + soc_row['title'][0])
        ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

        if opts['scale']:
            ax.set_ylim(0, opts['scale'])
        if opts['save']:
            ax.get_figure().savefig(soc_path + soc)
        if opts['display']:
            plt.show()
        plt.close()

        progress_bar.next()

def graph_aggregate(in_df, output_filename, displayName, opts):
    df = in_df.copy()

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
    ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    if opts['scale']:
        ax.set_ylim(0, opts['scale'])
    if opts['save']:
        ax.get_figure().savefig(output_filename)
    if opts['display']:
        plt.show()
    plt.close()


def graph(in_f, out_f, displayName, soc_path, socs, opts):
    progress_bar = PercentBar(displayName, max=2+len(socs))

    df = pd.read_excel(in_f, index_col=0)
    progress_bar.next()

    graph_aggregate(df, out_f, displayName, opts)
    progress_bar.next()

    graph_socs(df, soc_path, socs, opts, progress_bar)
    progress_bar.finish()


def read_command():
    """
    Read command line arguments.
    """
    from argparse import ArgumentParser

    parser = ArgumentParser(description=('Graph data computed by the simulation. '
                                         'Default behavior is to graph everything, save it to '
                                         + GRAPH_FILES +
                                         ', and not display the files as each is completed. '
                                         'Use options to specify what to graph. '
                                         'Use the --soc option to clarify which '
                                         'occupations to graph at a given level of '
                                         'granularity. use the --msa option to clarify '
                                         'which MSAs to graph. Alternatively, pass the '
                                         '--all-msa or --all-soc flags to graph all MSAs '
                                         'and all SOCs, respectively.'))

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
    parser.add_argument('--no-save', dest='save',
                        default=True, action='store_false',
                        help='Do not save graphs to ' + GRAPH_FILES)
    parser.add_argument('--scale', dest='scale',
                        default=None, action='store',
                        help=('set the y-axis scale limit for graphs. '
                              'Default is to auto-scale graphs'))
    parser.add_argument('--no-display', dest='display',
                        default=True, action='store_false',
                        help='Do not display graphs as they are computed')

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
