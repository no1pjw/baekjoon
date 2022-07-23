import sys
input = sys.stdin.readline
num = int(input())
total = 54
isfind = False
list1 =[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 21, 30, 31, 32, 40, 41, 42, 43, 50, 51, 52, 53, 54, 60, 61, 62, 63, 64, 65, 70, 71, 72, 73, 74, 75, 76, 80, 81, 82, 83, 84, 85, 86, 87, 90, 91, 92, 93, 94, 95, 96, 97, 98]
if num <= 54:
    print(list1[num])
    isfind = True
if not(isfind):
    for a in range(2, 10):
        for b in range(1, a):
            for c in range(0, b):
                total += 1
                if total == num:
                    print(f'{a}{b}{c}')
                    isfind = True
if not(isfind):
    for d in range(3, 10):
        for e in range(2, d):
            for f in range(1, e):
                for g in range(0, f):
                    total += 1
                    if total == num:
                        print(f'{d}{e}{f}{g}')
                        isfind = True
if not(isfind):
    for d in range(4, 10):
        for e in range(3, d):
            for f in range(2, e):
                for g in range(1, f):
                    for h in range(0, g):
                        total += 1
                        if total == num:
                            print(f'{d}{e}{f}{g}{h}')
                            isfind = True
if not(isfind):
    for d in range(5, 10):
        for e in range(4, d):
            for f in range(3, e):
                for g in range(2, f):
                    for h in range(1, g):
                        for i in range(0, h):
                            total += 1
                            if total == num:
                                print(f'{d}{e}{f}{g}{h}{i}')
                                isfind = True
if not(isfind):
    for d in range(6, 10):
        for e in range(5, d):
            for f in range(4, e):
                for g in range(3, f):
                    for h in range(2, g):
                        for i in range(1, h):
                            for j in range(0, i):
                                total += 1
                                if total == num:
                                    print(f'{d}{e}{f}{g}{h}{i}{j}')
                                    isfind = True
if not(isfind):
    for d in range(7, 10):
        for e in range(6, d):
            for f in range(5, e):
                for g in range(4, f):
                    for h in range(3, g):
                        for i in range(2, h):
                            for j in range(1, i):
                                for k in range(0, j):
                                    total += 1
                                    if total == num:
                                        print(f'{d}{e}{f}{g}{h}{i}{j}{k}')
                                        isfind = True
if not(isfind):
    for d in range(8, 10):
        for e in range(7, d):
            for f in range(6, e):
                for g in range(5, f):
                    for h in range(4, g):
                        for i in range(3, h):
                            for j in range(2, i):
                                for k in range(1, j):
                                    for l in range(0, k):
                                        total += 1
                                        if total == num:
                                            print(f'{d}{e}{f}{g}{h}{i}{j}{k}{l}')
                                            isfind = True
if not(isfind):
    total += 1
    if total == num:
        print(9876543210)
        isfind = True
if not(isfind):
    print(-1)
