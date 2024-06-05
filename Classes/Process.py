import time
from PyQt6.QtCore import QThread, QMutex, pyqtSignal
import threading

class Process(QThread):
    process_finished = pyqtSignal(int)
    remaining_time_signal = pyqtSignal(int)
    def __init__(self, idProcess, processName, processSize, finishTime, priority, type):
        super().__init__()
        self.idProcess = idProcess
        self.awaitingTime = 0
        self.processName = processName
        self.finishTime = int(finishTime)
        self.executionTime = 0
        self.priority = int(priority)
        self.quantum = 0
        self.pageNumber = 0 # this can be a list of the pages that the process have
        self.state = 'Await'
        self.processSize = int(processSize)
        self.pages_table = []
        self.type = type
        self.service_running = True
        self.startTime = time.time()
        self.is_waiting = True
        self.first_iteration = True
        self.velocity = 1
        self.remaining_time = 0

    def run(self):
        print(self.type)
        if self.type == 'Process':
            print(f'Process {self.idProcess} ({self.processName}) started with finish time {self.finishTime}')
            while self.executionTime < self.finishTime:
                if not self.is_waiting:
                    self.executionTime += 1
                    self.remaining_time = self.finishTime - self.executionTime
                    self.calculate_velocity()
                    print(f'Process {self.idProcess} ({self.processName}) executing, time left: {self.finishTime - self.executionTime}')
                    self.remaining_time_signal.emit(self.idProcess)
                    self.msleep(self.velocity)
            self.process_finished.emit(self.idProcess)
            print(f'Process {self.idProcess} ({self.processName}) finished')
        else:
            while self.service_running:
                if self.first_iteration:
                    self.remaining_time_signal.emit(self.idProcess)
                print(f'Service {self.idProcess} ({self.processName}) in execution')
                self.sleep(1)
            self.process_finished.emit(self.idProcess)

    def find_memory_pages_secondary_memory(self, secondary_memory_id):
        print(f'the pages_table list size is {len(self.pages_table)}')
        counter = 0
        for page in self.pages_table:
            if page.memory_id == secondary_memory_id:
                counter += 1

        if counter == len(self.pages_table):
            return True
        return False

    def update_time(self):
        self.awaitingTime += time.time() - self.startTime

    def set_start_time(self):
        self.startTime = time.time()

    def calculate_velocity(self):
        for page in self.pages_table:
            if page.memory_id == 1:
                self.velocity = 1500
                return
        self.velocity = 1000
        return


    def __str__(self):
        return (f"Process(idProcess={self.idProcess}, "
                f"awaitingTime={self.awaitingTime}, "
                f"processName={self.processName}, "
                f"finishTime={self.finishTime}, "
                f"executionTime={self.executionTime}, "
                f"priority={self.priority}, "
                f"quantum={self.quantum}, "
                f"pageNumber={self.pageNumber}, "
                f"state={self.state}, "
                f"processSize={self.processSize})")

    def set_is_waiting(self, is_waiting):
        self.is_waiting = is_waiting

    def get_size(self):
        return self.processSize