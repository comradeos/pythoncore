# formatted number output
print(1000000)
print(f'{1000000:,}') # 1,000,000

print(f'{1/2}') # 0.5
print(f'{1/2:.2f}') # 0.50

def hello(name:str='world')->None:
    print(f'hello,', name)

hello() # hello, world
hello('bob') # hello, bob