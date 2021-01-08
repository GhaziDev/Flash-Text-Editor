import tkinter as tk
from tkinter import ttk
from window import w
from menubar import menubar
from tkinter import colorchooser
from textconfig import txtconfig


class Themes:
    def __init__(self):
        self.Theme = tk.Menu(menubar.toolbar, tearoff=False)
        self.themes = tk.Menu(self.Theme, tearoff=False)

    def theme_menu(self):
        self.Theme.add_command(
            label=" Text Color", command=lambda: self.text_color()
        )
        self.Theme.add_command(
            label=" Cursor Color", command=lambda: self.cursor_color()
        )
        self.Theme.add_command(
            label=' Selector" Color', command=lambda: self.selector_color()
        )
        self.themes.add_radiobutton(
            label="Dark (Default)", command=lambda: self.dark_theme()
        )
        self.themes.add_radiobutton(
            label="White", command=lambda: self.white_theme()
            )
        self.themes.add_radiobutton(
            label="Valhalla", command=lambda: self.valhalla_theme()
        )
        self.themes.add_radiobutton(
            label="Havana", command=lambda: self.havana_theme()
            )
        menubar.toolbar.add_cascade(label="Theme", menu=self.Theme)
        self.Theme.add_cascade(label="  Themes", menu=self.themes)
        w.root.config(menu=self.Theme)

    def dark_theme(self):
        s = ttk.Style(w.root)
        s.configure(style="TNotebook", background="#282828")
        w.root.configure(bg="#282828")
        txtconfig.background = "#282828"
        txtconfig.foreground = "white"
        txtconfig.insertbackground = "white"

        for i in w.tab.txt_collection:
            i.config(
                background=txtconfig.background,
                foreground=txtconfig.foreground,
                insertbackground=txtconfig.insertbackground,
            )
            w.root.update()

    def valhalla_theme(self):
        s = ttk.Style(w.root)
        s.configure(style="TNotebook", background="#262442")
        w.root.configure(bg="#262442")
        txtconfig.background = "#262442"
        txtconfig.foreground = "white"
        txtconfig.insertbackground = "white"
        for i in w.tab.txt_collection:
            i.config(
                background=txtconfig.background,
                foreground=txtconfig.foreground,
                insertbackground=txtconfig.insertbackground,
            )
            w.root.update()

    def white_theme(self):
        s = ttk.Style(w.root)
        s.configure(style="TNotebook", background="white")
        w.root.configure(bg="white")
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

    def havana_theme(self):
        s = ttk.Style(w.root)
        w.root.configure(bg="#412A2B")
        s.configure("TNotebook", background="#412A2B")
        txtconfig.background = "#412A2B"
        txtconfig.foreground = "white"
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
        for i in w.tab.txt_collection:
            i.config(foreground=txtconfig.foreground)

    def cursor_color(self):
        txtconfig.insertbackground = colorchooser.askcolor()[1]
        for i in w.tab.txt_collection:
            i.config(insertbackground=txtconfig.insertbackground)

    def selector_color(self):
        txtconfig.selectbackground = colorchooser.askcolor()[1]
        for i in w.tab.txt_collection:
            i.config(selectbackground=txtconfig.selectbackground)


# control any background color through txtconfig object
