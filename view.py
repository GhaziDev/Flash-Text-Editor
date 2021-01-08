import tkinter as tk
from tkinter import font
from window import w
from menubar import menubar
from textconfig import txtconfig


class View:
    def __init__(self):
        self.view = tk.Menu(menubar.toolbar, tearoff=False)
        self.font_size = tk.Menu(self.view, tearoff=False)
        self.font_family = tk.Menu(self.view, tearoff=False)

    def view_menu(self):
        self.set_size_command()
        self.set_family_command()
        self.view.add_cascade(label="Font size", menu=self.font_size)
        self.view.add_cascade(label="Font Family", menu=self.font_family)
        menubar.toolbar.add_cascade(label="View", menu=self.view)
        w.root.config(menu=self.view)

    def size_and_family(self, fm, px):

        txtconfig.font_family = fm
        txtconfig.font_size = px
        fonts = font.Font(
            family=txtconfig.font_family,
            size=txtconfig.font_size
            )
        for i in w.tab.txt_collection:
            i.config(font=(fonts))
            w.root.update()

    def set_size_command(self):
        self.font_size.add_radiobutton(
            label="15px(Default)",
            command=lambda: self.size_and_family(txtconfig.font_family, 15),
        )
        self.font_size.add_radiobutton(
            label="20px",
            command=lambda: self.size_and_family(txtconfig.font_family, 20),
        )
        self.font_size.add_radiobutton(
            label="35px", command=lambda: self.size_and_family(txtconfig, 35)
        )
        self.font_size.add_radiobutton(
            label="45px",
            command=lambda: self.size_and_family(txtconfig.font_family, 45),
        )

    def set_family_command(self):
        self.font_family.add_radiobutton(
            label="Consolas",
            command=lambda: self.size_and_family(
                "Consolas", txtconfig.font_size
                )
        )
        self.font_family.add_radiobutton(
            label="Arial",
            command=lambda: self.size_and_family("Arial", txtconfig.font_size),
        )
        self.font_family.add_radiobutton(
            label="Modern",
            command=lambda: self.size_and_family(
                "Modern", txtconfig.font_size
                )
        )
        self.font_family.add_radiobutton(
            label="Roman",
            command=lambda: self.size_and_family("Roman", txtconfig.font_size),
        )
        self.font_family.add_radiobutton(
            label="Courier",
            command=lambda: self.size_and_family(
                "Courier", txtconfig.font_size
                )
        )
        self.font_family.add_radiobutton(
            label="Terminal",
            command=lambda: self.size_and_family(
                "Terminal", txtconfig.font_size
                )
        )
        self.font_family.add_radiobutton(
            label="Palatino Linotype",
            command=lambda: self.size_and_family(
                "Palatino Linotype", txtconfig.font_size
            ),
        )
