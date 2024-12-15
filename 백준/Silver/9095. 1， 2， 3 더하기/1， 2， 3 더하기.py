import sys
input = sys.stdin.readline
num1 = int(input())
dp = [[] for _ in range(11)]
dp[1] = ['1']
dp[2] = ['2', '1 + 1']
dp[3] = ['2 + 1', '1 + 2', '1 + 1 + 1', '3']
for a in range(num1):
    num = int(input())
    for b in range(4, num + 1):
        if dp[b] != []:
            continue
        for c in range(b - 3, b):
            for d in dp[c]:
                dp[b].append(d + f'+ {b - c}')
    print(len(dp[num]))

