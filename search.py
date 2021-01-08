import tkinter as tk
from tkinter import ttk
from window import w
from menubar import menubar


class Search:
    def __init__(self):
        self.search = tk.Menu(menubar.toolbar, tearoff=False)
        self.binding_keys()

    def search_menu(self):
        self.search.add_command(
            label="Find...",
            command=lambda: self.find_window(),
            accelerator="Ctrl+F"
        )
        self.search.add_command(
            label="Find and Replace",
            command=lambda: self.find_and_replace_window(),
            accelerator="Ctrl+H",
        )
        menubar.toolbar.add_cascade(label="Search", menu=self.search)
        w.root.config(menu=self.search)

    def find_window(self):
        self.find_win = tk.Toplevel(w.root)
        self.find_win.title("Find..")
        self.find_win.resizable(False, False)
        self.find_button = ttk.Button(
            self.find_win,
            text="           Find         ",
            command=lambda: self.find(),
        )
        self.find_all_button = ttk.Button(
            self.find_win,
            text="           Find all    ",
            command=lambda: self.find_all(),
        )
        self.entry = tk.Entry(self.find_win, width=75)
        self.find_win.geometry("200x100")

        self.entry.pack()
        self.find_all_button.pack(side=tk.LEFT, padx=(5, 0))
        self.find_button.pack(side=tk.LEFT, padx=(5, 0))

    def find(self):
        text = w.tab.txt_collection[
            (w.tab.notebook.index(w.tab.notebook.select()))
            ]
        text.tag_remove("match", "1.0", tk.END)
        count = tk.IntVar()
        try:
            s = text.search(self.entry.get(), "1.0", count=count)
            text.tag_configure("match", background="orange")
            end = f"{s}+{count.get()}c"
            text.tag_add("match", s, end)
            text.bind(
                "<Button-1>",
                lambda event_data: text.tag_remove("match", "1.0", tk.END)
            )
        except IndexError:
            return
        if self.entry.get() in text.get("1.0", tk.END):
            return True
        else:
            return False

    def find_all(self):
        text = w.tab.txt_collection[
            w.tab.notebook.index(w.tab.notebook.select())
            ]
        text.tag_remove("match", "1.0", tk.END)
        text.tag_configure("match", background="orange")
        count = tk.IntVar()
        addition_factor = 0
        index = "1.0"
        while True:
            try:
                s = text.search(
                    self.entry.get(), index, tk.END, count=count, regexp=True
                    )
                end = f"{s}+{count.get()}c"
                text.tag_add("match", s, end)
                text.see(s)
                addition_factor += 1
                index = f"1.0+{addition_factor}c"
                text.bind(
                    "<Button-1>",
                    lambda event_data: w.txt.tag_remove(
                        "match", "1.0", tk.END
                        ),
                )
                w.root.update()
            except tk.TclError:
                break
        if self.entry.get() in text.get("1.0", tk.END):
            return True
        else:
            return False

    def find_and_replace_window(self):
        self.f_r_win = tk.Toplevel(w.root)
        self.f_r_win.title("Find and Replace")
        self.find_button2 = ttk.Button(
            self.f_r_win,
            text="          Find        ",
            command=lambda: self.find(),
        )
        self.find_all_button = ttk.Button(
            self.f_r_win,
            text="          Find all      ",
            command=lambda: self.find_all(),
        )
        self.entry = tk.Entry(self.f_r_win, width=75)
        self.f_r_win.geometry("457x140")
        self.f_r_win.resizable(False, False)
        self.replace_entry = tk.Entry(self.f_r_win, width=75)
        self.replace_button = ttk.Button(
            self.f_r_win,
            text="          Replace           ",
            command=lambda: self.replace(),
        )
        self.replace_all_button = ttk.Button(
            self.f_r_win,
            text="          Replace all       ",
            command=lambda: self.replace_all(),
        )
        self.entry.pack()
        self.replace_entry.pack()
        self.replace_all_button.pack(side=tk.LEFT, padx=(5, 0))
        self.replace_button.pack(side=tk.LEFT, padx=(5, 0))
        self.find_all_button.pack(side=tk.LEFT, padx=(5, 0))
        self.find_button2.pack(side=tk.LEFT, padx=(5, 0))

    def replace(self):
        text = w.tab.txt_collection[
            (w.tab.notebook.index(w.tab.notebook.select()))
            ]
        try:
            if self.find():
                ranges = [str(i).strip("<>") for i in text.tag_ranges("match")]
                text.replace(ranges[0], ranges[-1], self.replace_entry.get())
        except (tk.TclError, IndexError):
            return

    def replace_all(self):
        text = w.tab.txt_collection[
            (w.tab.notebook.index(w.tab.notebook.select()))
            ]
        try:
            if self.find_all():
                ranges = [str(i).strip("<>") for i in text.tag_ranges("match")]
                all_occurences = len(ranges) - 1
                while all_occurences > 0:
                    text.replace(
                        ranges[all_occurences - 1],
                        ranges[all_occurences],
                        self.replace_entry.get(),
                    )
                    all_occurences -= 2
        except tk.TclError:
            return

    def binding_keys(self):
        w.root.bind_all("<Control-f>", lambda event: self.find_window())
        w.root.bind_all("<Control-F>", lambda event: self.find_window())
        w.root.bind_all(
            "<Control-h>", lambda event: self.find_and_replace_window()
            )
        w.root.bind_all(
            "<Control-H>", lambda event: self.find_and_replace_window()
            )
