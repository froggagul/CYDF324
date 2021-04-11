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
    
    def search(self, search_term):
        try:
            results = self.model.search(search_term)
        except Exception as e:
            print(e)
            results = []
        return results

    def updateListBox(self, event):
        search_term = self.view.viewPanel.search_term.get()

        self.view.viewPanel.listBox.delete(0, Tk.END)

        results = self.search(search_term)

        for result in results:
            self.view.viewPanel.listBox.insert(Tk.END, result)
    
    def addPhoneAddEntry(self, event):
        print(self.view.viewPanel.isPhoneRegisterOn)
        if (self.view.viewPanel.isPhoneRegisterOn):
            self.view.viewPanel.framePanel2.pack_forget()
        else:
            self.view.viewPanel.framePanel2.pack()
        self.view.viewPanel.isPhoneRegisterOn = not self.view.viewPanel.isPhoneRegisterOn
    
    def addPhoneInfo(self, event):
        name = self.view.viewPanel.phone_name.get()
        phone_number = self.view.viewPanel.phone_number.get()
        self.model.addPhoneInfo(name, phone_number)

        self.updateListBox(event)