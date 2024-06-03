class Scheduler:
    def __init__(self):
        self.methods = ["SJF","FIFO","HRRN"]
        self.processes = []

    #Shortest Job First
    def sort_process_list_sjf(self,process_list):
        return process_list.sort(key=lambda x: x.finishTime)

    #Taza repuesta mas alta
    def sort_process_list_hrrn(self,process_list):
        return process_list.sort(key=lambda x: ((x.awaitingTime + x.executionTime) / x.executionTime),reverse=True)

    #FIFO
    def get_processes_fifo(self):
        return self.processes


    def get_methods(self):
        return self.methods


    def add_process(self, process):
        self.processes.append(process)

    def set_processes(self,process_list):
        self.processes = process_list

    def delete_process(self, process):
        self.processes.remove(process)
