while True:
    try:
        n = int(input())
    except EOFError:
        break
    
    if n % 11 !=0:
        ans = 0
    else:
        ans = 1
    
    if ans == 1:
        print(f'{n} is a multiple of 11.')
    else:
        print(f'{n} is not a multiple of 11')

    
    #解題邏輯，基本上這題直接數字除11就可
    #Just divided by 11 is enough.