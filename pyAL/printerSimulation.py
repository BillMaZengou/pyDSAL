import sys
sys.path.insert(1, "YourPath/pyDSAL/pyDS")
from queue import Queue
import random

class Printer(object):
    """docstring for Printer."""

    def __init__(self, ppm):
        super(Printer, self).__init__()
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task != None:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        return self.current_task != None

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate

class Task(object):
    """docstring for Task."""

    def __init__(self, time):
        super(Task, self).__init__()
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp

def printer_simulation(num_seconds, pages_per_minute):
    lab_printer = Printer(pages_per_minute)
    print_queue = Queue()
    waiting_times = []

    for current_second in range(num_seconds):
        if random.randrange(1, 181) == 180:
            task = Task(current_second)
            print_queue.enqueue(task)

        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)

        lab_printer.tick()

    average_wait = sum(waiting_times) / len(waiting_times)
    print("Average Wait %6.2f secs %3d tasks remaining." % (average_wait, print_queue.size()))

def main():
    for i in range(10):
        printer_simulation(3600, 5)

    print('-' * 10)

    for i in range(10):
        printer_simulation(3600, 10)

if __name__ == '__main__':
    main()
