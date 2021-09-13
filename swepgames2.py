# 10 persons want to watch a match on the stadium. 7 seats left. The exit point only allows one at a time. Sensor gets their height. Code to 
# heights ae 6' 5'5, 5', & 4'. Code that allows 3 that are 6, 2 that's 5'5, 2 for 4' to enter.
# 1 of 6, 1 of 5'5, 1 of 4'
checkstr = ''
height = input("What's your height?\n A: 6 feet\n B: 5'5\n C: 5'\n D: 4'\n")
entrants = {'six':0, 'fivepoint': 0, 'four': 0, 'five':0}
if height.upper() == "A" and entrants['six']<3 and len(checkstr)%3==0:
    entrants['six'] += 1
    print("Welcome")
    checkstr+="l"
elif height.upper() == "B" and entrants['fivepoint']<2 and len(checkstr)%3==1:
    entrants['fivepoint'] += 1
    print("Welcome")
    checkstr+="l"
elif height.upper() == "D" and entrants['four']<2 and len(checkstr)%3==2:
    entrants['four'] += 1
    print("Welcome")
    checkstr+="l"
else:
    print("No space for people your height for now")
