import sys
sys.path.insert(1, "YourPath/pyDSAL/pyDS")
from stack import Stack

def base_converter(dec_number, base):
    digits = "0123456789ABCDEF"

    rem_stack = Stack()

    while dec_number > 0:
        rem = dec_number % base
        rem_stack.push(rem)
        dec_number //= base

    newString = ""
    while not rem_stack.is_empty():
        newString += digits[rem_stack.pop()]

    return newString

def main():
    print(base_converter(233, 16))

if __name__ == '__main__':
    main()
