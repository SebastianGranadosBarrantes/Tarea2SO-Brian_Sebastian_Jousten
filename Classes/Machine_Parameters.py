import math
from .Memory import Memory


class MachineParameters:
    def __init__(self, primary_memory, secondary_memory, pages_size):
        self.primary_memory_size = primary_memory
        self.secondary_memory_size = secondary_memory
        self.pages_size = pages_size
        self.pages_per_primary_memory = self.calculate_pages_per_pmemory()
        self.pages_per_secondary_memory = self.calculate_pages_per_smemory()
        self.primary_memory = Memory(self.primary_memory_size, self.pages_per_primary_memory, pages_size)
        self.secondary_memory = Memory(self.secondary_memory_size, self.pages_per_secondary_memory, pages_size)

    def calculate_pages_per_pmemory(self):
        if self.primary_memory_size != 0:
            amount_pages = math.ceil(self.primary_memory_size / self.pages_size)
            return amount_pages
        else:
            return 0

    def calculate_pages_per_smemory(self):
        if self.secondary_memory_size != 0:
            return math.ceil(self.secondary_memory_size / self.pages_size)
        else:
            return 0

    def get_principal_memory_pages(self):
        return self.primary_memory.memory

    def get_secondary_memory_pages(self):
        return self.secondary_memory.memory