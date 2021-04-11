import tkinter as Tk
import json

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

        # 안내창
        self.label = Tk.Label(self.framePanel, text="검색할 사람 혹은 전화번호를 입력하시오")
        self.label.pack()

        # 검색어 입력창
        self.search_term = Tk.StringVar()
        self.entry = Tk.Entry(self.framePanel, textvariable=self.search_term)
        self.entry.pack(side='top')
        # 엔터키 눌러도 검색할 수 있게
        # self.entry.bind("enter?")

        self.btn = Tk.Button(self.framePanel, text="search")
        self.btn.pack(side='top', padx=6)
        # Event handlers passes events to controller
        self.btn.bind("<Button>", self.controller.updateListBox) # <- search and update list

        self.listBox = Tk.Listbox(self.framePanel, height=0, selectmode="browse")
        self._init_listBox()
        self.listBox.pack()

        # 전화번호부 추가창
        self.phoneAddButton = Tk.Button(self.framePanel, text="새 전화번호 추가하기")
        self.phoneAddButton.pack(side="bottom")
        self.phoneAddButton.bind("<Button>", self.controller.addPhoneAddEntry)

        # frame 2
        self.isPhoneRegisterOn = False
        self.framePanel2 = Tk.Frame(root)
        if (self.isPhoneRegisterOn):
            self.framePanel2.pack()
        
        self.phoneNameLabel = Tk.Label(self.framePanel2, text="이름")
        self.phoneNameLabel.pack()

        self.phone_name = Tk.StringVar()
        self.entryPhoneName = Tk.Entry(self.framePanel2, textvariable=self.phone_name)
        self.entryPhoneName.pack()

        self.phoneNumberLabel = Tk.Label(self.framePanel2, text="전화번호")
        self.phoneNumberLabel.pack()

        self.phone_number = Tk.StringVar()
        self.entryPhoneNumber = Tk.Entry(self.framePanel2, textvariable=self.phone_number)
        self.entryPhoneNumber.pack()

        self.phoneAddButton = Tk.Button(self.framePanel2, text="추가하기")
        self.phoneAddButton.pack()
        # Event handlers passes events to controller
        self.phoneAddButton.bind("<Button>", self.controller.addPhoneInfo) # <- add phone info

    def _init_listBox(self):
        self.listBox.delete(0, Tk.END)

        items = self.controller.search("")
        for item in items:
            self.listBox.insert(Tk.END, item)
