import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from window import w
from menubar import menubar


class File:
    def __init__(self):

        self.filemenu = tk.Menu(menubar.toolbar, tearoff=False)
        self.binding_keys()

    def file_menu(self):
        self.filemenu.add_command(
            label="New file",
            command=lambda: self.new_file(),
            accelerator="Ctrl+N"
        )
        self.filemenu.add_command(
            label="Open File",
            command=lambda: self.open_file(),
            accelerator="Ctrl+O"
        )
        self.filemenu.add_command(
            label="Save",
            command=lambda: self.save_file(),
            accelerator="Ctrl+S"
        )
        self.filemenu.add_command(
            label="Save as",
            command=lambda: self.save_file_as(),
            accelerator="Ctrl+Shift+S",
        )
        self.filemenu.add_command(
            label="Close file",
            command=lambda: self.close_file(),
            accelerator="Ctrl+K"
        )
        self.filemenu.add_command(label="Exit", command=lambda: self.exit())
        menubar.toolbar.add_cascade(label="File", menu=self.filemenu)

    def open_file(self):
        try:
            self.f = filedialog.askopenfile(
                mode="r",
                initialdir="/",
                title="Select A File",
                filetype=(("files", "*.txt"), ("all files", "*.*")),
            )
            filename = os.path.basename(self.f.name)
            txt, tb = w.tab.add_tab(f"{filename}")
            txt.config(
                height=w.height,
                width=w.width,
            )
            txt.insert("1.0", self.f.read())
            txt.pack()
            tb.pack()

        except AttributeError:
            return

    def save_file_as(self):
        try:
            for i in w.tab.txt_collection:
                self.f = filedialog.asksaveasfile(
                    mode="w",
                    defaultextension=".txt",
                    initialdir="/",
                    title="Select A File",
                    filetype=(
                        ("text", "*.txt"),
                        ("python", "*.py"),
                        ("all files", "*.*"),
                    ),
                )
                self.f.write(i.get("1.0", tk.END))
                self.f.close()
                w.tab.notebook.tab(
                    w.tab.notebook.select(), text=os.path.basename(self.f.name)
                )
                return
        except AttributeError:
            return

    def save_file(self):

        try:
            text = w.tab.txt_collection[
                w.tab.notebook.index(w.tab.notebook.select())
                ]
            self.f = open(self.f.name, "w")
            self.f.write(text.get("1.0", tk.END))
            self.f.close()
        except AttributeError:
            self.save_file_as()

    def new_file(self):
        txt, tb = w.tab.add_tab("untitled")
        txt.config(
            height=w.height,
            width=w.width,
        )
        txt.pack()
        tb.pack()

    def close_file(self):
        for current_tab in w.tab.notebook.winfo_children():
            if str(current_tab) == w.tab.notebook.select():
                w.tab.txt_collection.pop(
                    w.tab.notebook.index(w.tab.notebook.select())
                    )
                current_tab.destroy()
                return

    def exit(self):
        exit_win = tk.Toplevel(w.root)
        exit_win.title("")
        windowWidth = exit_win.winfo_reqwidth()
        windowHeight = exit_win.winfo_reqheight()
        positionRight = int(exit_win.winfo_screenwidth() / 2 - windowWidth / 2)
        positionDown = int(
            exit_win.winfo_screenheight() / 2 - windowHeight / 2
            )
        exit_win.geometry(f"+{positionRight}+{positionDown}")
        exit_win.resizable(False, False)
        exit_label = tk.Label(exit_win, text="Are you sure you want to quit?")
        save_button = ttk.Button(
            exit_win, text="Save", command=lambda: self.save_file()
        )
        exit_button = ttk.Button(
            exit_win, text="Quit", command=lambda: w.root.destroy()
        )
        cancel_button = ttk.Button(
            exit_win, text="Cancel", command=lambda: exit_win.destroy()
        )
        exit_label.pack(side=tk.TOP)
        save_button.pack(side=tk.LEFT)
        exit_button.pack(side=tk.RIGHT)
        cancel_button.pack(side=tk.RIGHT)

    def binding_keys(self):
        w.root.bind_all("<Control-n>", lambda event: self.new_file())
        w.root.bind_all("<Control-N>", lambda event: self.new_file())
        w.root.bind_all("<Control-o>", lambda event: self.open_file())
        w.root.bind_all("<Control-O>", lambda event: self.open_file())
        w.root.bind_all("<Control-s>", lambda event: self.save_file())
        w.root.bind_all("<Control-S>", lambda event: self.save_file())
        w.root.bind_all("<Control-Shift-s>", lambda event: self.save_file_as())
        w.root.bind_all("<Control-Shift-S>", lambda event: self.save_file_as())
        w.root.bind_all("<Control-k>", lambda event: self.close_file())
        w.root.bind_all("<Control-K>", lambda event: self.close_file())
