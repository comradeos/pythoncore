def main():
    b1 = 0x03
    b2 = 0xFF
    sum = (b1 + b2) & 0xFF
    print(f"Sum: {sum}")

if __name__ == "__main__":
    main()