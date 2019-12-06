import pandas as pd
import matplotlib.pyplot as plt
from config import *
from util import *

def main():
    args = read_command()
    print(args)

    # merge all dfs together on SOC with only automated-10 column
    # sort this in descending order
    l = list(CA_MSA_MAP.keys())
    merged_df = pd.read_excel(OUTPUT_MSA + l[0] + '.xlsx', index_col=0)[['automated-10']]
    merged_df = merged_df.rename(columns={'automated-10': 'automated'})
    for i in range(1, len(l)):
        f = OUTPUT_MSA + l[i] + '.xlsx'
        df = pd.read_excel(f, index_col=0)[['automated-10']]
        df = df.rename(columns={'automated-10': 'automated'})
        merged_df = merged_df.merge(df, left_index=True, right_index=True)
        merged_df['automated'] = merged_df['automated_x'] + merged_df['automated_y']
        del merged_df['automated_x']
        del merged_df['automated_y']

    sorted_df = merged_df.sort_values(by='automated', ascending=False).head(5)
    print(sorted_df)

    return

    found = False
    while not found:
        low_p = p_df['SOC_CODE'][low_i]
        mid_p = p_df['SOC_CODE'][mid_i]
        high_p = p_df['SOC_CODE'][high_i]
        if low_i >= high_i:
            break
        inner_found = True
        for msa in CA_MSA_MAP.keys():
            f = OUTPUT_MSA + msa + '.xlsx'
            df = pd.read_excel(f, index_col=0)
            if low_p not in df.index:
                low_i += 1
                inner_found = False
                break
            if mid_p not in df.index:
                mid_i -= 1
                inner_found = False
                break
            if high_p not in df.index:
                high_i -= 1
                inner_found = False
                break
        found = inner_found

    print(found)
    print(low_i, low_p)
    print(mid_i, mid_p)
    print(high_i, high_p)

    return

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
