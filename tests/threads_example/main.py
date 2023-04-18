from threading import Thread
from time import sleep

def my_func(num:int, sleep_value:int)->None:
    for i in range(1, 10):
        print(f"func #{num} - {i}")
        sleep(sleep_value)

t1 = Thread(target=my_func, args=[1, 1], daemon=True)
t2 = Thread(target=my_func, args=[2, 2], daemon=True)

t2.start()
sleep(1)
t1.start()

while True:
    print(".")
    sleep(0.5)
    if not t1.is_alive() and not t2.is_alive():
        print("that's all")
        break