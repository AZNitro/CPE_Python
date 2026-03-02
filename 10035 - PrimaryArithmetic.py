while True:
    try:    
        numbers = input().split()
        if numbers[0] == '0' and numbers[1] == '0':
            break
    except EOFError:
        break
    
    
    max_len = max(len(numbers[0]), len(numbers[1]))

    s1 = numbers[0].zfill(max_len) #002
    s2 = numbers[1].zfill(max_len) #100
    

    carry = 0
    ans = 0
    for i in range(max_len-1, -1, -1):
        temp = int(s1[i])+int(s2[i])+ carry
        if temp > 9:
            carry =1
            ans = ans+1
        else:
            carry = 0
    

    if ans == 0:
        print(f'No carry operation.')
    elif ans == 1:
        print(f'{ans} carry operation.')
    else:
        print(f'{ans} carry operations.')  



    #解題思考: 先將數字補齊，後套用加法邏輯， 從後面數到前面
    #logic: fill two numbers and use add logic from the end to the beginning.