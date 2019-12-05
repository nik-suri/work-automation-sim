from progress.bar import Bar

class OutColors:
    PURPLE = '\033[95m' # purple
    OKBLUE = '\033[34m'
    OKGREEN = '\033[32m'
    WARNING = '\033[33m' # orange
    FAIL = '\033[91m' # light red
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

OUTPUT_SEPARATOR = OutColors.PURPLE + '*****************************************************' + OutColors.ENDC
OUTPUT_ERROR = OutColors.FAIL + '***************ERROR***************' + OutColors.ENDC

def print_header(msg):
    print(OutColors.BOLD + OutColors.UNDERLINE + msg + OutColors.ENDC)

def print_success(succMsg):
    print(OutColors.OKGREEN + succMsg + OutColors.ENDC)

def print_warning(warnMsg):
    print(OutColors.WARNING + warnMsg + OutColors.ENDC)

def print_err(errMsg):
    print(OutColors.FAIL + errMsg + OutColors.ENDC)

class PercentBar(Bar):
    suffix='%(percent)d%%'
