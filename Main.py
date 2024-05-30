from Classes.Process import Process
import Classes.Machine_Parameters as mp
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
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
            self.process_id.append(new_process_id)
            new_process_priority = self.get_random_priority()
            new_process_execution_time = self.get_random_execution_time()
            new_process = Process(new_process_id, process_name, process_size, new_process_execution_time, new_process_priority)
            self.process_list.append(new_process)
            print('proceso creado con exito')
            self.update_process_table()




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

    def update_process_table(self): # insert process in the table
        process = self.process_list[-1]
        print(process)
        actual_row = self.ui.tbwProcess.rowCount()
        self.ui.tbwProcess.insertRow(actual_row)
        print(actual_row)
        print(self.ui.tbwProcess.columnCount())

        self.ui.tbwProcess.setItem(actual_row, 0, QTableWidgetItem(str(process.idProcess)))
        self.ui.tbwProcess.setItem(actual_row, 1, QTableWidgetItem(process.processName))
        self.ui.tbwProcess.setItem(actual_row, 2, QTableWidgetItem(str(process.processSize)))
        self.ui.tbwProcess.setItem(actual_row, 3, QTableWidgetItem(str(process.pageNumber)))
        self.ui.tbwProcess.setItem(actual_row, 4, QTableWidgetItem(process.state))
        self.ui.tbwProcess.setItem(actual_row, 5, QTableWidgetItem(str(process.pages_per_principal)))
        self.ui.tbwProcess.setItem(actual_row, 6, QTableWidgetItem(str(process.pages_per_secondary)))

        print(f'El tamanno de la lista es ${len(self.process_list)}')



    def handle_launch(self):
        if self.machine_parameters.primary_memory == 0 or self.machine_parameters.secondary_memory == 0:
            QMessageBox.critical(self, 'Error', 'Before launching the program is necessary to set the machine parameters')
        else:
            print('Code executed')
    def get_random_priority(self):
        return random.randint(1, 20)

    def get_random_execution_time(self):
        return random.randint(30, 120)

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


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

def set_algorithm(option):
    algorithm = option
    print(f'El algoritmo se seteo a {algorithm}')




global process_list
process_list = []

global algorithm
algorithm = ''




