my_string = "Iaroslav".lower()

my_set = set(my_string)

my_dict = {}

for i in my_set:
    my_dict[i] = my_string.count(i) 

print(my_dict)

print(f"В строке '{my_string}':")

for key, value in my_dict.items():
    print(f"Символ {key} встречается {value} раз(а)")