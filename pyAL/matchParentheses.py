import sys
sys.path.insert(1, "YourPath/pyDSAL/pyDS")
from stack import Stack

def parertheses_checker(symbol_string):
    s = Stack()
    balanced = True
    idx = 0

    while idx < len(symbol_string) and balanced:
        symbol = symbol_string[idx]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        idx += 1

    if balanced and s.is_empty():
        return True
    else:
        return False

def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

def main():
    print(parertheses_checker("(()()()())"))
    print(parertheses_checker("(((())))"))
    print(parertheses_checker("())))"))

    print(parertheses_checker("{{([][])}()}"))
    print(parertheses_checker("[][][](){}"))
    print(parertheses_checker("[{()]"))

if __name__ == '__main__':
    main()
