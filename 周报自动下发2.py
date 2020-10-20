from datetime import datetime
import os
def member(path):
    file_member_list=[]
    file_member_list1=[]
    with open(path, 'r', encoding='utf-8') as file_member:
        for line in file_member:
            line=line.strip()  #去掉空格或者回车
            file_member_list.append(line)
    for line in file_member_list:
        file_member_list1.append(line.split(','))
    return file_member_list1

def template(path):
    template_file=''
    with open(path, 'r', encoding='utf-8') as f:
        template_fil=f.read()

    return template_file


def write(DEPT,EMAIL,DATE,NAME,NAME_file,template_file=''):
    template_file = template_file.replace('<DEPT>', DEPT)
    template_file = template_file.replace('<NAME>', NAME)
    template_file = template_file.replace('<EMAIL>', EMAIL)
    template_file = template_file.replace('<YYYYMMDD>', DATE)

    with open(f'./report/{NAME_file}','w',encoding='UTF-8')as f:
        f.write(template_file)
    print(template_file)

def auto_write():
    template_file=template('template.txt')
    for i in member('member.csv'):
        name = i[1] + datetime.now().strftime('%y%m%d_%H%M%S') + '.txt'
        dt = datetime.now().strftime('%Y%m%d_%H%M%S')
        write(DEPT=i[3],EMAIL=i[2],DATE=dt,NAME=i[1],NAME_file=name, template_file=template_file)

auto_write()




