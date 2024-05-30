import threading
import time

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
        self.pageNumber = 0
        self.processSize = int(processSize)

    def run(self):
        while self.finishTime > self.executionTime:
            if self.quantum != 0:
                print(f'process {self.idProcess} executed in background, rest execution time: {self.finishTime }')
                self.finishTime = self.finishTime - 1
                self.quantum = self.quantum - 1
    def __str__(self):
        return f"Process {self.idProcess} - Awaiting Time: {self.awaitingTime} - Finish Time: {self.finishTime} - Execution Time: {self.executionTime} - Priority: {self.priority}"

    def setQuantum(self, quantum):
        self.quantum = quantum

    def get_values(self):
        values = [self.idProcess,self.awaitingTime, self.finishTime, self.executionTime, self.priority]
        return values