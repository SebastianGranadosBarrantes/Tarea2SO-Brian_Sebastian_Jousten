import time
from queue import Queue


class Processor:
    def __init__(self, num_cores):
        self.num_cores = num_cores
        self.process_queue = Queue()
        self.cores = [None] * num_cores

    def add_process(self, process):
        self.process_queue.put(process)

    def handle_launch(self):
        while not self.process_queue.empty() or any(self.cores):
            for i in range(self.num_cores):
                if self.cores[i] is None or not self.cores[i].is_alive():
                    if not self.process_queue.empty():
                        process = self.process_queue.get()
                        self.cores[i] = process
                        process.start()
            time.sleep(1)
        print("All processes have been executed.")
