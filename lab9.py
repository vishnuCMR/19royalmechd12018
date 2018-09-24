import random
a= True
while a:
    print("You rolled",random.randint(1,6))
    print("Do you want to roll again? Yes/No")
    a = "Yes" in input()
    