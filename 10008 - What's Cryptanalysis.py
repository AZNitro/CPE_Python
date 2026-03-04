dict = {}

def sorting_rules(items):
    letter = items[0]
    counts = items[1]
    return (-counts, letter)
while True:
    try:
        times = int(input())
    except EOFError:
        break

    for _ in range(times):
        str = input()
        
        for char in str:
            if char.isalpha():
                char = char.upper()

                if char in dict:
                    dict[char] += 1
                else:
                    dict[char] = 1

    for alpha,value in sorted(dict.items(), key=sorting_rules):
        print(f'{alpha} {value}')
        

#解題邏輯： 拆開字母，一個一個檢查，轉換為大寫，檢查有無在字典，最後撰寫分類規則
#Split the letters, check one by one, convert to uppercase, check if in the dictionary, finally, write the sorting rules.