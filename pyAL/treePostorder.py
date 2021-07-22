import operator

def postorder(tree):
    if tree != None:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_root_val())

"""
Using Postorder to evaluate an operation tree for calculation
"""
def postorder_eval(tree):
    opers = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    res1 = None
    res2 = None

    if tree:
        res1 = postorder_eval(tree.get_left_child())
        res2 = postorder_eval(tree.get_right_child())
        if res1 and res2:
            return opers[tree.get_root_val()](res1, res2)
        else:
            return tree.get_root_val()

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
    print(postorder_eval(x))

if __name__ == '__main__':
    main()
