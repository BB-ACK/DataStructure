def iSeperate(num):
    while(num > 0):
        tmp = num % 10
        num /= 10
        print(tmp)

def rSeperate(num):
    if num < 10:
        print(num)
    else:
        print(num % 10)
        rSeperate(num // 10)

num = int(input())
print(rSeperate(num))