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

GRAPH_FILES = 'graphs/'
GRAPH_NAT = GRAPH_FILES + 'national_graph'
GRAPH_MSA = GRAPH_FILES + 'msa/'
GRAPH_SOC = GRAPH_FILES + 'occupations/'
GRAPH_SOC_NAT = GRAPH_SOC + 'national/'

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

# list of every SOC in Frey/Osborne
SOC_LIST = [
    '11-1011',
    '11-1021',
    '11-2011',
    '11-2021',
    '11-2022',
    '11-2031',
    '11-3011',
    '11-3021',
    '11-3031',
    '11-3051',
    '11-3061',
    '11-3071',
    '11-3111',
    '11-3121',
    '11-3131',
    '11-9013',
    '11-9021',
    '11-9031',
    '11-9032',
    '11-9033',
    '11-9041',
    '11-9051',
    '11-9071',
    '11-9081',
    '11-9111',
    '11-9121',
    '11-9131',
    '11-9141',
    '11-9151',
    '11-9161',
    '11-9199',
    '13-1011',
    '13-1021',
    '13-1022',
    '13-1023',
    '13-1031',
    '13-1032',
    '13-1041',
    '13-1051',
    '13-1074',
    '13-1078',
    '13-1081',
    '13-1111',
    '13-1121',
    '13-1141',
    '13-1151',
    '13-1161',
    '13-1199',
    '13-2011',
    '13-2021',
    '13-2031',
    '13-2041',
    '13-2051',
    '13-2052',
    '13-2053',
    '13-2061',
    '13-2071',
    '13-2072',
    '13-2081',
    '13-2082',
    '13-2099',
    '15-1111',
    '15-1121',
    '15-1131',
    '15-1132',
    '15-1133',
    '15-1141',
    '15-1142',
    '15-1150',
    '15-1179',
    '15-1799',
    '15-2011',
    '15-2021',
    '15-2031',
    '15-2041',
    '15-2091',
    '17-1011',
    '17-1012',
    '17-1021',
    '17-1022',
    '17-2011',
    '17-2021',
    '17-2031',
    '17-2041',
    '17-2051',
    '17-2061',
    '17-2071',
    '17-2072',
    '17-2081',
    '17-2111',
    '17-2112',
    '17-2121',
    '17-2131',
    '17-2141',
    '17-2151',
    '17-2161',
    '17-2171',
    '17-2199',
    '17-3011',
    '17-3012',
    '17-3013',
    '17-3021',
    '17-3022',
    '17-3023',
    '17-3024',
    '17-3025',
    '17-3026',
    '17-3027',
    '17-3029',
    '17-3031',
    '19-1011',
    '19-1012',
    '19-1013',
    '19-1021',
    '19-1022',
    '19-1023',
    '19-1029',
    '19-1031',
    '19-1032',
    '19-1041',
    '19-1042',
    '19-2011',
    '19-2012',
    '19-2021',
    '19-2031',
    '19-2032',
    '19-2041',
    '19-2042',
    '19-2043',
    '19-2099',
    '19-3011',
    '19-3022',
    '19-3031',
    '19-3032',
    '19-3039',
    '19-3041',
    '19-3051',
    '19-3091',
    '19-3092',
    '19-3093',
    '19-3094',
    '19-3099',
    '19-4011',
    '19-4021',
    '19-4031',
    '19-4041',
    '19-4051',
    '19-4061',
    '19-4091',
    '19-4092',
    '19-4093',
    '19-4099',
    '21-1011',
    '21-1012',
    '21-1013',
    '21-1014',
    '21-1015',
    '21-1021',
    '21-1022',
    '21-1023',
    '21-1091',
    '21-1092',
    '21-1093',
    '21-2011',
    '21-2021',
    '23-1011',
    '23-1012',
    '23-1021',
    '23-1022',
    '23-1023',
    '23-2011',
    '23-2091',
    '23-2093',
    '25-1000',
    '25-2011',
    '25-2012',
    '25-2021',
    '25-2022',
    '25-2023',
    '25-2031',
    '25-2032',
    '25-2053',
    '25-2054',
    '25-3011',
    '25-3021',
    '25-3999',
    '25-4011',
    '25-4012',
    '25-4013',
    '25-4021',
    '25-4031',
    '25-9011',
    '25-9021',
    '25-9031',
    '25-9041',
    '27-1011',
    '27-1012',
    '27-1013',
    '27-1014',
    '27-1021',
    '27-1022',
    '27-1023',
    '27-1024',
    '27-1025',
    '27-1026',
    '27-1027',
    '27-2011',
    '27-2012',
    '27-2021',
    '27-2022',
    '27-2023',
    '27-2031',
    '27-2032',
    '27-2041',
    '27-2042',
    '27-3011',
    '27-3012',
    '27-3021',
    '27-3022',
    '27-3031',
    '27-3041',
    '27-3042',
    '27-3043',
    '27-3091',
    '27-4011',
    '27-4012',
    '27-4013',
    '27-4014',
    '27-4021',
    '27-4031',
    '27-4032',
    '29-1011',
    '29-1021',
    '29-1022',
    '29-1023',
    '29-1024',
    '29-1031',
    '29-1041',
    '29-1051',
    '29-1060',
    '29-1071',
    '29-1081',
    '29-1111',
    '29-1122',
    '29-1123',
    '29-1124',
    '29-1125',
    '29-1126',
    '29-1127',
    '29-1131',
    '29-1181',
    '29-1199',
    '29-2011',
    '29-2012',
    '29-2021',
    '29-2031',
    '29-2032',
    '29-2033',
    '29-2037',
    '29-2041',
    '29-2051',
    '29-2052',
    '29-2053',
    '29-2054',
    '29-2055',
    '29-2056',
    '29-2061',
    '29-2071',
    '29-2081',
    '29-2091',
    '29-2799',
    '29-9011',
    '29-9012',
    '29-9091',
    '29-9799',
    '31-1011',
    '31-1013',
    '31-2011',
    '31-2012',
    '31-2021',
    '31-2022',
    '31-9011',
    '31-9091',
    '31-9092',
    '31-9093',
    '31-9094',
    '31-9095',
    '31-9096',
    '31-9799',
    '33-1011',
    '33-1012',
    '33-1021',
    '33-2011',
    '33-2021',
    '33-2022',
    '33-3011',
    '33-3012',
    '33-3021',
    '33-3031',
    '33-3041',
    '33-3051',
    '33-3052',
    '33-9011',
    '33-9021',
    '33-9031',
    '33-9032',
    '33-9091',
    '33-9092',
    '35-1011',
    '35-1012',
    '35-2011',
    '35-2012',
    '35-2013',
    '35-2014',
    '35-2015',
    '35-2021',
    '35-3011',
    '35-3021',
    '35-3022',
    '35-3031',
    '35-3041',
    '35-9011',
    '35-9021',
    '35-9031',
    '37-1011',
    '37-1012',
    '37-2011',
    '37-2012',
    '37-2021',
    '37-3011',
    '37-3012',
    '37-3013',
    '39-1011',
    '39-1012',
    '39-1021',
    '39-2011',
    '39-2021',
    '39-3011',
    '39-3012',
    '39-3021',
    '39-3031',
    '39-3091',
    '39-3092',
    '39-3093',
    '39-4011',
    '39-4021',
    '39-4831',
    '39-5011',
    '39-5012',
    '39-5091',
    '39-5092',
    '39-5093',
    '39-5094',
    '39-6011',
    '39-6012',
    '39-7011',
    '39-7012',
    '39-9011',
    '39-9021',
    '39-9031',
    '39-9032',
    '39-9041',
    '41-1011',
    '41-1012',
    '41-2011',
    '41-2012',
    '41-2021',
    '41-2022',
    '41-2031',
    '41-3011',
    '41-3021',
    '41-3031',
    '41-3041',
    '41-4011',
    '41-4012',
    '41-9011',
    '41-9012',
    '41-9021',
    '41-9022',
    '41-9031',
    '41-9041',
    '41-9091',
    '43-1011',
    '43-2011',
    '43-2021',
    '43-3011',
    '43-3021',
    '43-3031',
    '43-3041',
    '43-3051',
    '43-3061',
    '43-3071',
    '43-4011',
    '43-4021',
    '43-4031',
    '43-4041',
    '43-4051',
    '43-4061',
    '43-4071',
    '43-4081',
    '43-4111',
    '43-4121',
    '43-4131',
    '43-4141',
    '43-4151',
    '43-4161',
    '43-4171',
    '43-4181',
    '43-5011',
    '43-5021',
    '43-5031',
    '43-5032',
    '43-5041',
    '43-5051',
    '43-5052',
    '43-5053',
    '43-5061',
    '43-5071',
    '43-5081',
    '43-5111',
    '43-6011',
    '43-6012',
    '43-6013',
    '43-6014',
    '43-9011',
    '43-9021',
    '43-9022',
    '43-9031',
    '43-9041',
    '43-9051',
    '43-9061',
    '43-9071',
    '43-9081',
    '43-9111',
    '45-1011',
    '45-2011',
    '45-2021',
    '45-2041',
    '45-2090',
    '45-3011',
    '45-3021',
    '45-4011',
    '45-4021',
    '45-4022',
    '45-4023',
    '47-1011',
    '47-2011',
    '47-2021',
    '47-2022',
    '47-2031',
    '47-2041',
    '47-2042',
    '47-2043',
    '47-2044',
    '47-2051',
    '47-2053',
    '47-2061',
    '47-2071',
    '47-2072',
    '47-2073',
    '47-2081',
    '47-2082',
    '47-2111',
    '47-2121',
    '47-2131',
    '47-2132',
    '47-2141',
    '47-2142',
    '47-2151',
    '47-2152',
    '47-2161',
    '47-2171',
    '47-2181',
    '47-2211',
    '47-2221',
    '47-3011',
    '47-3012',
    '47-3013',
    '47-3014',
    '47-3015',
    '47-3016',
    '47-4011',
    '47-4021',
    '47-4031',
    '47-4041',
    '47-4051',
    '47-4061',
    '47-4071',
    '47-4091',
    '47-4799',
    '47-5011',
    '47-5012',
    '47-5013',
    '47-5021',
    '47-5031',
    '47-5041',
    '47-5042',
    '47-5051',
    '47-5061',
    '47-5071',
    '47-5081',
    '49-1011',
    '49-2011',
    '49-2021',
    '49-2022',
    '49-2091',
    '49-2092',
    '49-2093',
    '49-2094',
    '49-2095',
    '49-2096',
    '49-2097',
    '49-2098',
    '49-3011',
    '49-3021',
    '49-3022',
    '49-3023',
    '49-3031',
    '49-3041',
    '49-3042',
    '49-3043',
    '49-3051',
    '49-3052',
    '49-3053',
    '49-3091',
    '49-3092',
    '49-3093',
    '49-9011',
    '49-9012',
    '49-9021',
    '49-9031',
    '49-9041',
    '49-9043',
    '49-9044',
    '49-9045',
    '49-9051',
    '49-9052',
    '49-9061',
    '49-9062',
    '49-9063',
    '49-9064',
    '49-9071',
    '49-9091',
    '49-9092',
    '49-9093',
    '49-9094',
    '49-9095',
    '49-9096',
    '49-9097',
    '49-9098',
    '49-9799',
    '51-1011',
    '51-2011',
    '51-2021',
    '51-2022',
    '51-2023',
    '51-2031',
    '51-2041',
    '51-2091',
    '51-2092',
    '51-2093',
    '51-3011',
    '51-3021',
    '51-3022',
    '51-3023',
    '51-3091',
    '51-3092',
    '51-3093',
    '51-4011',
    '51-4012',
    '51-4021',
    '51-4022',
    '51-4023',
    '51-4031',
    '51-4032',
    '51-4033',
    '51-4034',
    '51-4035',
    '51-4041',
    '51-4051',
    '51-4052',
    '51-4061',
    '51-4062',
    '51-4071',
    '51-4072',
    '51-4081',
    '51-4111',
    '51-4121',
    '51-4122',
    '51-4191',
    '51-4192',
    '51-4193',
    '51-4194',
    '51-5111',
    '51-5112',
    '51-5113',
    '51-6011',
    '51-6021',
    '51-6031',
    '51-6041',
    '51-6042',
    '51-6051',
    '51-6052',
    '51-6061',
    '51-6062',
    '51-6063',
    '51-6064',
    '51-6091',
    '51-6092',
    '51-6093',
    '51-7011',
    '51-7021',
    '51-7031',
    '51-7032',
    '51-7041',
    '51-7042',
    '51-8011',
    '51-8012',
    '51-8013',
    '51-8021',
    '51-8031',
    '51-8091',
    '51-8092',
    '51-8093',
    '51-8099',
    '51-9011',
    '51-9012',
    '51-9021',
    '51-9022',
    '51-9023',
    '51-9031',
    '51-9032',
    '51-9041',
    '51-9051',
    '51-9061',
    '51-9071',
    '51-9081',
    '51-9082',
    '51-9083',
    '51-9111',
    '51-9121',
    '51-9122',
    '51-9123',
    '51-9141',
    '51-9151',
    '51-9191',
    '51-9192',
    '51-9193',
    '51-9194',
    '51-9195',
    '51-9196',
    '51-9197',
    '51-9198',
    '51-9399',
    '53-1011',
    '53-1021',
    '53-1031',
    '53-2011',
    '53-2012',
    '53-2021',
    '53-2022',
    '53-2031',
    '53-3011',
    '53-3021',
    '53-3022',
    '53-3031',
    '53-3032',
    '53-3033',
    '53-3041',
    '53-4011',
    '53-4012',
    '53-4013',
    '53-4021',
    '53-4031',
    '53-4041',
    '53-5011',
    '53-5021',
    '53-5022',
    '53-5031',
    '53-6011',
    '53-6021',
    '53-6031',
    '53-6041',
    '53-6051',
    '53-6061',
    '53-7011',
    '53-7021',
    '53-7031',
    '53-7032',
    '53-7033',
    '53-7041',
    '53-7051',
    '53-7061',
    '53-7062',
    '53-7063',
    '53-7064',
    '53-7071',
    '53-7072',
    '53-7073',
    '53-7081',
    '53-7111',
    '53-7121'
]
