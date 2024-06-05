class Scheduler:
    def __init__(self):
        self.methods = ["SJF", "FIFO", "HRRN", "PRIORITY"]

    #Shortest Job First
    def sort_process_list_sjf(self,process_list):
        """
        Sort process_list according to Short Job First
        :param process_list:
        :return:
        """
        process_list.sort(key=lambda x: (x.type == "Process", x.finishTime))

    #Taza repuesta mas alta
    def sort_process_list_hrrn(self,process_list):
        """
        Sort process_list according to High Rate Response Next First
        :param process_list:
        :return:
        """
        process_list.sort(key=lambda x: (x.type == "Process", -((x.awaitingTime + x.finishTime) / x.finishTime)))

    #FIFO
    def get_processes_fifo(self, process_list):
        """
        return process_list simulating fifo
        :return:
        """
        process_list.sort(key=lambda x: (x.type == "Process", x.idProcess))


    #Prioridad
    def sort_process_list_priority(self, process_list):
        """
        Sort process_list according to Priority
        :param process_list:
        :return:
        """
        process_list.sort(key=lambda x: (x.type == "Process", x.priority))


    def get_methods(self):
        return self.methods

    def add_process(self, process):
        """
        Add process to process_list to future simulate fifo
        :param process:
        :return:
        """
        self.processes.append(process)

    def delete_process(self, process):
        print(f'Esta es la lista \n {self.processes}')
        """
        Delete process from process_list
        :param process:
        :return:
        """
        self.processes.remove(process)
