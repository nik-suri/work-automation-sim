class OutColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

OUTPUT_SEPARATOR = '-----------------------------------'
OUTPUT_ERROR = OutColors.FAIL + '***************ERROR***************' + OutColors.ENDC

def printErr(errMsg):
    print(OutColors.FAIL + errMsg + OutColors.ENDC)
