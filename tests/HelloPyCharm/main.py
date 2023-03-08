# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def some_function(num: int) -> None:
    num += 10
    print(num)


def say_hello(word: str)->str:
    word += "word"
    for char in word:
        if char == 'a':
            print("b")
        else:
            print(char)
    return "fff"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm2')
    some_function(12)
    say_hello("aloalo")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
