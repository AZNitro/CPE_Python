while True:
    try:
        numbers= list(map(int,input().split()))
    except EOFError:
        break

    numbers.pop(0)
    
    check = 0
    for i in range(len(numbers)-1):
        check = check + abs(numbers[i]-numbers[i+1])
    
    ans = 0
    for j in range(len(numbers)-1,0,-1):
        ans = ans + j
    
    if check == ans:
        print('Jolly')
    else:
        print("Not jolly")


#解題邏輯：先處理數字字串，接下來拿掉第一個（無用），計算各個數字之間之差並相加，然後計算標準答案，最後比較。
#solution logic: First,process the numeric string, then remove the first element(useless). Calculate the differences consecutive numbers and sum them up. Finally, calculate the standard answer and compare the results.

