#方法一:递归
# def fun(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     if n>1:
#         return fun(n-1)+fun(n-2)
# print(list(map(fun,range(11))))

#方法二:循环
sum1=0
lst=[]
for i in range(11):
    if i==0:
        sum1=0
        lst.append(sum1)
    elif i==1:
        sum1=1
        lst.append(sum1)
    else:
        sum1=lst[i-2] + lst[i-1]
        lst.append(sum1)
print(lst) 

