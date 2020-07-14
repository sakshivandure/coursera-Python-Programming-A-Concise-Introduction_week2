import random
def problem2_6():
    random.seed(431)
    for i in range(100):
        x=random.randint(1,6)
        y=random.randint(1,6)
        print(x+y)