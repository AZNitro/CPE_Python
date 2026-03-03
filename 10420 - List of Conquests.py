dict = {}
while True:
    try:
        times= int(input())
    except EOFError:
        break
    
    for i in range(times):

        items = list(map(str, input().split()))
        
        if items[0] in dict:
            dict[items[0]] += 1
        else:
            dict[items[0]] = 1
    
    for country, value in sorted(dict.items()):
        print(f'{country} {value}')

#解題邏輯: 不用管人名，只用紀錄國家名稱
#solution logic: just count countries appear times.