import webbrowser
import tkinter as tk
from tkinter import ttk
from window import w
from menubar import menubar


class Tools:
    def __init__(self):
        self.tool_menu = tk.Menu(menubar.toolbar, tearoff=False)

    def tools_menu(self):
        self.tool_menu.add_command(
            accelerator="Google search",
            command=lambda: self.google_search_win()
        )
        self.tool_menu.add_command(
            accelerator="Wikipedia search",
            command=lambda: self.wiki_search_win()
        )
        menubar.toolbar.add_cascade(label="Tools", menu=self.tool_menu)
        w.root.config(menu=self.tool_menu)

    def google_search_win(self):
        toplevel = tk.Toplevel(w.root)
        toplevel.title("")
        toplevel.geometry("200x100")
        toplevel.resizable(False, False)
        self.entry = tk.Entry(toplevel, width=100)
        search_button = ttk.Button(
            toplevel,
            text="Google search",
            command=lambda: self.google_search()
        )
        search_button.pack(side=tk.BOTTOM, padx=(5, 0))
        self.entry.pack()

    def wiki_search_win(self):
        toplevel = tk.Toplevel(w.root)
        toplevel.title("")
        toplevel.geometry("200x100")
        toplevel.resizable(False, False)
        self.entry1 = tk.Entry(toplevel, width=100)
        search_button = ttk.Button(
            toplevel, text="Wiki search", command=lambda: self.wiki_search()
        )
        search_button.pack(side=tk.BOTTOM, padx=(5, 0))
        self.entry1.pack()

    def google_search(self):
        try:
            webbrowser.open(
                f"https://www.google.com/search?q={self.entry.get()}"
                )
        except tk.TclError:
            webbrowser.open("https://www.google.com/")

    def wiki_search(self):
        try:
            webbrowser.open(
                f"https://www.wikipedia.org/wiki/{self.entry1.get()}"
                )
        except tk.TclError:
            webbrowser.open("https//www.wikipedia.org/")
