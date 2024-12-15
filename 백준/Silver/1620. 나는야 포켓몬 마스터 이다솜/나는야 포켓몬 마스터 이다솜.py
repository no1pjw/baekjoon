import sys
N, M = map(int, sys.stdin.readline().split())
list1 = []
for a in range(N):
    str1 = sys.stdin.readline().rstrip()
    list1.append(str1)
for b in range(M):
    str2 = sys.stdin.readline().rstrip()
    if str2.isdigit():
        print(list1[int(str2)-1])
    else:
        print(list1.index(str2) + 1)