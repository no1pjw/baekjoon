import sys
from collections import deque
input = sys.stdin.readline
M, N = map(int, input().split())
one_list = []
minus_list = []
for a in range(N):
    list1 = list(map(int, input().split()))
    for b in range(len(list1)):
        if list1[b] == 1:
            one_list.append(a * M  + b)
        elif list1[b] == -1:
            minus_list.append(a * M + b)
        else:
            pass
def Tomato(one_list, minus_list):
    visited = [False]*1000001
    queue = deque([])
    len1 = len(one_list)
    len2 = 0
    len3 = 0
    count = 0
    one_count = 0
    if one_list == []:
        return -1
    for a in one_list:
        queue.append(a)
        visited[a] = True
    for b in minus_list:
        visited[b] = True
    while queue:
        if len2 == len1:
            count += 1
            len1 = len3
            len2 = 0
            len3 = 0
        node = queue.popleft()
        list1 = [node -1, node + 1, node - M, node + M]
        for c in list1:
            if c >= M * N or c < 0 or visited[c] or (c % M == 0 and node == c - 1) or (c % M == M - 1 and node == c + 1):
                pass
            else:
                queue.append(c)
                visited[c] = True
                len3 += 1
                one_count += 1
        len2 += 1
    if one_count + len(one_list) + len(minus_list) != M * N:
        return -1                                                                                                                      
    return count
print(Tomato(one_list, minus_list))
