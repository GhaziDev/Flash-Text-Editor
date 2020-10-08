from tkinter import ttk
from window import *
from menubar import *
from search import Search
from ttkthemes import ThemedStyle
from tkinter import colorchooser
from textconfig import *


class Themes:
    def __init__(self):
        self.Theme = Menu(menubar.toolbar, tearoff=False)
        self.themes = Menu(self.Theme, tearoff=False)

    def theme_menu(self):
        self.Theme.add_command(label=" Text Color", command=lambda: self.text_color())
        self.Theme.add_command(
            label=" Cursor Color", command=lambda: self.cursor_color()
        )
        self.Theme.add_command(
            label='"Selector" Color', command=lambda: self.selector_color()
        )
        self.themes.add_radiobutton(
            label="Dark (Default)", command=lambda: self.dark_theme()
        )
        self.themes.add_radiobutton(label="White", command=lambda: self.white_theme())
        self.themes.add_radiobutton(label="Blue", command=lambda: self.blue_theme())
        self.themes.add_radiobutton(label="Orange", command=lambda: self.orange_theme())
        menubar.toolbar.add_cascade(label="Theme", menu=self.Theme)
        self.Theme.add_cascade(label="  Themes", menu=self.themes)
        w.root.config(menu=self.Theme)

    def dark_theme(self):
        s = ThemedStyle(w.root)
        s.theme_use("black")
        txtconfig.background = "gray20"
        txtconfig.foreground = "black"
        txtconfig.insertbackground = "white"
        for i in w.tab.txt_collection:
            i.config(
                background=txtconfig.background,
                foreground=txtconfig.foreground,
                insertbackground=txtconfig.insertbackground,
            )
            w.root.update()

    def blue_theme(self):
        s = ThemedStyle(w.root)
        s.theme_use("blue")
        txtconfig.background = "CornflowerBlue"
        txtconfig.foreground = "white"
        txtconfig.insertbackground = "white"
        for i in w.tab.txt_collection:
            i.config(
                background=txtconfig.background,
                foreground=txtconfig.foreground,
                insertbackground=txtconfig.insertbackground,
            )
            w.root.update()

    def white_theme(self, txt=w.txt):
        s = ThemedStyle(w.root)
        s.theme_use("plastik")
        txtconfig.background = "white"
        txtconfig.foreground = "black"
        txtconfig.insertbackground = "black"
        for i in w.tab.txt_collection:
            i.config(
                background=txtconfig.background,
                foreground=txtconfig.foreground,
                insertbackground=txtconfig.insertbackground,
            )
            w.root.update()

    def orange_theme(self):
        s = ThemedStyle(w.root)
        s.theme_use("kroc")
        txtconfig.background = "Orange"
        txtconfig.foreground = "black"
        txtconfig.insertbackground = "white"
        for i in w.tab.txt_collection:
            i.config(
                background=txtconfig.background,
                foreground=txtconfig.foreground,
                insertbackground=txtconfig.insertbackground,
            )
            w.root.update()

    def text_color(self):
        txtconfig.foreground = colorchooser.askcolor()[1]
        try:
            for i in w.tab.txt_collection:
                i.config(foreground=txtconfig.foreground)
        except:
            return

    def cursor_color(self):
        txtconfig.insertbackground = colorchooser.askcolor()[1]
        try:
            for i in w.tab.txt_collection:
                i.config(insertbackground=txtconfig.insertbackground)
        except:
            return

    def selector_color(self):
        txtconfig.selectbackground = colorchooser.askcolor()[1]
        try:
            for i in w.tab.txt_collection:
                i.config(selectbackground=txtconfig.selectbackground)
        except:
            return
