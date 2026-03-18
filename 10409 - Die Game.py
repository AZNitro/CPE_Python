while True:
    times = int(input())

    if times == 0:
        break
    
    lst = []
    for i in range(times):
        cmd = input()
        lst.append(cmd)


    top = 1
    north = 2
    west =3
    for action in lst:

        
        if action == 'north':
            top,north,west = 7-north , top ,west
        elif action == 'south':
            top,north,west = north, 7-top ,west
        elif action == 'west':
            top,north,west = 7-west ,north, top
        elif action == 'east':
            top, north, west = west ,north, 7-top 
    
    print(top)

#解題邏輯:這題真的花盡了我的力量，其實就只是想清楚骰子數字會如何運作，難在一開始，想通後就簡單了。
#solution logic: What a terrible question it is!! Just need to understand how numbers will change on die. 