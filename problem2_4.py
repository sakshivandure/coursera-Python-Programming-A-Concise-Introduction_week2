import random

def problem2_4():
    
    lis=[]
    random.seed(70)
    for i in range(10):
        x=random.random()
        lis.append(x*5+30)
    print(lis)