import datetime
now = datetime.datetime.now()
yr = now.year
def turnToMultFour(n):
    if(n % 4 == 0):
        return n
    else:
        fin = n+1
        return turnToMultFour(fin)
print("The next 20 Olympics are in:")
for x in range(0, 20):
    print("----", turnToMultFour(yr) + (x*4), "----")
