from tkinter import *
from tkinter import ttk
from textconfig import txtconfig

class Tab:
    def __init__(self, master):
        self.notebook = ttk.Notebook(master)
        self.txt_collection = []

    def add_tab(self, title):
        frame = Frame(self.notebook)
        self.vertical_scrollbar = Scrollbar(frame)

        self.notebook.add(frame, text=title)
        self.txt = Text(
            frame,
            undo=True,
            insertbackground=txtconfig.insertbackground,
            background=txtconfig.background,
            foreground=txtconfig.foreground,
            selectbackground=txtconfig.selectbackground,
            yscrollcommand=self.vertical_scrollbar.set,
        )
        self.vertical_scrollbar.config(command=self.txt.yview)
        self.vertical_scrollbar.pack(fill="both", expand="yes", side=RIGHT)
        self.txt.focus_set()
        self.txt.config(font=(txtconfig.font_family, txtconfig.font_size))
        self.txt_collection.append(self.txt)
        self.txt.bind("<Return>", self.indentation)
        return self.txt, self.notebook

    def indentation(self, event):
        try:
            pos = self.txt.index(INSERT)
            line, column = (num for num in pos.split("."))
            func_len = (self.txt.get(f"{line}.0", f"{line}.{column}")).strip(" ")
            indentation_factor = abs(int(column) - len(func_len)) + 3
            auto_indent = abs(
                int(column)
                - len((self.txt.get(f"{line}.0", f"{line}.{column}").strip(" ")))
            )
            if ":" in self.txt.get("insert-1c"):
                self.txt.insert(INSERT, "\n" + " " * indentation_factor)
                return "break"
            if "{" in self.txt.get("insert-1c"):
                self.txt.insert(INSERT, "\n" + " " * indentation_factor)
                return "break"
            else:
                self.txt.insert(INSERT, "\n" + " " * auto_indent)
                return "break"

        except AttributeError:
            return
