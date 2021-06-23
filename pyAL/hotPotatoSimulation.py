import sys
sys.path.insert(1, "YourPath/pyDSAL/pyDS")
from queue import Queue

def hot_potato(name_list, num):
    sim_queue = Queue()
    for name in name_list:
        sim_queue.enqueue(name)

    while sim_queue.size() > 1:
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())

        sim_queue.dequeue()  # Drop from the game

    return sim_queue.dequeue()

def main():
    print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))

if __name__ == '__main__':
    main()
