print('Multiply numbers easily!')
again=""
while again!="N":
    print('What is the Number?')
    num=int(input())
    for times in range(1,13):
        print(num," times ",times," = ", num*times)
    print("\nAgain?(Y/N)")
    again=input()
    again=again.upper()
