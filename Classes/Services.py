import threading
import time
from os import system

class Service(threading.Thread):
    def __init__(self, idService, serviceName, serviceSize):
        super().__init__()
        self.idService = idService
        self.awaitingTime = 0
        self.serviceName = serviceName
        self.stopped = threading.Event()
        self.pageNumber = 0
        self.serviceSize = int(serviceSize)
        self.pages_table = []

    def run(self):
        print(f'({self.serviceName})')
        while time:
            time.sleep(1)
            print(f'({self.serviceName}) executing')
            print()

    def __str__(self):
        return (f"Service(idService={self.idService}, "
                f"serviceName={self.serviceName}, "
                f"pageNumber={self.pageNumber}, "
                f"serviceSize={self.serviceSize})")


