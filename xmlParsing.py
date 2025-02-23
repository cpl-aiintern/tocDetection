from re import split
import xml.etree.ElementTree as ET
import math
import re
import os

tocKeyWords = ['contents','table of contents','chapters','sections']

def fontList():
    pass

def findTOCpage(filename):
    tree = ET.parse(os.path.join("xmlData",filename))
    root = tree.getroot()
    totalPages = len(root.findall('page'))
    pagesToBeConsidered = math.ceil(totalPages*30/100)
    for page in range(pagesToBeConsidered):
        pageElement = root[page]
        for box in pageElement.findall('textbox'):
            for line in box.findall('textline'):
                tempLine = r''
                for text in line.findall('text'):
                    if text.text != None:
                        tempLine+=text.text
                    else:
                        tempLine+=" "
                for keywords in tocKeyWords:
                    if re.search(keywords,tempLine.lower()) and len(tempLine)<30:
                        return page+1
    print("No Table of content found")

def font_list(filename):
    font_family = []
    font_size = []
    tree = ET.parse(os.path.join("xmlData",filename))
    root = tree.getroot()
    totalPages = len(root.findall('page'))
    pagesToBeConsidered = math.ceil(totalPages*30/100)
    for page in range(pagesToBeConsidered):
        pageElement = root[page]
        for box in pageElement.findall('textbox'):
            for line in box.findall('textline'):
                for text in line.findall('text'):
                    if 'font' in text.attrib and text.attrib['font'] not in font_family:
                        font_family.append(text.attrib['font'])
                    if 'size' in text.attrib and float(text.attrib['size']) not in font_size:
                        font_size.append(float(text.attrib['size']))
    return font_family,font_size

def main():
    xmlFiles = os.listdir('xmlData')

    if not os.path.exists('xmlData'):
        print("Please first convert the pdf data to XML")
        return
    
    for file in xmlFiles:
        page = findTOCpage(file)
        if page:
            print("TOC is located at %s in document %s"%(page,".".join(file.split(".")[:-1])))
        
if __name__ == '__main__':
    main()
    