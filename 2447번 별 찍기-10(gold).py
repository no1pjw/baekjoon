def pattern(num, count, list1):
    if num == 1:
        for f in list1:
            print(f)
        return
    else:
        count *= 3
        num2 = count // 3 + 1
        num /= 3
        list2 = []
        list3 = []
        for e in range(len(list1)):
            list2.append(list1[e])
        for a in range(len(list1)):
            list1[a] *= 3
        for b in range(num2, num2 + count // 3):
            list1. append(list2[b - len(list2) - 1]+ " " * (count // 3) + list2[b - len(list2)-1])
        for c in range(len(list2)):
            list1.append(list2[c] * 3)
        pattern(num, count, list1)

num = int(input())
count = 1
list1 = ["*"]
pattern(num, count, list1)

