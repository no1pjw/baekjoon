building_num = int(input())
building_list = list(map(int, input().split()))
max_seen_building = 0
for a in range(0, building_num):
    count = 0
    for b in range(0, building_num):
        cant_see = False
        if a == b:
            continue
        for c in range(min(a, b) + 1, max(a, b)):
            num = (building_list[a] - building_list[b]) /(a - b)
            num2 = building_list[b] - num * (b + 1)
            if num * (c + 1) + num2 <= building_list[c]:
                cant_see = True
                break
        if not(cant_see):
            count += 1
    if count > max_seen_building:
        max_seen_building = count
print(max_seen_building)