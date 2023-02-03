square_num = int(input())
global paper_list
paper_list = [0, 0, 0]
total_list = []
for a in range(square_num):
    total_list.append(list(map(int, input().split())))
def check_is_same(list):
    previous_num = -2
    for a in list: # checking is paper ?
        for b in a:
            if previous_num != -2 and previous_num != b:
                return False
            previous_num = b 
    return True
def paper(list, current_number):
    global paper_list
    if current_number == 1 or check_is_same(list):
        paper_list[list[0][0] + 1] += 1
        return
    for c in range(0, current_number, current_number // 3):
        for d in range(0, current_number, current_number // 3):
            temp_list = []
            for e in range(0, current_number // 3):
                temp_list.append(list[c + e][d: d+ current_number // 3])
            if check_is_same(temp_list):
                paper_list[temp_list[0][0] + 1]+= 1
            else:
                paper(temp_list, current_number // 3)
    return
paper(total_list, square_num)
for a in range(3):
    print(paper_list[a])
    