import tkinter as Tk


class View():
    def __init__(self, master, controller):
        self.controller = controller
        self.frame = Tk.Frame(master)
        self.frame.pack()
        self.viewPanel = ViewPanel(master, controller)


class ViewPanel():
    def __init__(self, root, controller):
        self.controller = controller

        # frame 1
        self.framePanel = Tk.Frame(root)
        self.framePanel.pack()

        self.label = Tk.Label(self.framePanel, text="검색할 사람 혹은 전화번호를 입력하시오")
        self.label.pack()

        self.search_term = Tk.StringVar()
        self.entry = Tk.Entry(self.framePanel, textvariable=self.search_term)
        self.entry.pack()