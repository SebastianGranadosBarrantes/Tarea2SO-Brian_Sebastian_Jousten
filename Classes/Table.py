from tkinter import *
from tkinter import ttk
class Table:
    def __init__(self, columns_heading, columns_text, view):
        self.frame = Frame(view)
        self.frame.pack()
        self.columns_heading = columns_heading
        self.columns_text = columns_text
        self.table = ttk.Treeview(self.frame, columns=self.columns_heading, show='headings', height=14)
        self.define_columns()
        self.row_counter = 0
        self.scroll = ttk.Scrollbar(self.frame, orient=VERTICAL, command=self.table.yview)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.table.configure(yscrollcommand=self.scroll.set)
        self.table.pack()

    def define_columns(self):
        for columnT, columnH  in zip(self.columns_text, self.columns_heading):
            self.table.column(columnH, width=150, minwidth=150, stretch=NO)
            self.table.heading(columnH, text=columnT, anchor=W)

    def insert(self, row):
        self.table.insert('', self.row_counter, values=row)
        self.row_counter += 1
        print('columna insertada correctamente')

    def delete(self, row_id):
        self.table.delete(row_id)
        self.row_counter -= 1
        self.rearrange_table()
    def rearrange_table(self):
        for i, row_id in enumerate(self.table.get_children(), start=0):
            self.table.move(row_id, '', i)