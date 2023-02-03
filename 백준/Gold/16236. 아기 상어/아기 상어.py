square_num = int(input())
global fish_list, fish_size, fish_eaten, total_time, all_list, return_list
fish_list = []
fish_size = 2
fish_eaten = 0
time = 0
total_time = 0
x = 0
y = 0
all_list = []
return_list = []
for a in range(square_num):
    fish_list.append(list(map(int, input().split())))
def next_move(x, y): #return next_move_list
    global all_list, return_list, fish_list, fish_size
    check_num = 0
    while(check_num < 1):
        temp_list = []
        for a in return_list:
            temp_temp_list = [[a[0] - 1, a[1]], [a[0], a[1] - 1], [a[0], a[1] + 1], [a[0] + 1, a[1]]]
            for b in temp_temp_list:
                try:
                    if b not in temp_list and b[0] >= 0 and b[1] >= 0 and (b[0] != x or b[1] != y) and b not in all_list and fish_list[b[0]][b[1]] <= fish_size:
                        temp_list.append(b)
                        all_list.append(b)
                except IndexError:
                    pass
        check_num += 1
        return_list = temp_list
        return_list.sort(key = lambda x : (x[0], x[1]))
    return return_list
def find_fish(x, y):
    time = 0
    global total_time, fish_eaten, fish_size, all_list, return_list
    not_find = True
    if fish_eaten == fish_size:
        fish_eaten = 0
        fish_size += 1
    while(not_find):
        time += 1
        next_move_list = next_move(x, y)
        if next_move_list == []:
            break
        for a in next_move_list:
            if 0 < fish_list[a[0]][a[1]] < fish_size:
                not_find = False
                fish_eaten += 1
                fish_list[a[0]][a[1]] = 0
                break
    if not_find:
        return
    all_list = []
    return_list = [[a[0], a[1]]]
    total_time += time
    find_fish(a[0], a[1])
for a in range(square_num):
    for b in range(square_num):
        if fish_list[a][b] == 9: #find first start point
            x = a
            y = b
            break
    if fish_list[a][b] == 9:
        break
fish_list[x][y] = 0
return_list = [[x, y]]
find_fish(x, y)
print(total_time)