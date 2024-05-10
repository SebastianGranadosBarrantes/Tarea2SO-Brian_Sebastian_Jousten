class Process:
    def __init__(self, idProcess, awaitingTime, finishTime, executionTime, priority):
        self.idProcess = idProcess
        self.awaitingTime = awaitingTime
        self.finishTime = finishTime
        self.executionTime = executionTime
        self.priority = priority

    def __str__(self):
        return f"Process {self.idProcess} - Awaiting Time: {self.awaitingTime} - Finish Time: {self.finishTime} - Execution Time: {self.executionTime} - Priority: {self.priority}"
        