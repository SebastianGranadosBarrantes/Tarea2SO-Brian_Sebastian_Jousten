import math

class MachineParameters:
    def __init__(self, primary_memory, secondary_memory, pages_size):
        self.primary_memory = primary_memory
        self.secondary_memory = secondary_memory
        self.pages_size = pages_size
        self.pages_per_primary_memory = self.calculate_pages_per_pmemory()
        self.pages_per_secondary_memory = self.calculate_pages_per_smemory()


    def calculate_pages_per_pmemory(self):
        if self.primary_memory != 0:
            return math.ceil(self.primary_memory / self.pages_size)
        else:
            return 0

    def calculate_pages_per_smemory(self):
        if self.secondary_memory != 0:
            return math.ceil(self.secondary_memory / self.pages_size)
        else:
            return 0
