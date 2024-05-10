class MachineParameters:
    def __init__(self, virtualMemory, primaryMemory, secondaryMemory) :
        self.virtualMemory = virtualMemory
        self.primaryMemory = primaryMemory
        self.secondaryMemory = secondaryMemory

    def __str__(self):
        return f"Virtual Memory: {self.virtualMemory} - Primary Memory: {self.primaryMemory} - Secondary Memory: {self.secondaryMemory}"
    
    def setVirtualMemory(self, virtualMemory):
        self.virtualMemory = virtualMemory

    def setPrimaryMemory(self, primaryMemory):
        self.primaryMemory = primaryMemory
    
    def setSecondaryMemory(self, secondaryMemory):
        self.secondaryMemory = secondaryMemory
    
    def getVirtualMemory(self):
        return self.virtualMemory
    
    def getPrimaryMemory(self):
        return self.primaryMemory
    
    def getSecondaryMemory(self):
        return self.secondaryMemory
    
    