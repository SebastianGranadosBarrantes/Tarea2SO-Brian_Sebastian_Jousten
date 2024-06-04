from Classes.Process import Process
from Classes.Machine_Parameters import MachineParameters
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from Classes.Processor import Processor
from mainInterface import Ui_MainWindow
from Classes.Scheduler import Scheduler

class MainWindow(QMainWindow):
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
        self.ui.btnGenerateRandom.clicked.connect(self.create_random_proc)

        self.ui.btnLauch.clicked.connect(self.handle_launch)
        self.ui.tbwProcess.itemSelectionChanged.connect(self.get_process_from_table)
        self.ui.btnPause.clicked.connect(self.handle_pause_process)
        self.ui.btnDone.clicked.connect(self.handle_resume_process)
        self.process_id = []
        self.schedul = Scheduler()
        self.selected_process = None

    def updateTblPrcs(self):
        """
        Update table after sorting
        :return:
        """
        try:
            self.ui.tbwProcess.setRowCount(len(self.process_list))
            for i in range(len(self.process_list)):
                self.ui.tbwProcess.setItem(i, 0, QTableWidgetItem(str(self.process_list[i].idProcess)))
                self.ui.tbwProcess.setItem(i, 1, QTableWidgetItem(str(self.process_list[i].type)))
                self.ui.tbwProcess.setItem(i, 2, QTableWidgetItem(self.process_list[i].processName))
                self.ui.tbwProcess.setItem(i, 3, QTableWidgetItem(str(self.process_list[i].processSize)))
                self.ui.tbwProcess.setItem(i, 4, QTableWidgetItem(str(self.process_list[i].pageNumber)))
                self.ui.tbwProcess.setItem(i, 5, QTableWidgetItem(self.process_list[i].state))
        except Exception as e:
            print(e)

    def handler_create_proces_service(self):

        process_size = self.ui.tfProcessSize.text()
        process_name = self.ui.tfProcessName.text()
        new_process_type = self.ui.cmbType.currentText()
        if self.machine_parameters is None:
            QMessageBox.critical(self, 'Error','The machine parameters most be initialize')
        elif process_name == '':
            QMessageBox.critical(self, 'Error', 'A process/service cant be created without a name')
        elif process_size == '':
            QMessageBox.critical(self, 'Error', 'A process/service cant be created with out a size')
        elif process_size == '0':
            QMessageBox.critical(self, 'Error', 'A process/service cant be created with a size zero')

        else:
            self.create_proces_service(new_process_type, process_name, process_size)

    def create_proces_service(self, new_process_type, process_name, process_size):
        """
        Create a process/service
        :param new_process_type:
        :param process_name:
        :param process_size:
        :return:
        """
        try:
            new_process_id = self.find_avaliable_id()
            new_process_priority = self.get_random_priority()
            new_process_execution_time = self.get_random_execution_time()
            new_process = Process(new_process_id, process_name, process_size, new_process_execution_time, new_process_priority, new_process_type)
            if self.machine_parameters.assign_memory_to_process(new_process):
                QMessageBox.about(self, 'Success', 'process created successfully')
            else:
                QMessageBox.critical(self, 'Error','Could not reserve memory space for the process, the process cannot be created')
                return
            self.machine_parameters.update_remaining_memory(process_size,True)

            self.schedul.add_process(new_process)
            self.process_list.append(new_process)
            self.process_id.append(new_process_id)
            self.update_process_table()
            self.init_prMemory_table()
            self.init_seMemory_table()
        except Exception as e:
            print(e)

    def create_random_proc(self):
        """
        Create a random process/service
        :return:
        """
        try:
            if self.machine_parameters is None:
                QMessageBox.critical(self, 'Error', 'The machine parameters most be initialize')
                return
            process_size = random.randint(1, self.machine_parameters.get_remaining_memory())
            option = random.randint(0,1)
            new_process_type = "Process" if option == 0 else "Service"
            process_name = new_process_type + str(random.randint(1, 100))
            self.create_proces_service(new_process_type, process_name, process_size)
        except Exception as e:
            print(e)

    def verify_pow2(self, number):
        if number <= 0:
            return False
        return (number & (number - 1)) == 0

    def define_machine(self):
        """
        Define a machine parameter
        :return:
        """
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

    def update_process_table(self):
        """
        Insert a process in the table processes
        :return:
        """
        process = self.process_list[-1]
        actual_row = self.ui.tbwProcess.rowCount()
        self.ui.tbwProcess.insertRow(actual_row)
        self.ui.tbwProcess.setItem(actual_row, 0, QTableWidgetItem(str(process.idProcess)))
        self.ui.tbwProcess.setItem(actual_row, 1, QTableWidgetItem(process.type))
        self.ui.tbwProcess.setItem(actual_row, 2, QTableWidgetItem(process.processName))
        self.ui.tbwProcess.setItem(actual_row, 3, QTableWidgetItem(str(process.processSize)))
        self.ui.tbwProcess.setItem(actual_row, 4, QTableWidgetItem(str(process.pageNumber)))
        self.ui.tbwProcess.setItem(actual_row, 5, QTableWidgetItem(process.state))
        #self.ui.tbwProcess.setItem(actual_row, 5, QTableWidgetItem(str(process.pages_per_principal)))
        #self.ui.tbwProcess.setItem(actual_row, 6, QTableWidgetItem(str(process.pages_per_secondary)))

    def get_process_from_table(self):
        selected_process = self.ui.tbwProcess.currentRow()
        if selected_process != -1:
            item = self.ui.tbwProcess.item(selected_process, 0)
            if item:
                self.selected_process = self.find_process_per_id(item.text())

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

    def find_row_proccess_table_per_processId(self, process_id):
        for row in range(self.ui.tbwProcess.rowCount()):
            process = self.ui.tbwProcess.item(row, 0)
            if int(process.text()) == process_id:
                return row
    def alter_prMemory_table(self, page_number):
        row = self.find_row_pgN_prMemo(page_number)
        page = self.machine_parameters.get_principal_memory_pages()[row]
        self.ui.tbwPrimaryMemory.setItem(row, 0, QTableWidgetItem(str(f'{page.initial_position} - {page.final_position}')))
        self.ui.tbwPrimaryMemory.setItem(row, 1, QTableWidgetItem(str(page.page_number)))
        self.ui.tbwPrimaryMemory.setItem(row, 2, QTableWidgetItem(str(page.execution_page_number)))
        self.ui.tbwPrimaryMemory.setItem(row, 3, QTableWidgetItem(str(page.process_id)))
        self.ui.tbwPrimaryMemory.setItem(row, 4, QTableWidgetItem(str(page.process_name)))

    def handle_process_finished(self, process_id):
        process = self.find_process_per_id(process_id)
        self.remove_process_from_tables(process)


    def remove_process_from_tables(self, process):
        try:
            self.process_list.remove(process)
            self.schedul.delete_process(process)
            self.machine_parameters.update_remaining_memory(process.get_size(),False)
            self.machine_parameters.remove_memory_from_process(process)
            self.init_seMemory_table()
            self.init_prMemory_table()
            if process.type == 'Service':
                process.service_running = False
            process.finishTime = 0
            process.pages_table = []
            self.updateTblPrcs()
        except Exception as e:
            print(e)

    def handle_pause_process(self):
        if self.selected_process == -1 or self.selected_process is None:
            QMessageBox.critical(self, 'Error', 'Before pause please select a process from the table by selected him')
        else:
            if self.selected_process.state == 'Execution':
                self.selected_process.state = 'Await'
                self.updateTblPrcs()
            else:
                QMessageBox.warning(self, 'Warning', 'Process already paused')
    def handle_resume_process(self):
            if self.selected_process == -1 or self.selected_process is None:
                QMessageBox.critical(self, 'Error', 'Before resume please select a process from the table by selected him')
            else:
                self.remove_process_from_tables(self.selected_process)
                self.selected_process = None

    def handle_launch(self):
        """
        Launch sorting and initialize cores with processes
        :return:
        """
        if not self.machine_parameters or self.machine_parameters.secondary_memory_size == 0:
            QMessageBox.critical(self, 'Error', 'Before launching the program is necessary to set the machine parameters')
        elif len(self.process_list) == 0:
            QMessageBox.critical(self, 'Error', 'Before launching the program is necessary to set minimum one process')
        else:
            try:
                self.processor = Processor(4)
                self.algorithm = self.ui.cmbSelectAlgorithm.currentText()
                self.processor.process_finished.connect(self.handle_process_finished)
                if self.algorithm == 'SJF':
                    self.schedul.sort_process_list_sjf(self.process_list)
                elif self.algorithm == 'HRRN':
                    self.schedul.sort_process_list_hrrn(self.process_list)
                elif self.algorithm == 'FIFO':
                    self.process_list = self.schedul.get_processes_fifo()
                elif self.algorithm == 'PRIORITY':
                    self.process_list = self.schedul.sort_process_list_priority(self.process_list)
                for process in self.process_list:
                    self.processor.add_process(process)
                self.processor.start()
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

    def find_process_per_id(self, process_id):
        for process in self.process_list:
            if process.idProcess == int(process_id):
                return process
        return -1

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()






