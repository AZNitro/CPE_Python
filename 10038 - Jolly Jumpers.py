while True:
    try:
        numbers = list(map(int,input().split()))
    except EOFError:
        break
    
    lst = []
    numbers.pop(0)
    for i in range(len(numbers)-1):
        lst.append(abs(numbers[i]-numbers[i+1]))
    
    
    ans = 0
    for j in range(len(lst),0,-1): 
        ans += j

    check = 0
    for k in range(len(lst)):
        check = check + lst[k]
    
    
    if ans == check:
        print('Jolly')
    else:
        print('Not jolly')


#解題邏輯:先處理字串，接下來將差距建立成list,計算答案與題目差距總和並比較，一致通過
#solution logic: First, solving split problem. Second, create a list which include each numbers difference. Third,count the answer and the question's gap then check. If the ans and the question's the same, it pass.