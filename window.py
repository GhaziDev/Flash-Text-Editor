from tkinter import *
from tab import Tab


class Window:
    def __init__(self):
        self.root = Tk()
        self.root.title("Flash")
        self.label = Label(
            self.root,
            width=self.root.winfo_reqwidth(),
            height=self.root.winfo_reqheight(),
            text="Create new file",
        )
        self.tab = Tab(self.root)
        self.txt, self.tb = self.tab.add_tab("Untitled")
        self.height, self.width = (
            self.root.winfo_reqheight(),
            self.root.winfo_reqwidth(),
        )
        self.txt.config(
            height=self.height,
            width=self.width,
        )
        self.footer = Label(self.root)

        self.footer.pack(fill="both", expand="yes", side=BOTTOM)
        self.txt.pack(fill="both", expand="yes")
        self.tb.pack(fill="both", expand="yes")
        self.label.pack()
        self.root.geometry("998x646")
        self.root.minsize(width=400, height=200)

    def footer_elements(self):
        while True:
            try:
                for i in w.tab.txt_collection:
                    word_count = len(i.get("1.0", END).split())
                    character_count = len(i.get("1.0", END)) - i.get("1.0", END).count(
                        "\n"
                    )
                    mouse_pos = i.index(INSERT)
                    line, column = (int(num) for num in mouse_pos.split("."))
                    self.footer.configure(
                        text=f"word count: {word_count}   character count: {character_count}     lines number: {line}    columns number: {column}",
                        anchor=E,
                    )
                self.root.update()
            except TclError:
                break


w = Window()
