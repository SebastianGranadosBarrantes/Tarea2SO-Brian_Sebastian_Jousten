from sched import scheduler

from Classes.Process import Process
from Classes.Machine_Parameters import MachineParameters
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem

from Classes.Processor import Processor
from Classes.Services import Service
from mainInterface import Ui_MainWindow
from Classes.Scheduler import Scheduler

class MainWindow(QMainWindow):##Inicio de clase
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.algorithm = ''
        self.process_list = []
        self.machine_parameters = None
        self.processor = None
        self.ui.btnCreateProccess.clicked.connect(self.handler_create_proces_service)
        self.ui.btnSetParameters.clicked.connect(self.define_machine)
        self.ui.btnLauch.clicked.connect(self.handle_launch)
        self.process_id = []
        self.schedul = Scheduler()

    #actualizar tabla luego de hacer ordenamiento
    def updateTblPrcs(self):
        try:
            self.ui.tbwProcess.setRowCount(len(self.process_list))
            for i in range(len(self.process_list)):
                self.ui.tbwProcess.setItem(i, 0, QTableWidgetItem(str(self.process_list[i].idProcess)))
                self.ui.tbwProcess.setItem(i, 1, QTableWidgetItem(self.process_list[i].processName))
                self.ui.tbwProcess.setItem(i, 2, QTableWidgetItem(str(self.process_list[i].processSize)))
                self.ui.tbwProcess.setItem(i, 3, QTableWidgetItem(str(self.process_list[i].pageNumber)))
                self.ui.tbwProcess.setItem(i, 4, QTableWidgetItem(self.process_list[i].state))
        except Exception as e:
            print(e)

    def handler_create_proces_service(self):
        process_size = self.ui.tfProcessSize.text()
        process_name = self.ui.tfProcessName.text()
        if process_size == '':
            QMessageBox.critical(self, 'Error', 'A process/service cant be created with out a size')
        elif process_name == '':
            QMessageBox.critical(self, 'Error', 'A process/service cant be created without a name')
        elif process_size == '0':
            QMessageBox.critical(self, 'Error', 'A process/service cant be created with a size zero')
        elif self.machine_parameters == None:
            QMessageBox.critical(self, 'Error','The machine parameters most be initialize')
        else:
            new_process_id = self.find_avaliable_id()
            new_process_priority = self.get_random_priority()
            new_process_execution_time = self.get_random_execution_time()
            new_process_type = self.ui.cmbType.currentText()
            new_process = Process(new_process_id, process_name, process_size, new_process_execution_time, new_process_priority, new_process_type)
            if self.machine_parameters.assign_memory_to_process(new_process):
                QMessageBox.about(self, 'Success', 'process created successfully')
            else:
                QMessageBox.critical(self, 'Error','Could not reserve memory space for the process, the process cannot be created')
                return
            self.process_list.append(new_process)
            self.process_id.append(new_process_id)
            self.update_process_table()
            self.init_prMemory_table()
            self.init_seMemory_table()

    def verify_pow2(self, number):
        if number <= 0:
            return False
        return (number & (number - 1)) == 0


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
        elif not self.verify_pow2(int(principal_memory_size)):
            QMessageBox.critical(self, 'Error', 'The principal memory size most be a power of 2 ')
        elif not self.verify_pow2(int(secondary_memory_size)):
            QMessageBox.critical(self, 'Error', 'The secondary memory size most be a power of 2 ')
        elif not self.verify_pow2(int(pages_size)):
            QMessageBox.critical(self, 'Error', 'The principal pages size most be a power of 2 ')
        else:
            try:
                self.machine_parameters = MachineParameters(int(principal_memory_size), int(secondary_memory_size), int(pages_size))
                self.init_prMemory_table()
                self.init_seMemory_table()

            except ValueError:
                print('error while managing the class machine_parameters')

    def update_process_table(self): # insert process in the table
        process = self.process_list[-1]
        actual_row = self.ui.tbwProcess.rowCount()
        self.ui.tbwProcess.insertRow(actual_row)
        print(self.ui.tbwProcess.columnCount())

        self.ui.tbwProcess.setItem(actual_row, 0, QTableWidgetItem(str(process.idProcess)))
        self.ui.tbwProcess.setItem(actual_row, 1, QTableWidgetItem(process.type))
        self.ui.tbwProcess.setItem(actual_row, 2, QTableWidgetItem(process.processName))
        self.ui.tbwProcess.setItem(actual_row, 3, QTableWidgetItem(str(process.processSize)))
        self.ui.tbwProcess.setItem(actual_row, 4, QTableWidgetItem(str(process.pageNumber)))
        self.ui.tbwProcess.setItem(actual_row, 5, QTableWidgetItem(process.state))
        #self.ui.tbwProcess.setItem(actual_row, 5, QTableWidgetItem(str(process.pages_per_principal)))
        #self.ui.tbwProcess.setItem(actual_row, 6, QTableWidgetItem(str(process.pages_per_secondary)))

        print(f'El tamanno de la lista es ${len(self.process_list)}')


    def init_prMemory_table(self):
        self.ui.tbwPrimaryMemory.clearContents()
        self.ui.tbwPrimaryMemory.setRowCount(0)
        actual_row = self.ui.tbwPrimaryMemory.rowCount()
        memory_list = self.machine_parameters.get_principal_memory_pages()
        for page in memory_list:
            self.ui.tbwPrimaryMemory.insertRow(actual_row)
            self.ui.tbwPrimaryMemory.setItem(actual_row, 0, QTableWidgetItem(str(f'{page.initial_position} - {page.final_position}')))
            self.ui.tbwPrimaryMemory.setItem(actual_row, 1, QTableWidgetItem(str(page.page_number)))
            self.ui.tbwPrimaryMemory.setItem(actual_row, 2, QTableWidgetItem(str(page.execution_page_number)))
            self.ui.tbwPrimaryMemory.setItem(actual_row, 3, QTableWidgetItem(str(page.process_id)))
            self.ui.tbwPrimaryMemory.setItem(actual_row, 4, QTableWidgetItem(str(page.process_name)))
            actual_row = self.ui.tbwPrimaryMemory.rowCount()
            self.ui.tfProcessName.clear()
            self.ui.tfProcessSize.clear()
            self.ui.tfProcessName.setFocus()

    def init_seMemory_table(self):
        self.ui.tbwSecondaryMemory.clearContents()
        self.ui.tbwSecondaryMemory.setRowCount(0)
        actual_row = self.ui.tbwSecondaryMemory.rowCount()
        memory_list = self.machine_parameters.get_secondary_memory_pages()
        storage_number = 1
        for page in memory_list:
            self.ui.tbwSecondaryMemory.insertRow(actual_row)
            self.ui.tbwSecondaryMemory.setItem(actual_row, 0, QTableWidgetItem(str(f'{page.initial_position} - {page.final_position}')))
            self.ui.tbwSecondaryMemory.setItem(actual_row, 1, QTableWidgetItem(str(storage_number)))
            self.ui.tbwSecondaryMemory.setItem(actual_row, 2, QTableWidgetItem(str(page.process_id)))
            self.ui.tbwSecondaryMemory.setItem(actual_row, 3, QTableWidgetItem(str(page.process_name)))
            self.ui.tbwSecondaryMemory.setItem(actual_row, 4, QTableWidgetItem(str(page.page_number)))
            actual_row = self.ui.tbwSecondaryMemory.rowCount()
            storage_number += 1

    def find_row_pgN_seMemo(self, page_number):
        for row in range(self.ui.tbwSecondaryMemory.rowCount()):
            item = self.ui.tbwSecondaryMemory.item(row, 4)
            if item and item.text() == str(page_number):
                return row
        return -1

    def alter_seMemory_table(self, page_number):
        row = self.find_row_pgN_seMemo(page_number)
        page = self.machine_parameters.get_secondary_memory_pages()[row]
        self.ui.tbwSecondaryMemory.setItem(row, 0, QTableWidgetItem(str(f'{page.initial_position} - {page.final_position}')))
        self.ui.tbwSecondaryMemory.setItem(row, 1, QTableWidgetItem(str(page.page_number + 1)))
        self.ui.tbwSecondaryMemory.setItem(row, 2, QTableWidgetItem(str(page.process_id)))
        self.ui.tbwSecondaryMemory.setItem(row, 3, QTableWidgetItem(str(page.process_name)))
        self.ui.tbwSecondaryMemory.setItem(row, 4, QTableWidgetItem(str(page.page_number)))

    def find_row_pgN_prMemo(self, page_number):
        for row in range(self.ui.tbwPrimaryMemory.rowCount()):
            item = self.ui.tbwPrimaryMemory.item(row, 4)
            if item and item.text() == str(page_number):
                return row
        return -1

    def alter_prMemory_table(self, page_number):
        row = self.find_row_pgN_prMemo(page_number)
        page = self.machine_parameters.get_principal_memory_pages()[row]
        self.ui.tbwPrimaryMemory.setItem(row, 0, QTableWidgetItem(str(f'{page.initial_position} - {page.final_position}')))
        self.ui.tbwPrimaryMemory.setItem(row, 1, QTableWidgetItem(str(page.page_number)))
        self.ui.tbwPrimaryMemory.setItem(row, 2, QTableWidgetItem(str(page.execution_page_number)))
        self.ui.tbwPrimaryMemory.setItem(row, 3, QTableWidgetItem(str(page.process_id)))
        self.ui.tbwPrimaryMemory.setItem(row, 4, QTableWidgetItem(str(page.process_name)))


    def handle_launch(self):
        if not self.machine_parameters or self.machine_parameters.secondary_memory_size == 0:
            QMessageBox.critical(self, 'Error', 'Before launching the program is necessary to set the machine parameters')
        else:
            try:
                self.processor = Processor(4)
                self.algorithm = self.ui.cmbSelectAlgorithm.currentText()
                if self.algorithm == 'SJF':
                    #ordena por nombre usando scheduler, para obtener un cambio controlado
                    self.schedul.sort_process_list_sjf(self.process_list)
                    
                elif self.algorithm == 'HRRN':
                    print("HRRN aun no implementado")
                    #scheduler.sort_process_list_hrrn(self.process_list)

                elif self.algorithm == 'FIFO':
                    print("Algoritmo FIFO")
                    for process in self.process_list:
                        self.processor.add_process(process)

                else:
                    print("TTF aun no implementado")
                    #scheduler.sort_process_list_ft(self.process_list)
                self.processor.handle_launch()
                self.updateTblPrcs()
            except Exception as e:
                print(e)

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

##Fin de clase

### MAIN ###
### MAIN ###
### MAIN ###

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




