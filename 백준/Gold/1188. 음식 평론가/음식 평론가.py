sausage_num, people_num = map(int, input().split())
def gcd(a, b):
    while True:
        num = a % b 
        if num == 0:
            break
        a = b
        b = num
    return b   
print(people_num - gcd(sausage_num, people_num))