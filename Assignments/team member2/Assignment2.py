import random
def high(tre):
    if tre>45:
        print("alarm ON")
    else:
        print("alarm  OFF")

while(1):
    tre=random.randint(25,100)
    hum=random.randint(0,100)
    print(tre)
    print(hum)
    high(tre)
print("\n")
