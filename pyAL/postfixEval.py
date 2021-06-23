import sys
sys.path.insert(1, "YourPath/pyDSAL/pyDS")
from stack import Stack

def postfix_eval(postfix_expr):
    operand_stack = Stack()
    token_list = postfix_expr.split()

    for token in token_list:
        if token in "0123456789":
            operand_stack.push(int(token))
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.push(result)

    return operand_stack.pop()

def do_math(op, num1, num2):
    if op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2
    elif op == '+':
        return num1 + num2
    else:
        return num1 - num2

def main():
    print(postfix_eval("1 2 3 * + 4 +"))  # 1 + 2 * 3 + 4 = 11

if __name__ == '__main__':
    main()
