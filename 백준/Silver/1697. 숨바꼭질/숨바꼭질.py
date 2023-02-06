subin_location, other_location = map(int, input().split())
visited = [False] * 100001
def find_other(subin_location, other_location):
    location_list = [[subin_location, 0]]
    while location_list != []:
        v = location_list.pop()
        try:
            if v[0] < 0 or visited[v[0]]:
                continue
        except IndexError:
            continue
        visited[v[0]] = True
        if v[0] == other_location:
            print(v[1])
            break
        location_list.insert(0,[v[0] * 2, v[1] + 1])
        location_list.insert(0,[v[0] + 1, v[1] + 1])
        location_list.insert(0,[v[0] - 1, v[1] + 1])
find_other(subin_location, other_location)

    