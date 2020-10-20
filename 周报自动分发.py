from datetime import datetime
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

def write(DEPT,EMAIL,DATE,CONTECT,NAME):
    with open(f'./report/{NAME}', 'w') as f:
        f.write(f'DEPT:<{DEPT}')
        f.write(f'NAME:<{NAME}>\n')
        f.write(f'EMAIL:<{EMAIL}>\n')
        f.write(f'DATE:<{DATE}>\n')
        f.write(f'CONTECT:<{CONTECT}>\n')

def auto_write():
    for i in member('member.csv'):
        name = i[1] + datetime.now().strftime('%y%m%d_%H%M%S') + '.txt'
        write(i[3],i[2],datetime.now(),NAME=name,CONTECT='')

auto_write()





