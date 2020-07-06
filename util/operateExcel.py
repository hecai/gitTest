import xlrd


def getExcelValue(bookName, sheetName):
    book = xlrd.open_workbook(f'../cases/{bookName}.xlsx')
    print(book.sheet_names())
    sheet = book.sheet_by_name(sheetName)
    caseNos = sheet.col_values(0)
    caseBefores = sheet.col_values(1)
    cases = sheet.col_values(2)
    caseResults = sheet.col_values(3)
    values = []
    print(caseNos[1])
    for i in range(1,len(sheet.col_values(0))):
        dic = {'no': caseNos[i], 'caseBefores': caseBefores[i], 'cases': cases[i], 'caseResults': caseResults[i]}
        values.append(dic)
    return values