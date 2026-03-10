def solve(str1, str2):
    ans = []

    for char in set(str1):
        if char in str2:
            ans += [char] * min(str1.count(char),  str2.count(char))
    

    return "".join(sorted(ans))

while True:
    try:
        str1 = input()
        str2 = input() 
        print(solve(str1,str2))
    except EOFError:
        break

#解題邏輯：其實這題就是思考如何計算，同時要知道抓駔最小
#solution logic:Find every unique character shared by both strings, keep the minimum number of times it appears in each, and return all those characters combined in alphabetical order.