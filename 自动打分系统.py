
# for i in range(3):
#     record=int(input(f'第{i+1}个裁判打分：'))
#     list1.append(record)
#使用列表生成式
list1=[int(input(f'第{i+1}个裁判打分：')) for i in range(3)]

# 方法1：使用列表切片
# list1.sort()
# print(f'当前评分:{list1},共{len(list1)}个')
# print(f'去掉一个最高分{list1[9]},去掉一个最低分{list1[0]},平均得分是{sum(list1[1:9])/8}')

# 方法二：使用max min()
# print(f'去掉一个最高分{max(list1)},去掉一个最低分{min(list1)},平均得分是{(sum(list1)-min(list1)-max(list1))/8}')

#方法三:
list1.sort()
min_v,*mid_vaule,max_v=list1
print(list1)
print(min_v)
print(mid_vaule)
print(max_v)