def summing(n):
    
    total = 0
    
    for i in range(len(str(n))):
        n = str(n)
        total =  total + int(n[i])
    
    return str(total)


#main program

while True:
    try:
        n = input()
    except EOFError:
        break

    if n =='0':
        break

    while len(n) > 1:
        n = summing(n)
    

    print(n)

#解題邏輯:先想好演算法，透過字元轉換整數計算，在轉換回字元給main program測試長度
#solution logic: Implementing Algorithm first. Then, calculating from integer which transfer from string. Finally, transfering back to main program for testing length.