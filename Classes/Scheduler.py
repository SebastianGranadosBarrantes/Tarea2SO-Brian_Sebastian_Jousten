class Scheduler:
    def __init__(self):
        self.methods = ["SJF","FIFO","HRRN"]

    #Shortest Job First
    def sort_process_list_sjf(self,process_list):
        return process_list.sort(key=lambda x: x.finishTime)

    #Primero en entrar primero en salir
    def sort_process_list_FIFO(self,process_list):
        return process_list.sort(key=lambda x: x.idProcess)

    #Taza repuesta mas alta
    def sort_process_list_hrrn(self,process_list):
        return process_list.sort(key=lambda x: ((x.awaitingTime + x.executionTime) / x.executionTime),reverse=True)

    def getMethods(self):
        return self.methods