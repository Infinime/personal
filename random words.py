import random

vowels = ["a","e","i","o","u",'y']
consonants = ['q','w','r','t','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
answers = []

for x in range(1000):
    word=''
    word += random.choice(random.choice([vowels,consonants])) for y in range(4)
    answers += word

finans = random.choice(answers)
print(answers)