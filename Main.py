
import customtkinter as ctk

from Classes.Process import Process
import Classes.Machine_Parameters as mp
import Classes.Table as tb

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

def set_parameters():
    principalMemorySize = int(principalMemorySize_entry.get())
    secondaryMemorySize = int(secondaryMemorySize_entry.get())
    virtualMemorySize = int(virtualMemorySize_entry.get())
    machine = mp.MachineParameters(virtualMemorySize, principalMemorySize, secondaryMemorySize)
    print(machine)
    parametersView.destroy()
    openProcessView(machine)


def openProcessView(machine):
    processView = ctk.CTk()
    processView.title('Process view')
    processView.geometry("1100x550")

    colum_heading = ("idProcess", "awaitingTime", "finishTime", "executionTime", "priority")
    colum_text = ("Id Process", "Awaiting Time", "Finish Time", "Execution Time", "Priority")
    global table_process
    table_process = tb.Table(colum_heading, colum_text, processView)

    ctk.CTkLabel(processView, text='Actual process').pack()
    processName_entry = ctk.CTkEntry(processView)
    processName_entry.pack()

    ctk.CTkLabel(processView, text='Define a new process').pack(pady=10)


    frame_fields_process = ctk.CTkFrame(processView)
    frame_fields_process.pack()

    fields = ["Id Process:", "Awaiting Time:", "Finish Time:", "Execution Time:", "Priority:"]
    entry_fields = []
    for field in fields:
        label = ctk.CTkLabel(frame_fields_process, text=field)
        label.pack(side=ctk.LEFT)
        entry = ctk.CTkEntry(frame_fields_process)
        entry.pack(side=ctk.LEFT)
        entry_fields.append(entry)
    ctk.CTkButton(processView, text='Create process', command=lambda: add_process(entry_fields)).pack(pady=10)

    frame_algorithms = ctk.CTkFrame(processView)
    frame_algorithms.pack()

    algorithm_options = ["FIFO", "SJF", "tercero", "cuarto"]

    for option in algorithm_options:
        ctk.CTkButton(frame_algorithms, text=option, command=lambda opt=option: set_algorithm(opt)).pack(padx=10, side=ctk.LEFT)

    processView.mainloop()


def set_algorithm(option):
    algorithm = option
    print(f'El algoritmo se seteo a {option}')

def add_process(entry_fields):
    values = [entry.get() for entry in entry_fields]
    for value in values:
        if value == '':
            print('Error, alguno de los campos necesarios esta vacio')
            return
    for process in process_list:
        if process.idProcess == values[0]:
            print('Error, el proceso con ese id ya existe, cambielo y vuelva a intentar')
            return

    process = Process(values[0], values[1], values[2], values[3], values[4])
    process_list.append(process)
    table_process.insert(values)
    print(f'Esta es la lista de procesos actual{process_list}')

parametersView = ctk.CTk()
parametersView.title('Define general parameters')
parametersView.geometry("1000x500")

global process_list
process_list = []

global algorithm
algorithm = ''
ctk.CTkLabel(parametersView, text='Enter the principal memory size(MB):').pack()
principalMemorySize_entry = ctk.CTkEntry(parametersView)
principalMemorySize_entry.pack(pady = 20, padx = 15)

ctk.CTkLabel(parametersView, text='Enter the secondary memory size(GB):').pack()
secondaryMemorySize_entry = ctk.CTkEntry(parametersView)
secondaryMemorySize_entry.pack(pady = 20, padx = 15)

ctk.CTkLabel(parametersView, text='Enter the virtual memory size(MB):').pack()
virtualMemorySize_entry = ctk.CTkEntry(parametersView)
virtualMemorySize_entry.pack(pady = 20, padx = 15)

ctk.CTkButton(parametersView, text='Set machine parameters', command=set_parameters).pack()

parametersView.mainloop()