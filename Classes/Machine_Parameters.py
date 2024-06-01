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

    def calculate_pages_per_process(self, process_size):
        return math.ceil(process_size / self.pages_size)

    def assign_memory_to_process(self, process):
        necessary_pages = self.calculate_pages_per_process(process.processSize)
        if len(self.primary_memory.available_pages) >= necessary_pages:
            print('all the process can be charged in the principal memory')
            for i in range(necessary_pages):
                saved1 = self.primary_memory.add_process_to_memory(process.idProcess, process.processName)
                if saved1:
                    print(f'Process page number {i + 1} has been added to memory {saved1}')
                else:
                    print(f'Error while adding process page number {i + 1}')
                    return False

        elif len(self.primary_memory.available_pages) < necessary_pages and len(self.primary_memory.available_pages) != 0:
            print('not all the process can be charged in the principal memory, the process will charged in both memories')
            principal_memory_pages = len(self.primary_memory.available_pages)
            for i in range(necessary_pages):
                if i < principal_memory_pages:
                    saved1 = self.primary_memory.add_process_to_memory(process.idProcess, process.processName)
                    if saved1:
                        print(f'Process page number {i + 1} has been added to memory {saved1}')
                    else:
                        print(f'Error while adding process page number {i + 1}')
                        return False
                else:
                    saved2 = self.secondary_memory.add_process_to_memory(process.idProcess, process.processName)
                    if saved2:
                        print(f'Process page number {i + 1} has been added to memory {saved2}')
                    else:
                        print(f'Error while adding process page number {i + 1}')
                        return False
        elif len(self.secondary_memory.available_pages) >= necessary_pages:
            print('all the process will be charged on the secondary memory, because there is no space in the principal memory')
            for i in range(necessary_pages):
                saved2 = self.secondary_memory.add_process_to_memory(process.idProcess, process.processName)
                if saved2:
                    print(f'Process page number {i + 1} has been added to memory {saved2}')
                else:
                    print(f'Error while adding process page number {i + 1}')
                    return False
        else: # el proceso no puede ser creado porque en ninguno de los dos almacenamientos hay espacio sufieciente para contenerlo
            return False
        return True


        print('both primary and secondary memory are filled, the process cant be created')
        return False

    def calculate_pages_per_smemory(self):
        if self.secondary_memory_size != 0:
            return math.ceil(self.secondary_memory_size / self.pages_size)
        else:
            return 0

    def get_principal_memory(self):  # Get the complete object:
        return self.primary_memory

    def get_secondary_memory(self):
        return self.secondary_memory

    def get_principal_memory_pages(self):
        return self.primary_memory.memory

    def get_secondary_memory_pages(self):
        return self.secondary_memory.memory