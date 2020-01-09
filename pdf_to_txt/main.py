from multiprocessing import Process, Queue, Pool
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import os, time

def get_file_names(path):
    file_list = os.listdir(path)
    return file_list

def get_file_paths( input_path, file_names, replacer):
    if(replacer == 'txt'):
        x = []
        for i, v in enumerate(file_names):
            x.insert(i, input_path + v.replace(".pdf", ".txt"))
        return x
    else:
        x = []
        for i, v in enumerate(file_names):
            x.insert(i, input_path + v)
        return x

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text

def multiprocessing_work(paths):
    return list(Pool(processes= 4).map(convert_pdf_to_txt, paths))

def save_text_files(output_path, path_list, string_list):
    for i, v in enumerate(path_list):
        text_file = open(v, "w")
        text_file.write(string_list[i])
        text_file.close()

def main(input_path, output_path):
# def main():
    # start_time = time.time()
    # input_path = "./files/"
    # output_path = "./output/"
    file_name_list = get_file_names(input_path)
    file_input_path_list = get_file_paths(input_path, file_name_list, "input")
    # file_string_list = list( map( convert_pdf_to_txt, file_input_path_list ) )
    file_string_list = multiprocessing_work(file_input_path_list)
    file_output_path_list = get_file_paths(output_path, file_name_list, "txt")
    save_text_files(output_path, file_output_path_list, file_string_list)
    # print("--- %s seconds ---" % (time.time() - start_time))

# main()
