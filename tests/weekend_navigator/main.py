import random

with open("loc_d") as file:
    d = file.read().splitlines()

with open("loc_v") as file:
    v = file.read().splitlines()

d_updated =

print(d)

r = random.choice(d)

print(f"-> {r}")

with open("loc_v", mode='a') as file:
    v = file.write(f"{r}" + "\n")



print(v)
