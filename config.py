RAW_FILES = 'raw_data_files/'
RAW_FREY_OSBORNE = RAW_FILES + 'frey_osborne_automation_susceptibility.xlsx'
RAW_EMPLOYMENT = RAW_FILES + 'employment/'
RAW_PROJECTIONS = RAW_FILES + 'projections/'
RAW_EMPLOYMENT_MSA = RAW_EMPLOYMENT + 'oesm18ma/MSA_M2018_dl.xlsx'
RAW_EMPLOYMENT_NAT = RAW_EMPLOYMENT + 'oesm18nat/national_M2018_dl.xlsx'
RAW_PROJECTIONS_REGIONAL = RAW_PROJECTIONS + 'alltb6/'
RAW_PROJECTIONS_NAT = RAW_PROJECTIONS + 'occupation.xlsx'

CLEAN_FILES = 'clean_data_files/'
CLEAN_FREY_OSBORNE = CLEAN_FILES + 'automation_susceptibility.xlsx'
CLEAN_EMPLOYMENT = CLEAN_FILES + 'employment/'
CLEAN_PROJECTIONS = CLEAN_FILES + 'projections/'
CLEAN_MERGED = CLEAN_FILES + 'merged/'
CLEAN_EMPLOYMENT_MSA = CLEAN_EMPLOYMENT + 'msa/'
CLEAN_EMPLOYMENT_NAT = CLEAN_EMPLOYMENT + 'national_emp.xlsx'
CLEAN_PROJECTIONS_REGIONAL = CLEAN_PROJECTIONS + 'regional/'
CLEAN_PROJECTIONS_MSA = CLEAN_PROJECTIONS + 'msa/'
CLEAN_PROJECTIONS_NAT = CLEAN_PROJECTIONS + 'national_emp_proj.xlsx'
CLEAN_MERGED_MSA = CLEAN_MERGED + 'msa/'
CLEAN_MERGED_NAT = CLEAN_MERGED + 'national_data_merged.xlsx'

OUTPUT_FILES = 'sim_outputs/'
OUTPUT_MSA = OUTPUT_FILES + 'msa/'
OUTPUT_NAT = OUTPUT_FILES + 'national_output.xlsx'

CA_MSA_MAP = {
    'Bakersfield, CA': ['bake$OccProj.xlsx'],
    'Chico, CA': ['chic$OccProj.xlsx'],
    'El Centro, CA': ['ecen$OccProj.xlsx'],
    'Fresno, CA': ['frsn$OccProj.xlsx'],
    'Hanford-Corcoran, CA': ['hanf$OccProj.xlsx'],
    'Los Angeles-Long Beach-Anaheim, CA': ['la$OccProj.xlsx', 'oran$OccProj.xlsx'],
    'Madera, CA': ['mad$OccProj.xlsx'],
    'Merced, CA': ['merc$OccProj.xlsx'],
    'Modesto, CA': ['mode$OccProj.xlsx'],
    'Napa, CA': ['napa$OccProj.xlsx'],
    'Oxnard-Thousand Oaks-Ventura, CA': ['vent$OccProj.xlsx'],
    'Redding, CA': ['redd$OccProj.xlsx'],
    'Riverside-San Bernardino-Ontario, CA': ['rive$OccProj.xlsx'],
    'Sacramento--Roseville--Arden-Arcade, CA': ['sacr$OccProj.xlsx'],
    'Salinas, CA': ['sali$OccProj.xlsx'],
    'San Diego-Carlsbad, CA': ['sand$OccProj.xlsx'],
    'San Francisco-Oakland-Hayward, CA': ['oak$OccProj.xlsx', 'sanf$OccProj.xlsx', 'sanrf$OccProj.xlsx'],
    'San Jose-Sunnyvale-Santa Clara, CA': ['sjos$OccProj.xlsx'],
    'San Luis Obispo-Paso Robles-Arroyo Grande, CA': ['slo$OccProj.xlsx'],
    'Santa Cruz-Watsonville, CA': ['scrz$OccProj.xlsx'],
    'Santa Maria-Santa Barbara, CA': ['satb$OccProj.xlsx'],
    'Santa Rosa, CA': ['satr$OccProj.xlsx'],
    'Stockton-Lodi, CA': ['stoc$OccProj.xlsx'],
    'Vallejo-Fairfield, CA': ['vall$OccProj.xlsx'],
    'Visalia-Porterville, CA': ['visa$OccProj.xlsx'],
    'Yuba City, CA': ['yuba$OccProj.xlsx'],
}
