people = int(input())
people_list = []
price_list = []
for a in range(people):
    people_list.append(list(map(int, input().split())))
for b in people_list:
    number_list = [0] * 7
    max_num = 0
    price = 2000
    count = 0
    two_num = 0
    for c in b:
        number_list[c]+= 1
    for c in range(7):
        if number_list[c] == 4:
            price_list.append(50000 + c * 5000)
            break
        elif number_list[c] == 3:
            price_list.append(10000 + 1000 * c)
            is_three = True
            break
        elif number_list[c] == 2:
            count += 1
            price += 500 * c
            two_num = c
        elif number_list[c] == 1:
            if c > max_num:
                max_num = c
    if count == 2:
        price_list.append(price)
    elif two_num != 0:
        price_list.append(1000 + 100 * two_num)
    elif max_num != 0:
        price_list.append(100 * max_num)
print(max(price_list))