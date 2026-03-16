times = 0
while True:
    try:
        text = input()
    except EOFError:
        break

    
    for i in text:
        if i == '"':
            times += 1
            if times % 2 == 1:
                print("``",end="")
            else:
                print("''",end="")
        else:
            print(i,end="")
    print('')

#解題思路：讀取整字串後，一字一字讀取輸出，計算times次數，然後判斷是第幾次出現，決定輸出內容。
#solution logic:First, read the whole string, output the words one by one. Then, counting the times and checking times variables to decide what the final text is.