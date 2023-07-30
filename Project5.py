import random
def monty_hall(simulations):
    without_switching=0
    with_switching=0
    for a in range(simulations):    
        doors=["goat","goat","car"]
        random.shuffle(doors)
        choice=random.choice(doors)
        if choice=="car":
            without_switching+=1
        lst2=[]
        if choice=="goat":
            num1=doors.index(choice)
            num2=doors.index("car")
            lst2.append(doors[num1])
            lst2.append(doors[num2])
            for b in lst2:
                if b=="car":
                    with_switching+=1
    return without_switching,with_switching
simlations=int(input("Enter the number of simulations:"))
count_wins_without_switching,count_wins_with_switching=monty_hall(simlations)

print("Total Simulations:",simlations)
print("Count of wins without switching:",count_wins_without_switching)
print("Probability of wins without switching:",count_wins_without_switching/simlations)
print("Count of wins with switching:",count_wins_with_switching)
print("Probability of wins with switching:",count_wins_with_switching/simlations)
