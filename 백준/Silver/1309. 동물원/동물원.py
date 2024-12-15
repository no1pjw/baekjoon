N = int(input())
check_num = 2
prev_prev_num = 3
prev_num = 7
temp_num = 0
if N == 1:
    print(prev_prev_num)
elif N == 2:
    print(prev_num)
else:
    while check_num < N:
        temp_num = prev_num + prev_prev_num + prev_num
        prev_prev_num = prev_num
        prev_num = temp_num
        check_num += 1
    print(temp_num % 9901)