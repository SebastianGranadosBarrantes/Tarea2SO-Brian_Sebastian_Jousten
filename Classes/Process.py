import threading
import time
from os import system

class Process(threading.Thread):
    def __init__(self, idProcess, processName, processSize, finishTime, priority):
        super().__init__()
        self.idProcess = idProcess
        self.awaitingTime = 0
        self.processName = processName
        self.finishTime = int(finishTime)
        self.executionTime = 0
        self.priority = int(priority)
        self.quantum = 0
        self.stopped = threading.Event()
        self.pageNumber = 0 # this can be a list of the pages that the process have
        self.state = 'Await'  # states are await, ready and execution
        self.processSize = int(processSize)
        self.pages_table = []

    def run(self):
        print(f'Process {self.idProcess} ({self.processName}) started with finish time {self.finishTime}')
        while self.executionTime < self.finishTime:
            time.sleep(1)
            self.executionTime += 1
            print(f'Process {self.idProcess} ({self.processName}) executing, time left: {self.finishTime - self.executionTime}')
            print()
        print(f'Process {self.idProcess} ({self.processName}) finished')

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


    def setQuantum(self, quantum):
        self.quantum = quantum

    def get_values(self):
        values = [self.idProcess,self.awaitingTime, self.finishTime, self.executionTime, self.priority]
        return values