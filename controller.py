import tkinter as Tk
from model import Model
from view import View


class Controller():
    def __init__(self):
        # Toplevel widget of Tk which represents mostly the main window of an application.
        self.root = Tk.Tk()
        # model
        self.model = Model()

        # Pass to view links on root frame and controller object
        self.view = View(self.root, self)
        self.root.title("MVC example")
        self.root.geometry('300x800')

        self.root.mainloop()