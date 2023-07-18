def main()->None:
    content = input("Input some content: ")
    
    if content.isdigit() :
        print("This is a number!")
    else:
        print("This is a string!")
    
if __name__ == "__main__":
    main()