import xml.etree.ElementTree as ET
import math
import re

tocKeyWords = ['contents','table of contents','chapters','sections']

def main():
    tree = ET.parse("xmlData/Response to Feedback Received on the Proposed Framework for Variable Capital Companies Part 3.xml")
    root = tree.getroot()
    found = False
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
                    if re.search(keywords,tempLine.lower()):
                        print("Table of contents is located at",page+1)
                        found = True
                        break
                if found: break
            if found: break
        if found: break
        
if __name__ == '__main__':
    main()
    