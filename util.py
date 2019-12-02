class OutColors:
    HEADER = '\033[95m' # pink
    OKBLUE = '\033[34m'
    OKGREEN = '\033[32m'
    WARNING = '\033[33m' # orange
    FAIL = '\033[91m' # light red
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

OUTPUT_SEPARATOR = OutColors.OKBLUE + '-----------------------------------------------------' + OutColors.ENDC
OUTPUT_SECTION_END = OutColors.HEADER + ('****************************************************************\n'
                                         '****************************************************************') + OutColors.ENDC
OUTPUT_ERROR = OutColors.FAIL + '***************ERROR***************' + OutColors.ENDC

def print_bold(boldMsg):
    print(OutColors.BOLD + boldMsg + OutColors.ENDC)

def print_success(succMsg):
    print(OutColors.OKGREEN + succMsg + OutColors.ENDC)

def print_warning(warnMsg):
    print(OutColors.WARNING + warnMsg + OutColors.ENDC)

def print_err(errMsg):
    print(OutColors.FAIL + errMsg + OutColors.ENDC)
