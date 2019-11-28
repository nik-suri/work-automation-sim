import sys
import pandas as pd
from openpyxl import load_workbook, Workbook

RAW_REGIONAL_PREFIX = 'raw_data_files/alltb6/'
CLEAN_REGIONAL_PREFIX = 'clean_data_files/cleaned_'

def main():
    clean_regional_proj_file('oak$OccProj.xlsx')
    clean_regional_proj_file('sanf$OccProj.xlsx')
    clean_regional_proj_file('sanrf$OccProj.xlsx')

    aggregate_proj('oak$OccProj.xlsx', 'sanf$OccProj.xlsx', 'sanrf$OccProj.xlsx')

    # clean employment data to SF employment
    msa_employment_df = pd.read_excel('raw_data_files/oesm18ma/MSA_M2018_dl.xlsx', sheet_name='MSA_dl')
    msa_filtered = msa_employment_df.query('AREA_NAME == "San Francisco-Oakland-Hayward, CA" and TOT_EMP != "**"')[['OCC_CODE', 'TOT_EMP', 'OCC_TITLE']]
    msa_filtered.to_excel(
        'clean_data_files/sf_employment.xlsx',
        sheet_name='Sheet1',
        index=False
    )
    print("employment data written to sf_employment.xlsx")


# aggregate granular county projections into a mean metropolitan projection
def aggregate_proj(*args):
    aggregate_df = pd.read_excel(CLEAN_REGIONAL_PREFIX + args[0])

    for i in range(1, len(args)):
        to_add_df = pd.read_excel(CLEAN_REGIONAL_PREFIX + args[i])
        aggregate_df = aggregate_df.merge(to_add_df, on='SOC_CODE')
        aggregate_df['ANNUAL_CHANGE'] = aggregate_df['ANNUAL_CHANGE_x'] + aggregate_df['ANNUAL_CHANGE_y']
        del aggregate_df['ANNUAL_CHANGE_x']
        del aggregate_df['ANNUAL_CHANGE_y']

    aggregate_df['ANNUAL_MEAN_CHANGE'] = aggregate_df['ANNUAL_CHANGE'].div(len(args))
    del aggregate_df['ANNUAL_CHANGE']
    aggregate_df.to_excel(
        'clean_data_files/sf_employment_projections.xlsx',
        sheet_name='Sheet1',
        index=False
    )

    print('aggregated ' + str(args))


# clean local projection data excel files
def clean_regional_proj_file(filename):
    raw_filename = RAW_REGIONAL_PREFIX + filename
    clean_filename = CLEAN_REGIONAL_PREFIX + filename

    raw_wb = load_workbook(filename=raw_filename)
    clean_wb = Workbook()

    raw_ws = raw_wb.active
    clean_ws = clean_wb.active
    clean_ws.title = 'Occupational_Cleaned'
    for i in range(4, raw_ws.max_row):
        for j in range(1, raw_ws.max_column):
            clean_ws.cell(row=i - 3,column=j).value = raw_ws.cell(row=i,column=j).value

    clean_ws.delete_cols(1, 1)
    clean_ws.delete_cols(2, 4)
    clean_ws.delete_cols(3, 8)
    clean_ws.delete_rows(2, 1)

    # should delete all rows which are meaningless at the end
    empty_rows = 18
    clean_ws.delete_rows(clean_ws.max_row - empty_rows, empty_rows + 1)

    for row, cellObj in enumerate(list(clean_ws.columns)[1]):
        if row != 0:
            cellObj.value = (float(cellObj.value) + 1) ** 0.1 - 1

    clean_ws['A1'] = 'SOC_CODE'
    clean_ws['B1'] = 'ANNUAL_CHANGE'

    clean_wb.save(filename=clean_filename)
    print('cleaned ' + filename)


if __name__ == "__main__":
    main()
