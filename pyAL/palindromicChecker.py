import sys
sys.path.insert(1, "YourPath/pyDSAL/pyDS")
from deque import Deque

def palindromic_checker(a_string):
    char_deque = Deque()

    for ch in a_string:
        char_deque.add_rear(ch)

    still_equal = True

    while char_deque.size() > 1 and still_equal:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()
        if first != last:
            still_equal = False

    return still_equal

def main():
    print(palindromic_checker("radar"))
    print(palindromic_checker("root"))
    print(palindromic_checker("toot"))

if __name__ == '__main__':
    main()
