import random
def high(temp):
    if temp>45:
        print("alarm is ON")
    else:
        print("alarm is OFF")

while(1):
    temp=random.randint(25,100)
    humid=random.randint(0,100)
    print(temp)
    print(humid)
    high(temp)
print("\n")
