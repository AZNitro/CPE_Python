while True:
    try:
        numbers = list(map(int, input().split()))
        ans = abs(numbers[0]-numbers[1])
        print(ans)

    except EOFError:
        break

    #這題其實沒啥難度，只是計算兩數差距
    #It's very easy. Just count the difference from two numbers