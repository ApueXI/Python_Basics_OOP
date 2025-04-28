# Can laso be done in sets or tuple
# chose best for yout jop
fruits =     ["apple", "orange", "banana", "coconut"]
vegetables = ["celeru", "carrot", "potatoe"]
meat =       ["chicken", "fish", "turkey"]


names = [["Kiana", "Mei", "Bronya"]
        ,["Seele", "Dudu", "Rita"]
        ,["Cecilia", "Therasa", "Elysia"]]

groceries = [fruits, vegetables, meat]

# [Row][Column]
print(groceries[0][2])

print(names[2][2])

for row in names:
    for column in row:
        print(column, end=" ")
    print()