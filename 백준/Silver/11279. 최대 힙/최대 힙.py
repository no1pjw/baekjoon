import sys
import heapq

numbers = int(input())
heap = []

#Max Heap
for _ in range(numbers):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, (-num, num))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)