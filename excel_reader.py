import openpyxl
def read_excel_data(filepath, sheet_name="Sheet1"):
   workbook  = openpyxl.load_workbook(filepath)
   sheet     = workbook[sheet_name]
   test_data = []
   for row in sheet.iter_rows(min_row=2, values_only=True):
       username        = row[0] if row[0] else ""
       password        = row[1] if row[1] else ""
       expected_result = row[2] if row[2] else ""
       test_data.append((username, password, expected_result))
   return test_data