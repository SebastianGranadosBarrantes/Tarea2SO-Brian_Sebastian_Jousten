from tkinter import *
from Classes.Process import Process
import Classes.Machine_Parameters as mp

def set_parameters():
    principalMemorySize = int(principalMemorySize_entry.get())
    secondaryMemorySize = int(secondaryMemorySize_entry.get())
    virtualMemorySize = int(virtualMemorySize_entry.get())
    machine = mp.MachineParameters(virtualMemorySize, principalMemorySize, secondaryMemorySize)
    root.quit()

root = Tk()
root.title('Define general parameters')
root.geometry("1000x500")

Label(root, text='Enter the principal memory size(MB):').pack()
principalMemorySize_entry = Entry(root)
principalMemorySize_entry.pack()

Label(root, text='Enter the secondary memory size(GB):').pack()
secondaryMemorySize_entry = Entry(root)
secondaryMemorySize_entry.pack()

Label(root, text='Enter the virtual memory size(MB):').pack()
virtualMemorySize_entry = Entry(root)
virtualMemorySize_entry.pack()

Button(root, text='Set machine parameters', command=set_parameters).pack()

root.mainloop()