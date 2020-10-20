import random
result = random.randint(1,200)

count=1
while count<=10:
    number=int(input('请输入200以内的整数'))
    if number==result:
        print(f'猜对了，随机数就是{number},一共尝试{count}次')
        break
    else:
        print(f'猜{"大" if number > result else "小"}了，请重新输入，剩余次数{10-count}')
        count+=1
