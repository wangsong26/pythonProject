def member(path):
    file_member_list = []
    file_member_list1=[]

    with open(path, 'r', encoding='utf-8') as file_member:
        for line in file_member:
            file_member_list.append(line)

    print(file_member_list)
    for line in file_member_list:
        file_member_list1.append(line.split(','))

    return file_member_list1

print(member('member.csv'))
