# Convert a PDF to DOCX, extracting plain text
# The PDF file should only contain text and tables, not images

import pdfplumber

pdf_name = str(input("Enter the filename of the .pdf you want to convert to .docx = " ))
pdf_file = (pdf_name+'.pdf')
with pdfplumber.open(pdf_file) as pdf:
    text = ""
    for page in pdf.pages:
        text += page.extract_text()

with open('pdf_to_text.txt', 'w') as file:
    #print(text)
    file.write(text)

print('!!!!!Done!!!!!')

#------------------------------------------#
#End

'''

#######################################
# The same output


import pdfplumber

pdf_name = str(input("Enter the filename of the .pdf you want to convert to .docx = " ))
pdf_file = (pdf_name+'.pdf')
pdf_file_reader = pdfplumber.open(pdf_file)

text = ""

for page in pdf_file_reader.pages:
    text += page.extract_text()

pdf_file_reader.close()

with open('pdf_to_text.txt', 'w') as file:
    #print(text)
    file.write(text)

print('!!!!!Done!!!!!')

#######################################
# The same output

import PyPDF3

pdf_name = str(input("Enter the filename of the .pdf you want to convert to .docx = " ))
pdf_file = (pdf_name+'.pdf')
pdf_file_reader = open(pdf_file, 'rb')

pdf_reader = PyPDF3.PdfFileReader(pdf_file_reader)

pdf_reader.numPages

page_obj = pdf_reader.getPage(0)
output_txt = page_obj.extractText()
pdf_file_reader.close()

with open('pdf_to_text.txt', 'w') as file:
    #print(output_txt)
    file.write(output_txt)

print('!!!!!Done!!!!!')

#######################################
# The same output

import PyPDF3

pdf_name = str(input("Enter the filename of the .pdf you want to convert to .docx = " ))
pdf_file = (pdf_name+'.pdf')
pdf_file_reader = open(pdf_file, 'rb')

pdf_reader = PyPDF3.PdfFileReader(pdf_file_reader)

text = ""

for page_num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(page_num)
    text += page.extractText()

pdf_file_reader.close()

with open('pdf_to_text.txt', 'w') as file:
    #print(text)
    file.write(text)

print('!!!!!Done!!!!!')

'''