cache = {1: 1}
while True:
    try:
        n = list(map(int,input().split()))
    except EOFError:
        break


    end = max(n[0],n[1])
    start = min(n[0],n[1])       #找出頭尾 #find where start and end.

    lst = []                     #一個list用於儲存，最後比較  #a list for storing each number cycles.

    for i in range(start, end+1):    #定義範圍 #define the scope
        cycles = 0                   #每個數字都從跑0回開始 #start from round 0
        temp = i                     #i用於定義現在是數字幾 temp用於跑演算法，目標計算最後數   # i is for numbers, temp is for algorithm, because i will change during the process, we need a temp for calculating. 
        
        while temp not in cache:      #檢查目前值是否有在字典裡，有查表到第24行，無進行演算法計算 # check the current value is in the dictionary or not, if it is and run line 24. if it's not, run algorithm.
            if temp % 2 !=0:
                temp = 3*temp +1
            else:
                temp = temp//2
            cycles = cycles+1
        total_cycles = cycles + cache[temp]       #計算總數 #count the total cycles
        
        
        
        cache[i] = total_cycles                    #補充字典 # add in dict
        lst.append(total_cycles)

    print(f'{n[0]} {n[1]} {max(lst)}')


#解題邏輯: 先處理演算法，再處理字典
#logic: algorithm first then add dict