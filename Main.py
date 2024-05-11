from tkinter import *
from Classes.Process import Process
import Classes.Machine_Parameters as mp
from tkinter import ttk

def set_parameters():
    principalMemorySize = int(principalMemorySize_entry.get())
    secondaryMemorySize = int(secondaryMemorySize_entry.get())
    virtualMemorySize = int(virtualMemorySize_entry.get())
    machine = mp.MachineParameters(virtualMemorySize, principalMemorySize, secondaryMemorySize)
    parametersView.destroy()
    openProcessView(machine)

parametersView = Tk()
parametersView.title('Define general parameters')
parametersView.geometry("1000x500")

def openProcessView(machine):
    processView = Tk()
    processView.title('Process view')
    processView.geometry("1000x500")

    frame = Frame(processView)
    frame.pack()

    tree = ttk.Treeview(frame, columns=("idProcess", "awaitingTime", "finishTime", "executionTime", "priority"), show="headings", height=14)
    tree.pack(side=LEFT)

    tree.column("#0", width=270, minwidth=270, stretch=NO)
    tree.column("idProcess", width=150, minwidth=150, stretch=NO)
    tree.column("awaitingTime", width=400, minwidth=200)
    tree.column("finishTime", width=80, minwidth=50, stretch=NO)
    tree.column("executionTime", width=120, minwidth=50, stretch=NO)
    tree.column("priority", width=120, minwidth=50, stretch=NO)

    tree.heading("#0",text="Name",anchor=W)
    tree.heading("idProcess", text="Id Process",anchor=W)
    tree.heading("awaitingTime", text="Awaiting Time",anchor=W)
    tree.heading("finishTime", text="Finish Time",anchor=W)
    tree.heading("executionTime", text="Execution Time",anchor=W)
    tree.heading("priority", text="Priority",anchor=W)

    tree.insert("", 1, text="Line 1", values=("X","220","40", "10", "3"))
    tree.insert("", 2, text="Line 2", values=("Y","66","12", "38", "3"))
    tree.insert("", 3, text="Line 3", values=("Z","152","120", "134", "4"))
    tree.insert("", 4, text="Line 4", values=("0","175","60", "20", "2"))
    tree.insert("", 5, text="Line 5", values=("P","198","36", "14", "3"))
    tree.insert("", 6, text="Line 6", values=("R","374","128", "20", "2"))
    tree.insert("", 7, text="Line 7", values=("S","100","79", "175", "4"))
    tree.insert("", 8, text="Line 8", values=("T","528","96", "20", "2"))
    tree.insert("", 9, text="Line 9", values=("A","146","115", "139", "3"))
    tree.insert("", 10, text="Line 10", values=("B","110","20", "30", "2"))
    tree.insert("", 11, text="Line 11", values=("C","107","84", "7", "3"))
    tree.insert("", 12, text="Line 12", values=("D","299","236", "18", "4"))
    tree.insert("", 13, text="Line 13", values=("E","275","50", "0", "2"))
    tree.insert("", 14, text="Line 14", values=("F","231","79", "1", "2"))
   
    scroll = ttk.Scrollbar(frame, orient=VERTICAL, command=tree.yview)
    scroll.pack(side=RIGHT, fill=Y)

    tree.configure(yscrollcommand=scroll.set)
    tree.pack()

    Label(processView, text='Actual process').pack()
    processName_entry = Entry(processView)
    processName_entry.pack()

    processView.mainloop()

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