def print_bangla(n):
    
    if n >= 10000000:
        front_part = n // 10000000
        print_bangla(front_part)
        print(" kuti", end="")
        n = n % 10000000
    
    if n >=100000:
        front_part = n // 100000
        print_bangla(front_part)
        print(" lakh",end="")
        n = n % 100000
    
    if n >= 1000:
        front_part = n // 1000
        print_bangla(front_part)
        print(" hajar", end="")
        n = n % 1000
    
    if n >=100:
        front_part = n // 100
        print_bangla(front_part)
        print(" shata",end="")
        n = n % 100
    if n >0:
        print(f' {n}',end="")
    
case_num = 1
while True:
    try:
        n = int(input())
    except EOFError:
        break

    print(f'{case_num:>4}.', end="")

    if n == 0:
        print(f' {0}')
    else:
        print_bangla(n)
        print()

    case_num += 1

#解題邏輯：顯處理最大刀，10000000的部份，接下來透過遞迴處理，分前後部份，直到切到底，須注意的是排版，需要空四格，以及各單位前面空格
#Solution logic: Start by processing the largest unit (the 10,000,000 part). Next, use recursion to split the number into a quotient (front) and a remainder (back), repeating this process until the base case is reached. For formatting, note that the case number requires a 4-character right alignment, and there must be a leading space before every unit."