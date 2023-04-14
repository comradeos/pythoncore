import random

with open("loc_d") as file:
    d = file.read().splitlines()

with open("loc_v") as file:
    v = file.read().splitlines()

d_updated = list(set(d)-set(v))

print(d_updated)

try:
    r = random.choice(d_updated)
except:
    print("that's all")
    exit(0)

print(f"-> {r}")

with open("loc_v", mode='a') as file:
    v = file.write(f"{r}" + "\n")

