import sys
import pandas as pd
from openpyxl import load_workbook, Workbook

def main():
    clean_regional_file('oak$OccProj.xlsx')
    clean_regional_file('sanf$OccProj.xlsx')
    clean_regional_file('sanrf$OccProj.xlsx')

# clean employment data
# msa_employment_df = pd.read_excel('raw_data_files/oesm18ma/MSA_M2018_dl.xlsx', sheet_name='MSA_dl')
# msa_filtered = msa_employment_df.query('AREA_NAME == "San Francisco-Oakland-Hayward, CA" and TOT_EMP != "**"')[['OCC_CODE', 'TOT_EMP', 'OCC_TITLE']]
# msa_filtered.to_excel('clean_data_files/sf_employment.xlsx', sheet_name='Sheet1')
# print(msa_filtered)
# print("employment data written to sf_employment.xlsx")

# clean local projection data excel files
def clean_regional_file(filename):
    raw_filename = 'raw_data_files/alltb6/' + filename
    clean_filename = 'clean_data_files/cleaned_' + filename

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

    for row, cellObj in enumerate(list(clean_ws.columns)[1]):
        if row != 0:
            try:
                cellObj.value = (float(cellObj.value) + 1) ** 0.1 - 1
            except TypeError:
                continue

    clean_ws['A1'] = 'SOC_CODE'
    clean_ws['B1'] = 'ANNUAL_CHANGE'

    clean_wb.save(filename=clean_filename)
    print('cleaned ' + filename)


# oakland (alameda and contra costa)

if __name__ == "__main__":
    main()
