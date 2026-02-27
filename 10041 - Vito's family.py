times = int(input())

for _ in range(times):
    numbers = list(map(int,input().split()))
    numbers.pop(0)
    numbers.sort()

    middle = len(numbers)/2
    middle = int(middle)

    total = 0

    for i in range(0,len(numbers)):
        temp = numbers[middle] - numbers[i]
        total = total + abs(temp)

    print(total)
    
    
    
    # 中文：輸出所有家庭成員到中位數住址的最小總距離。
    # English: Output the minimum total distance to the median address.

    #中文思考邏輯:此題其實是考計算中位數
    # 1)先設次數
    # 2)將題目輸入，並移除首位(無用於後續計算，因首位為親戚數)
    # 3)計算並找出中位數
    # 4)最後計算每戶到中位數距離，相加

    #Eng
    # This question is asking you how to count the middle number
    # 1)Set times
    # 2)Then, entering the questions and removing the first integer. It's useless for counting later.
    # 3)Calcluate and find the middel number
    # 4)Last, count each distance from relatives to the middle number. Then, count the total