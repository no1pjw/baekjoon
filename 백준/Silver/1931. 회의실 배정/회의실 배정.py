N = int(input())
time_list = []
present_start_time = 0
present_end_time = 0
count = 0
for a in range(N):
  time_list.append(list(map(int, input().split())))
time_list.sort(key = lambda x : (x[0], x[1]))
for b in range(N):
  if b == 0:
    count += 1
    present_start_time = time_list[b][0]
    present_end_time = time_list[b][1]
    continue
  else:
    if (time_list[b][0] >= present_start_time and time_list[b][1] <= present_end_time and time_list[b][0] != time_list[b][1]) or(time_list[b][0] == time_list[b][1] and (time_list[b][0] > present_start_time and time_list[b][1] < present_end_time)):
      present_start_time = time_list[b][0]
      present_end_time = time_list[b][1]
    elif time_list[b][0] == time_list[b][1]:
      count += 1
    elif time_list[b][0] >= present_end_time:
      count += 1
      present_start_time = time_list[b][0]
      present_end_time = time_list[b][1]
print(count)
  