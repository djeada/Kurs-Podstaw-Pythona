import os
import sys
import comtypes.client

def get_files(dirname):
    all_files = []
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            if filename[-4:] == 'docx':
                all_files.append(os.path.join(root, filename))
    return all_files

def get_out_name(input_name):            
    return input_name[:len(input_name)-4] + 'pdf'

files = get_files(os.getcwd())

for file in files:
    word = comtypes.client.CreateObject('Word.Application')
    doc = word.Documents.Open(file)
    doc.SaveAs(get_out_name(file), FileFormat=17)
    doc.Close()
    word.Quit()
