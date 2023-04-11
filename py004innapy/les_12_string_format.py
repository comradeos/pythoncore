name = "Yaroslav"
age = 33

print("My name " + name + ", I\'m " + str(age) + " years old.")
print("My name {0}, I\'m {1} years old.".format(name, age))
print("My name {fio}, I\'m {old} years old.".format(fio=name, old=age))
print(f"My name {name}, I\'m {age} years old.")
print(f"My name {name.upper()}, I\'m {age/2} years old.")
