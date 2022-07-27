def main():
    print_column(3)
    print_row(4)
    print_block(3, 6)
    
def print_column(height):
    for i in range(height):
        print('#')

def print_row(width):
    print('?' * width )

def print_block(height, width):
    for i in range(height):
        print('&' * width)    
    
main()
