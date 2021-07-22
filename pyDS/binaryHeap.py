class BinaryHeap(object):
    """docstring for BinaryHeap."""

    def __init__(self):
        super(BinaryHeap, self).__init__()
        self.heap_list = [0]
        self.current_size = 0

    def perc_up(self, i):
        """
        help-method for insert
        push small child node up to parent position
        """
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i //= 2

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.perc_up(self.current_size)

    def perc_down(self, i):
        """
        help-method for del_min
        push large parent position down to child node
        """
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc

    def min_child(self, i):
        """
        help-method for prec_down
        find the smallest child
        """
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def del_min(self):
        ret_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.perc_down(1)
        return ret_val

    def build_heap(self, a_list):
        i = len(a_list) // 2
        self.current_size = len(a_list)
        self.heap_list = [0] + a_list[:]
        while i > 0:
            self.perc_down(i)
            i -= 1

def main():
    a = BinaryHeap()
    a.build_heap([9, 6, 5, 2, 3])
    print(a.heap_list[1:])
    a.insert(4)
    print(a.heap_list[1:])

if __name__ == '__main__':
    main()
