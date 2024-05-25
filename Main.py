from tkinter import *
import tkinter as tk
from Classes.Process import Process
import Classes.Machine_Parameters as mp
import Classes.Table as tb




def set_parameters():
    principalMemorySize = int(principalMemorySize_entry.get())
    secondaryMemorySize = int(secondaryMemorySize_entry.get())
    virtualMemorySize = int(virtualMemorySize_entry.get())
    machine = mp.MachineParameters(virtualMemorySize, principalMemorySize, secondaryMemorySize)
    print(machine)
    parametersView.destroy()
    openProcessView(machine)

def openProcessView(machine):
    processView = Tk()
    processView.title('Process view')
    processView.geometry("1000x500")

    colum_heading = ("idProcess", "awaitingTime", "finishTime", "executionTime", "priority")
    colum_text = ("Id Process", "Awaiting Time", "Finish Time", "Execution Time", "Priority")
    table_process = tb.Table(colum_heading, colum_text, processView)

    Label(processView, text='Actual process').pack()
    processName_entry = Entry(processView)
    processName_entry.pack()

    Label(processView, text='Define a new process').pack()


    frame_fields_process = Frame(processView)
    frame_fields_process.pack()

    frame_button_create_process = Frame(processView)
    frame_button_create_process.pack()

    fields = ["Id Process", "Awaiting Time", "Finish Time", "Execution Time", "Priority"]
    entry_fields = []
    for field in fields:
        label = Label(frame_fields_process, text=field)
        label.pack(side=tk.LEFT)
        entry = Entry(frame_fields_process)
        entry.pack(side=tk.LEFT)
        entry_fields.append(entry)
    Button(frame_button_create_process, text='Create process', command=lambda: add_process(entry_fields)).pack()
    processView.mainloop()

def add_process(entry_fields):
    values = [entry.get() for entry in entry_fields]
    print(f'Estos son los valores que estan en los fields: {values}')

parametersView = Tk()
parametersView.title('Define general parameters')
parametersView.geometry("1000x500")


Label(parametersView, text='Enter the principal memory size(MB):').pack()
principalMemorySize_entry = Entry(parametersView)
principalMemorySize_entry.pack()

Label(parametersView, text='Enter the secondary memory size(GB):').pack()
secondaryMemorySize_entry = Entry(parametersView)
secondaryMemorySize_entry.pack()

Label(parametersView, text='Enter the virtual memory size(MB):').pack()
virtualMemorySize_entry = Entry(parametersView)
virtualMemorySize_entry.pack()

Button(parametersView, text='Set machine parameters', command=set_parameters).pack()

parametersView.mainloop()