from tabula import read_pdf
import PyPDF2
import re

# Ler tabelas:
#   - Depois fazer o tratamento usando pandas.
lista = read_pdf('Schedule.pdf', pages='all')
print(len(lista))

# print(lista.iloc[0][0])

for tabela in lista:
    # print(type(tabela))
    print(tabela.iloc[0])

# Transformar conteúdo em uma strings:
#   - Depois fazer o tratamento usando expressões regulares.
# pdf_file = open('Schedule.pdf', 'rb')
# read_pdf = PyPDF2.PdfFileReader(pdf_file)

# page = read_pdf.getPage(0)
# page_content = page.extractText()
# parsed = ''.join(page_content)

# print(parsed)