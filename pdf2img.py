import pdf2image
import os

def pdf2img(filepath):
    filename = ".".join(filepath.split(".")[:-1])
    
    if not os.path.exists('imageData'):
        os.mkdir('imageData')
    
    outputpath = os.path.join('imageData',filename)
    os.mkdir(outputpath) if not os.path.exists(outputpath) else print("Folder already exists")

    pdf2image.convert_from_path(os.path.join('pdfData',filepath),output_folder=outputpath,fmt="tiff")


def main():
    pdf_file_list = os.listdir('pdfData')
    for file in pdf_file_list:
        print("Converting %s to images"%(file))
        pdf2img(file)
        print("converted\n")

if __name__ == '__main__':
    main()