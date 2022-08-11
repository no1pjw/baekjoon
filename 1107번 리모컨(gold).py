import sys
input = sys.stdin.readline
def iswork(str1, list1): #바로 채널을 옮길 수 있는지 확인하는 함수
    count = 0
    if list1 == []:
        return True
    for a in list1:
        count += str1.count(str(a))
    if count == 0:
        return True
    return False
def low_check(cha):
    try:
        iswrong = False
        working_list = []
        low_cha = ""
        num = 0
        for c in range(9, -1, -1):
            if c not in bro_cha_list:
                working_list.append(c)
        working_set = set(working_list)
        for d in range(len(cha)): #채널보다 낮은 수
            if iswrong:
                for e in range(9, -1, -1):
                    if e in working_set:
                        low_cha += str(e)
                        break
            else:
                if int(cha[d]) in working_set:
                    low_cha += cha[d]
                else:
                    for f in range(int(cha[d]), -1, -1):
                        if f in working_set:
                            low_cha += str(f)
                            iswrong = True
                            break
                    if iswrong:
                        continue
                    else:
                        if d == 0:
                            iswrong = True
                            continue
                        else:
                            iswrong = True
                            num += 10 ** (len(cha) - d)
                            for g in range(9, -1, -1):
                                if g in working_set:
                                    low_cha += str(g)
                                    break
        if low_cha == '':
            return 1000000000000
        low_cha = str(int(low_cha) - num)
        if iswork(low_cha, bro_cha_list):
            return low_cha
        else:
            return low_check(low_cha)
    except RecursionError:
        return 100000000
def high_check(cha):
    try:
        iswrong = False
        working_list = []
        high_cha = ""
        num = 0
        for c in range(9, -1, -1):
            if c not in bro_cha_list:
                working_list.append(c)
        working_set = set(working_list)
        for d in range(len(cha)):
            if iswrong:
                for e in range(0, 10):
                    if e in working_set:
                        high_cha += str(e)
                        break
            else:
                if int(cha[d]) in working_set:
                    high_cha += cha[d]
                else:
                    for f in range(int(cha[d]),10):
                        if f in working_set:
                            high_cha += str(f)
                            iswrong = True
                            break
                    if iswrong:
                        continue
                    else:
                        iswrong = True
                        num += 10 ** (len(cha) - d)
                        for g in range(0, 10):
                            if g in working_set:
                                high_cha += str(g)
                                break
        if high_cha == "":
            return 100000000000
        high_cha = str(int(high_cha) + num)
        if iswork(high_cha, bro_cha_list):
            return high_cha
        else:
            return high_check(high_cha)
    except RecursionError:
        return 100000000000

cha = input().rstrip()
num = int(input().rstrip())
if num == 0:
    bro_cha_list = []
else:
    bro_cha_list = list(map(int, input().split())) #broken channel list
gap = abs(int(cha) - 100)
if cha == "100": #옮기려는 채널이 현재 시청 중인 채널인 경우
    print(0)
elif iswork(cha, bro_cha_list): #채널을 바로 옮길 수 있는 경우
    if len(cha) > gap:
        print(gap)
    elif len(cha) < gap:
        print(len(cha))
    else:
        print(gap)
else: # 이 외의 상황
    gap_1 = abs(int(cha) - int(low_check(cha))) + len(str(low_check(cha)))
    gap_2 = abs(int(cha) - int(high_check(cha))) + len(str(high_check(cha)))
    gap_3 = abs(100 - int(cha))
    print(min(gap_1, gap_2, gap_3))
