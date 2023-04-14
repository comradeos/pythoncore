import os
import time
import random
import webbrowser


def get_locations(filename: str) -> list:
    with open(filename, mode="r", encoding="utf-8") as f:
        return list(f.read().splitlines())


def set_visited(location: str) -> None:
    with open("locations_visited", mode="a", encoding="utf-8") as f:
        f.write(f"{location}" + "\n")


def make_intrigue(text: str) -> None:
    print(f"{text}", end='', flush=True)
    dots_number = random.randint(3, 7)
    for i in range(dots_number):
        time.sleep(1)
        print(".", end='', flush=True)
    print("\n")


os.chdir(os.path.dirname(__file__))

print("\n\n*** Навігатор \"Кудись-2\" ***\n\n")
time.sleep(1)

locations_all = get_locations("locations_all")
locations_visited = get_locations("locations_visited")
locations_updated = list(set(locations_all) - set(locations_visited))

# print(locations_all)
# print(locations_visited)
# print(locations_updated)

if len(locations_updated) == 0:
    print("Всі маршрути відвідані, час поновити :)")
    exit(0)

make_intrigue("Обираємо маршрут")

random_location = random.choice(locations_updated)

print(f"Маршрут обрано! Сьогодні випало відвідати:\n\t{random_location}")
set_visited(random_location)
print()

make_intrigue(f"Шукаємо інформацію в Інтернеті про {random_location}")

webbrowser.open(f"https://www.google.com/search?q=Київ+\"{random_location}\"+цікаві+місця")
print(f"Готово, приємної подорожі!")
input()
