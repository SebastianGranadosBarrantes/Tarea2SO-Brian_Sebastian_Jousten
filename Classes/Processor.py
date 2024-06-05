import time
from queue import Queue
from PyQt6.QtCore import QThread, QMutex, pyqtSignal


class Processor(QThread):
    process_finished = pyqtSignal(int)
    necessary_swap = pyqtSignal(int)
    def __init__(self, num_cores):
        super().__init__()
        self.num_cores = num_cores
        self.process_queue = Queue()
        self.cores = [None] * num_cores
        self.mutex = QMutex()

    def add_process(self, process):
        self.process_queue.put(process)

    def run(self):
        """
        Execute all the processes in queue
        :return:
        """
        while not self.process_queue.empty() or any(self.cores):
            #self.mutex.lock()
            process_in_secondary_memory = False
            for i in range(self.num_cores):
                if self.cores[i] is None or not self.cores[i].isRunning():
                    if not self.process_queue.empty():
                        process = self.process_queue.get()
                        process.set_is_waiting(False)
                        process.state = 'Execution'
                        if process.find_memory_pages_secondary_memory(1):
                            self.necessary_swap.emit(process.idProcess)
                        self.cores[i] = process
                        self.cores[i].state = 'Execution'
                        self.cores[i].process_finished.connect(self.on_process_finished)
                        process.start()
            #self.mutex.unlock()
            self.msleep(1000)
        print("All processes have been executed.")

    def on_process_finished(self, process_id):
        print('Capturando signal')
        print(process_id)
        self.process_finished.emit(process_id)
