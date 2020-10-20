from functools import reduce
# 方法1：使用函数嵌套函数
# def hannum2int(s):
#     def changetolst(y):
#         dict1 = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9}
#         return dict1[y]
#
#     def add(i, j):
#         return i * 10 + j
#     return reduce(add, list(map(changetolst, s)))
#
# print(hannum2int('二四六八'))
# 方法2：使用lamdba
# dict1 = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '零': 0}

dict1={ i:idx for idx, i in enumerate('零一二三四五六七八九')}
def hannum2int(s):

    return reduce(lambda i,j:i*10+j, list(map((lambda i:dict1[i]), s)))
print(hannum2int('一三五七九'))