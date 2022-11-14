import random
def high(temp):
    if temp>45:
        print("ON the alarm")
    else:
        print("OFF the alarm")

while(1):
    temperature=random.randint(25,100)
    humidity=random.randint(0,100)
    print(temperature)
    print(humidity)
    high(temperature)
print("\n")
