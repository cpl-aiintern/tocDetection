from xmlParsing import font_list
import os



def printing_fonts_and_size():
    xml_files = os.listdir('xmlData')
    for file in xml_files:
        print(file)
        font_family,font_sizes = font_list(file)
        print("Fonts\n",font_family)
        int_font_sizes = list(map(lambda x:int(x),font_sizes))
        int_font_sizes = list(set(int_font_sizes))
        int_font_sizes.sort()
        print("\nFont sizes\n",int_font_sizes)
        print("-"*100)

