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
        self.btn.bind("<Button>", self.controller.search) # <- model의 search function이 들어갈 곳

        self.listBox = Tk.Listbox(self.framePanel, height=0, selectmode="browse")
        for item in self._init_listBox():
            self.listBox.insert(Tk.END, item)

        self.listBox.pack()

        # 전화번호부 추가창
        self.phoneAddButton = Tk.Button(self.framePanel, text="전화번호 추가")
        self.phoneAddButton.pack(side="bottom")
        self.phoneAddButton.bind("<Button>", None)

    def _init_listBox(self):
        with open('data.json', 'r', encoding='utf-8') as f:
            phone_data = json.load(f)
        result_list = []
        for name in phone_data:
            for phone_number in phone_data[name]:
                result_list.append(f'{name} : {phone_number}')
        return sorted(result_list)