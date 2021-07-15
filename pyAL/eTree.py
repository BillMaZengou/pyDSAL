import sys
sys.path.insert(1, "YourPath/pyDSAL/pyDS")
from stack import Stack
from binaryTreeInRef import BinaryTree

def build_parse_tree(fpexp):
    fplist = fpexp.split()
    p_stack = Stack()
    eTree = BinaryTree('')
    p_stack.push(eTree)
    current_tree = eTree

    for i in fplist:
        if i == '(':
            current_tree.insert_left('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i not in '+-*/)':
            current_tree.set_root_val(eval(i))
            parent = p_stack.pop()
            current_tree = parent
        elif i in '+-*/':
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ')':
            current_tree = p_stack.pop()
        else:
            raise ValueError("Unknown Operator: " + i)
    return eTree

def evaluate(parse_tree):
    opers = {
        '+':operator.add,
        '-':operator.sub,
        '*':operator.mul,
        '/':operator.truediv
    }
    left_c = parse_tree.get_left_child()
    right_c = parse_tree.get_right_child()

    if left_c and right_c:
        fn = opers[parse_tree.get_root_val()]
        return fn(evaluate(left_c), evaluate(right_c))
    else:
        return parse_tree.get_root_val()
