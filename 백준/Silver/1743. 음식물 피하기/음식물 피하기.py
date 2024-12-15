import sys
sys.setrecursionlimit(100000)
N, M, K = map(int, input().split())
global visited_list, trash_count
visited_list = []
for a in range(N):
  temp_list = []
  for b in range(M):
    temp_list.append(True)
  visited_list.append(temp_list)
target_list = []
trash_count = 0
count_list = []
for a in range(K):
  x, y = map(int, input().split())
  target_list.append([x -1, y -1])
  visited_list[x -1][y- 1] = False
def find_biggest_trash(x, y):
  global visited_list, trash_count
  if x < 0 or y < 0 :
    pass
  else:
    try:
      if not(visited_list[x][y]):
        trash_count += 1
        visited_list[x][y] = True
        move_list = [[x -1 , y], [x + 1, y], [x, y -1], [x, y + 1]]
        for a in move_list:
          find_biggest_trash(a[0], a[1])
      else:
        pass
    except IndexError:
      pass
for b in target_list:
  count_list.append(trash_count)
  trash_count = 0
  if visited_list[b[0]][b[1]]:
    continue
  find_biggest_trash(b[0], b[1])
count_list.append(trash_count)
print(max(count_list))
