from tkinter import *
from pandastable import Table, TableModel
import hussle
import curtis

class TestApp(Frame):
    """Basic test frame for the table"""
    def __init__(self, stock_code, depth, parent=None):
        self.parent = parent
        Frame.__init__(self)

        self.main = self.master
        self.main.geometry('1200x400')
        self.main.title('Marshall-Hussle Algorithm Result')

        self.stock_code = stock_code
        self.depth = depth

        f = Frame(self.main)
        f.pack(fill=BOTH,expand=1)

        df = hussle.Hussle(self.stock_code, self.depth).hussle()
        self.table = pt = Table(f, dataframe=df,
                                showtoolbar=True, showstatusbar=True)
        pt.show()
        return

# app = TestApp('SLB', 5)
# #launch the app
# app.mainloop()
