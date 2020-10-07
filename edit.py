import os
from tkinter import ttk
from tkinter import *
import pyautogui
import keyboard
from window import *
from menubar import *


class Edit:
    def __init__(self):
        self.edit = Menu(menubar.toolbar, tearoff=False)

    def edit_menu(self):
        self.edit.add_command(label="Copy          Ctrl+c", command=lambda: self.copy())
        self.edit.add_command(
            label="Paste          Ctrl+v", command=lambda: self.paste()
        )
        self.edit.add_command(
            label="Cut             Ctrl+x", command=lambda: self.cut()
        )
        self.edit.add_command(
            label="Redo           Ctrl+y", command=lambda: self.redo()
        )
        self.edit.add_command(label="Undo          Ctrl+z", command=lambda: self.undo())
        self.edit.add_command(
            label="Select all    Ctrl+a", command=lambda: self.select_all()
        )
        self.edit.add_command(
            label="Delete         DEL", command=lambda: keyboard.press("DEL")
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
        try:
            w.root.focus_get().tag_add("sel", "1.0", END)
        except:
            return
