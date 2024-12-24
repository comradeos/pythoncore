def fibonacci(value: int) -> int:
    print(f'Calculating fibonacci for {value}')
    if value <= 1:
        return value
    return fibonacci(value-1) + fibonacci(value-2)

def main() -> None:
    # number_values = 40

    # for i in range(number_values):
    #     print(f'{i}: {fibonacci(i)}')
    print(fibonacci(9))

if __name__ == "__main__":
    main()