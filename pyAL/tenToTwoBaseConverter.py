import sys
sys.path.insert(1, "YourPath/pyDSAL/pyDS")
from stack import Stack

def divide_by_2(dec_number):
    rem_stack = Stack()

    while dec_number > 0:
        rem = dec_number % 2
        rem_stack.push(rem)
        dec_number //= 2

    bin_string = ""
    while not rem_stack.is_empty():
        bin_string += str(rem_stack.pop())

    return bin_string

def main():
    print(divide_by_2(233))

if __name__ == '__main__':
    main()
