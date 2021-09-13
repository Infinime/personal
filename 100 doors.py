doors = ["Closed"] * 100


def multsto100(num):
    # Finds the multiples of the number, num
    # that are less than 100
    oneto100 = [x for x in range(1, 101)]
    multiples = []
    for multiple in oneto100:
        if multiple % num == 0:
            multiples += [multiple]
    return multiples


for x in range(1, 101):
    for doornum in multsto100(x):
        if doors[doornum - 1] == "Closed":
            doors[doornum - 1] = "Open"
        else:
            doors[doornum - 1] = "Closed"

print(doors)
print(multsto100(9))
