def print_callback(result):
    print("Received result: ", result)

def do_something(callback):
    # ... do some work here ...
    result = "Hello, World!"
    callback(result)

def main():
    do_something(print_callback)

if __name__ == "__main__":
    main()