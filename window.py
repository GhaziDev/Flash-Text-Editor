from tkinter import ttk
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
        self.indentation()
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
            except:
                break
    def indentation(self):

        text = self.tab.txt_collection[
            self.tab.notebook.index(self.tab.notebook.select())
        ]

        def wrapper(event):
            try:
                pos = text.index(INSERT)
                line, column = (num for num in pos.split("."))
                func_string = text.get(f"{line}.0", f"{line}.{column}")
                pattern = re.compile(r"(?<=\s)[\w()]+(?=\:)")
                func_length = len(pattern.search(func_string).group())
                indentation_factor = abs((int(column) - 1) - func_length)
                if ":" in text.get("insert-1c") or "{" in text.get("insert-1c"):
                    text.insert(INSERT, "\n" + " " * indentation_factor)
                    return "break"
            except:
                return

        text.bind("<Return>", wrapper)



w = Window()
