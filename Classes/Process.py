import time
from PyQt6.QtCore import QThread, QMutex, pyqtSignal


class Process(QThread):
    process_finished = pyqtSignal(int)
    remaining_time_signal = pyqtSignal(int, int)
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

    def run(self):
        print(self.type)
        if self.type == 'Process':
            print(f'Process {self.idProcess} ({self.processName}) started with finish time {self.finishTime}')
            while self.executionTime < self.finishTime:
                self.sleep(1)
                self.executionTime += 1
                remaining_time = self.finishTime - self.executionTime
                print(f'Process {self.idProcess} ({self.processName}) executing, time left: {self.finishTime - self.executionTime}')
                self.remaining_time_signal.emit(self.idProcess, remaining_time)
            self.process_finished.emit(self.idProcess)
            print(f'Process {self.idProcess} ({self.processName}) finished')
        else:
            while self.service_running:
                print(f'Service {self.idProcess} ({self.processName}) in execution')
                self.sleep(1)

    def find_memory_pages_secondary_memory(self, secondary_memory_id):
        print(f'the pages_table list size is {len(self.pages_table)}')
        counter = 0
        for page in self.pages_table:
            if page.memory_id == secondary_memory_id:
                counter += 1

        if counter == len(self.pages_table):
            return True
        return False

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

    def get_size(self):
        return self.processSize