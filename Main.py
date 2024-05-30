from PyQt6.uic import loadUi
from Classes.Process import Process
import Classes.Machine_Parameters as mp


import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from mainInterface import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.algorithm = ''
        self.process_list = []
        self.machine_parameters = mp.MachineParameters(0,0,0)
        self.ui.btnCreateProccess.clicked.connect(self.handler_create_proces)
        self.ui.btnSetParameters.clicked.connect(self.define_machine)
        self.ui.btnLauch.clicked.connect(self.handle_launch)
        self.process_id = []

    def handler_create_proces(self):
        process_size = self.ui.tfProcessSize.text()
        process_name = self.ui.tfProcessName.text()
        if process_size == '':
            QMessageBox.critical(self, 'Error', 'A process cant be created with out a size')
        elif process_name == '':
            QMessageBox.critical(self, 'Error', 'A process cant be created without a name')
        elif process_size == '0':
            QMessageBox.critical(self, 'Error', 'A process cant be created with a size zero')
        else:
            new_process_id = self.find_avaliable_id()
            new_process_priority = self.get_random_priority()

    def define_machine(self):
        principal_memory_size = self.ui.tfPrincipalMemorySize.text()
        secondary_memory_size = self.ui.tfSecondaryMemorySize.text()
        pages_size = self.ui.tfPagesSize.text()
        if principal_memory_size == '' or principal_memory_size == '0':
            QMessageBox.critical(self, 'Error', 'Is necessary to define a principal memory size')
        elif secondary_memory_size == '' or secondary_memory_size == '0':
            QMessageBox.critical(self, 'Error', 'Is necessary to define a secondary memory size')
        elif pages_size == '' or pages_size == '0':
            QMessageBox.critical(self, 'Error', 'Is necessary to define a page size')
        else:
            self.machine_parameters.primary_memory = int(principal_memory_size)
            self.machine_parameters.secondary_memory = int(secondary_memory_size)
            self.machine_parameters.pages_size = int(pages_size)
            self.machine_parameters.pages_per_primary_memory = self.machine_parameters.calculate_pages_per_pmemory()
            self.machine_parameters.pages_per_secondary_memory = self.machine_parameters.calculate_pages_per_smemory()


    def handle_launch(self):
        if self.machine_parameters.primary_memory == 0 or self.machine_parameters.secondary_memory == 0:
            QMessageBox.critical(self, 'Error', 'Before launching the program is necessary to set the machine parameters')
        else:
            print('Code executed')
    def get_random_priority(self):
        return random.randint(1, 20)



    def find_avaliable_id(self):
        find = False
        counter = 0
        while not find:
            counter_find = True
            for id in self.process_id:
                if id == counter:
                    counter_find = False
            if counter_find:
                find = True
            else:
                counter += 1
        return counter




    def add_process(self):
        print('Esto es una prueba')
        # values = [entry.get() for entry in entry_fields]
        # for value in values:
        #     if value == '':
        #         print('Error, alguno de los campos necesarios esta vacio')
        #         return
        # for process in process_list:
        #     if process.idProcess == values[0]:
        #         print('Error, el proceso con ese id ya existe, cambielo y vuelva a intentar')
        #         return
        #
        # process = Process(values[0], values[1], values[2], values[3], values[4])
        # process_list.append(process)
        # print(f'Esta es la lista de procesos actual{process_list}')


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()



# def set_parameters():
#     principalMemorySize = int(principalMemorySize_entry.get())
#     secondaryMemorySize = int(secondaryMemorySize_entry.get())
#     machine = mp.MachineParameters(principalMemorySize, secondaryMemorySize)
#     print(machine)
#     parametersView.destroy()
#     openProcessView(machine)


def set_algorithm(option):
    algorithm = option
    print(f'El algoritmo se seteo a {algorithm}')




global process_list
process_list = []

global algorithm
algorithm = ''




