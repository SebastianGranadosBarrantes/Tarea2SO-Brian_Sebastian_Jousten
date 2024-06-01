

class Scheduler:
    def __init__(self):
        self.methods = ["SJF","HRRN","FIFO","FT"]

    def sort_process_list_ft(self,process_list):
        return process_list.sort(key=lambda x: x.finishTime)

    # metodo para odenar por tiempo restante mas corto primero (este deberia estar siempre activo)
    def sort_process_list_sjf(self,process_list):
        return process_list.sort(key=lambda x: x.processName)

    # metodo para ordenar por taza repuesta mas alta
    def sort_process_list_hrrn(self,process_list):
        return process_list.sort(key=lambda x: ((x.awaitingTime + x.executionTime) / x.executionTime),reverse=True)

    def getMethods(self):
        return self.methods


def sort_process_list_sjf():
    return None