import sys
sys.path.insert(1, "YourPath/pyDSAL/pyDS")
from stack import Stack
import string

def infix_to_postfix(infix_expr):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1
    }

    operation_stack = Stack()
    postfix_list = []

    token_list = infix_expr.split()
    for token in token_list:
        if (token in string.ascii_uppercase) or (token in string.ascii_lowercase):
            postfix_list.append(token)
        elif token == '(':
            operation_stack.push(token)
        elif token == ')':
            top_token = operation_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = operation_stack.pop()
        else:
            while (not operation_stack.is_empty()) and (prec[operation_stack.peek()] >= prec[token]):
                postfix_list.append(operation_stack.pop())
            operation_stack.push(token)

    while not operation_stack.is_empty():
        postfix_list.append(operation_stack.pop())

    return " ".join(postfix_list)

def main():
    print(infix_to_postfix("( A + B ) * ( C + D )"))
    print(infix_to_postfix("A + B * C + D"))
    print(infix_to_postfix("a + b * c + d"))

if __name__ == '__main__':
    main()
