import random
def wins_without_switching(simulations):
    without_switching=0
    for _ in range(simulations):    
        doors=["goat","goat","car"]
        random.shuffle(doors)
        choice=random.choice(doors)
        if choice=="car":
            without_switching+=1
    return without_switching
def wins_with_switching(simulations):
    with_switching=0
    for _ in range(simulations):    
        doors=["goat","goat","car"]
        random.shuffle(doors)
        choice=random.choice(doors)             
        lst2=[]
        if choice=="goat":
            num1=doors.index(choice)
            num2=doors.index("car")
            lst2.append(doors[num1])
            lst2.append(doors[num2])
            for b in lst2:
                if b=="car":
                    with_switching+=1
    return with_switching

simlations=int(input("Enter the number of simulations:"))
count_wins_without_switching=wins_without_switching(simlations)
count_wins_with_switching=wins_with_switching(simlations)
print("Total Simulations:",simlations)
print("Count of wins without switching:",count_wins_without_switching)
print("Count of wins without switching:",count_wins_with_switching)
print("Probability of wins without switching:",round(count_wins_without_switching/simlations,4))
print("Probability of wins without switching:",round(count_wins_with_switching/simlations,4))
print("Percentage of wins without switching:",round((count_wins_without_switching/simlations)*100,0),"%")
print("Percentage of wins without switching:",round((count_wins_with_switching/simlations)*100,0),"%")
