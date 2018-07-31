from xlrd import open_workbook

def read_one():
    with open("2.log", "r") as ins:
        for line in ins:
            yield line.replace('\n', '')

def read_two():
    with open("1.log", "r") as ins:
        for line in ins:
            yield line.replace('\n', '')

def read_three():
    wb = open_workbook('1.xlsx')
    for sheet in wb.sheets():
        number_of_rows = sheet.nrows
        for row in range(0, number_of_rows):
            yield str(sheet.cell(row, 0).value)

def read_four():
    wb = open_workbook('2.xlsx')
    for sheet in wb.sheets():
        number_of_rows = sheet.nrows
        for row in range(0, number_of_rows):
            yield str(sheet.cell(row, 0).value)


p = [n for n in read_three() if n in read_four()]
print(p)

