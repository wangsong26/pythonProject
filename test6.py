import os
import fnmatch
from openpyxl import load_workbook
import openpyxl
def return_object(path):
    all_file = fnmatch.filter(os.listdir(path), '*.txt')
    print(all_file)
    for file in all_file:
        print(file)
        lst = []
        with open(f'./report/{file}', 'r', encoding='utf-8') as f:
            for line in f.readlines():
                line = line.strip()
                lst.append(line)
        print(f'name{file}--- {lst}')
return_object('./report')