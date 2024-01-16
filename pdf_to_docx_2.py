# Convert PDF to DOCX, generating image output types in the DOCX file instead of text.

from pdf2docx import Converter
#import pdf2docx

pdf_name = str(input("Enter the filename of the .pdf you want to convert to .docx = " ))
pdf_file = (pdf_name+'.pdf')
docx_file = 'pdf_convert2_doc.docx'

convert_file = Converter(pdf_file)
convert_file.convert(docx_file)
convert_file.close()

print('!!!!!Done!!!!!')

#End