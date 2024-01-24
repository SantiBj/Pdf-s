from PyPDF2 import PdfReader
import re
import openpyxl

# funcion sacar datos pdf

def dataPdf(pdf)->dict:
    pdfName:str = pdf.name
    
    with pdf.open('rb') as pdfTemporal:
        pdfReader = PdfReader(pdfTemporal)
             
        records:list[tuple] = []

        for numberPage in range(len(pdfReader.pages)):
            text = pdfReader.pages[numberPage].extract_text().split('\n')
            for line in text:
                if(line[0] == '9'):
                    isbn = re.search(r'^[\d-]+',line).group()
                    title = re.search(r'[A-za-zÑñ][\w,ñÑ?\s]+[A-Za-z?]',line).group()
                    lineEdit = line.split(title)[1].strip().split(" ")
                    quantity = lineEdit[0]
                    empty = lineEdit[1]
                    importe = lineEdit[2]
                    records = [*records,(isbn,title,quantity,empty,importe)]

    return {
        "records":records,
        "nameFile":pdfName
    }

# funcion imprimir datos excel

def printDataInExcel(records:list[tuple],nameFile:str):
    book = openpyxl.load_workbook("plantilla.xlsx")
    sheet = book.worksheets[0]

    startRow = 2
    startCol = 1

    for rowIndex, rowData in enumerate(records, start=startRow):
            for colIndex, value in enumerate(rowData, start=startCol):
                sheet.cell(row=rowIndex, column=colIndex, value=value)

   
    book.save(nameFile)
    return book

