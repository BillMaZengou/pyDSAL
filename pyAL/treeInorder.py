def inorder(tree):
    if tree != None:
        inorder(tree.get_left_child())
        print(tree.get_root_val())
        inorder(tree.get_right_child())

"""
Using inorder to return an expression of equation with parentheses
"""
def print_exp(tree):
    s_val = ""
    if tree:
        s_val = '(' + print_exp(tree.get_left_child())
        s_val += str(tree.get_root_val())
        s_val += print_exp(tree.get_right_child()) + ')'
    return s_val

def main():
    import sys
    sys.path.insert(1, "YourPath/pyDSAL/pyDS")
    from binaryTreeInRef import BinaryTree

    x = BinaryTree('*')
    x.insert_left('+')
    l = x.get_left_child()
    l.insert_left(4)
    l.insert_right(5)
    x.insert_right(7)
    print(print_exp(x))

if __name__ == '__main__':
    main()
