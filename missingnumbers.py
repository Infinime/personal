import time
number = input("Input a long number\n")
rn = time.time()
numlist = [x for x in number]
print(time.time.__module__)
numlist.sort()
for x in range(1, 10):
    if str(x) not in numlist:
        print(x)
print(time.time() - rn)
input()
