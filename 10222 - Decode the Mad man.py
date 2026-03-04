def solve(text):
    original = "234567890-=ertyuiop[]\\dfghjkl;'cvbnm,./"

    translated = "`1234567890qwertyuiop[asdfghjklzxcvbnm,"

    decode_table = str.maketrans(original, translated)

    ans = text.translate(decode_table)

    print(ans)


while True:
    try:
        n = input()
    except EOFError:
        break

    solve(n)

#解題邏輯：1.建立好table對照 2.採用str.maketrans 和 translate 兩大關鍵
#solution logic: 1. create a table for decoding 2. implement with str.maketrans and translate these two key points.
