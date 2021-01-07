from tkinter import *
import keyboard
from window import w
from menubar import menubar


class Edit:
    def __init__(self):
        self.edit = Menu(menubar.toolbar, tearoff=False)

    def edit_menu(self):
        self.edit.add_command(
            label="Copy", command=lambda: self.copy(), accelerator="Ctrl+C"
        )
        self.edit.add_command(
            label="Paste", command=lambda: self.paste(), accelerator="Ctrl+V"
        )
        self.edit.add_command(
            label="Cut", command=lambda: self.cut(), accelerator="Ctrl+X"
        )
        self.edit.add_command(
            label="Redo", command=lambda: self.redo(), accelerator="Ctrl+Y"
        )
        self.edit.add_command(
            label="Undo", command=lambda: self.undo(), accelerator="Ctrl+Z"
        )
        self.edit.add_command(
            label="Select all", command=lambda: self.select_all(), accelerator="Ctrl+A"
        )
        self.edit.add_command(
            label="Delete", command=lambda: keyboard.press("DEL"), accelerator="DEL"
        )
        menubar.toolbar.add_cascade(label="Edit", menu=self.edit)
        w.root.config(menu=self.edit)

    def copy(self):
        for i in w.tab.txt_collection:
            i.event_generate("<<Copy>>")
            w.root.update()

    def paste(self):
        for i in w.tab.txt_collection:
            i.event_generate("<<Paste>>")
            w.root.update()

    def cut(self):
        for i in w.tab.txt_collection:
            i.event_generate("<<Cut>>")
            w.root.update()

    def redo(self):
        for i in w.tab.txt_collection:
            i.event_generate("<<Redo>>")
            w.root.update()

    def undo(self):
        for i in w.tab.txt_collection:
            i.event_generate("<<Undo>>")
            w.root.update()

    def select_all(self):
        w.root.focus_get().tag_add("sel", "1.0", END)
