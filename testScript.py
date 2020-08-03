from xmlParsing import font_list
import os

xml_files = os.listdir('xmlData')

for file in xml_files:
    font_list(file)