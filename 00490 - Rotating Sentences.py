from itertools import zip_longest

import sys

lines = sys.stdin.read().splitlines()

for chars in zip_longest(*reversed(lines), fillvalue=" "):
    print("".join(chars))

#解題邏輯: 放輕鬆，採用zip_longest解決配對問題，同時reversed轉90度
#solution logic: take easy. Just use zip_longest this function