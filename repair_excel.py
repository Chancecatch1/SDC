import glob
import openpyxl

# Load all Excel files in the specified directory
file_path = './Personal_Rent_files/*.xlsx'
all_files = glob.glob(file_path)

# Loop through each file and repair it
for file in all_files:
    wb = openpyxl.load_workbook(file)

    # Check for and repair any corruption in the file
    if not wb.read_only:
        try:
            wb.save(file)
        except openpyxl.utils.exceptions.ReadOnlyWorkbookException:
            wb = openpyxl.load_workbook(file, read_only=True)

    # Save the repaired file with a new name
    repaired_file = file.replace('.xlsx', '_repaired.xlsx')
    wb.save(repaired_file)