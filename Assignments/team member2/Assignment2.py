import random
def high(t):
    if t>45:
        print("alarm is turned ON")
    else:
        print("alarm is turned OFF")

while(1):
    temperature=random.randint(25,100)
    humidity=random.randint(0,100)
    print(temperature)
    print(humidity)
    high(temperature)
print("\n")
