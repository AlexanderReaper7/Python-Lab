import openpyxl
from pathlib import Path

def main():
	# get xls file from path
	#xlsx_file = Path(Path.home(), 'Documents', 'source.xlsx')
	xlsx_file = 'c:/Share/source.xlsx'
	# Load the workbook
	wb_obj = openpyxl.load_workbook(xlsx_file)

	# Read the active sheet:
	sheet = wb_obj.active

	for row in sheet.iter_rows():
		for cell in row:
			print(cell.value, end=" ")
		print()


main()
