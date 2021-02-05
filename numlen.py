def numLen(num):
    x = 0
    while True:
        if 10**x > num:
            break
        else:
            x += 1
    return x


print(numLen(int(input("Number?"))))
input()
