starting = int(input("What is the starting number? "))
ending = int(input("What is the ending number? "))
amount = int(input("What would you like to count by? "))

while int(starting) <= int(ending):
    print(starting)
    starting = int(starting)+int(amount)
