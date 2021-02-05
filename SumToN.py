while True:
    print("Input a number")
    n=input()
    print("Sum or Product to N? (s/p?)")
    oper=input()
    sum=0
    product=1
    if oper=="s":
        for x in range(1,int(n)+1):
            sum+=x
        print(sum)
    elif oper=="p":
        for x in range(1,int(n)+1):
            product*=x
        print(product)
    else:
        print("Invalid user input! If you want a sum, type 's'. If you want a product, type 'p'")
