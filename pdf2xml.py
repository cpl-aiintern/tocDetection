from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter
from pdfminer.layout import LAParams

import os
from io import StringIO

def pdf_to_xml(pdfpath):
    rsrcmgr = PDFResourceManager()
    sio = StringIO()
    laparams = LAParams()
    device = XMLConverter(rsrcmgr, sio, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    fp = open(pdfpath, 'rb')
    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
    fp.close()

    text = sio.getvalue()

    device.close()
    sio.close()

    return text

def main():
    pdfFiles = os.listdir('pdfData')

    if not os.path.exists('xmlData'):
        os.mkdir('xmlData')

    for file in pdfFiles:
        text = pdf_to_xml(os.path.join('pdfData',file))
        xml_file_writer = open(os.path.join('xmlData',".".join(file.split(".")[:-1])+'.xml'),'w')
        xml_file_writer.write(text)
        xml_file_writer.write("</pages>")
        xml_file_writer.close()

if __name__ == '__main__':
    main()
