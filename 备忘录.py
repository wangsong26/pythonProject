memo = []
sum=0
while True:

    record=input('请输入事件')
    time,event,*_ =record.split('点')
    memo.append({'time':time,'event':event})
    sum+=1
    print(f'共{sum}个待办事项')
    s=input('是否继续，y/n')
    if s=='y':
        continue
    else:
        break
print(memo)
for index, item in enumerate(memo):
    print(f'事件{index+1}----{item["time"]} 点 {item["event"]}')










