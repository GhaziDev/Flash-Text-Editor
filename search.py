from tkinter import ttk
from tkinter import *
import keyboard
from window import w
from menubar import menubar


class Search:
    def __init__(self):
        self.search = Menu(menubar.toolbar, tearoff=False)
        self.binding_keys()

    def search_menu(self):
        self.search.add_command(
            label="Find...",
            command=lambda: self.find_window(),accelerator='Ctrl+F'
        )
        self.search.add_command(
            label="Find and Replace",
            command=lambda: self.find_and_replace_window(),accelerator='Ctrl+H'
        )
        menubar.toolbar.add_cascade(label="Search", menu=self.search)
        w.root.config(menu=self.search)

    def find_window(self):
        self.find_win = Toplevel(w.root)
        self.find_win.title("Find..")
        self.find_win.resizable(False, False)
        self.find_button = ttk.Button(
            self.find_win,
            text="           Find         ",
            command=lambda: self.find(),
            width=20,
        )
        self.find_all_button = ttk.Button(
            self.find_win,
            text="           Find all    ",
            command=lambda: self.find_all(),
            width=20,
        )
        self.entry = Entry(self.find_win, width=75)
        self.find_win.geometry("457x70")

        self.entry.pack()
        self.find_all_button.pack(side=BOTTOM)
        self.find_button.pack(side=BOTTOM)

    def find(self):
        try:
            w.txt.tag_remove("match", "1.0", END)
            count = IntVar()
            s = w.txt.search(self.entry.get(), "1.0", stopindex="end", count=count)
            w.txt.tag_configure("match", background="orange")
            end = f"{s}+{count.get()}c"
            w.txt.tag_add("match", s, end)
            w.txt.bind(
                "<Button-1>", lambda event_data: w.txt.tag_remove("match", "1.0", END)
            )
        except:
            return
        if self.entry.get() in w.txt.get("1.0", END):
            return True
        else:
            return False

    def find_all(self):
        w.txt.tag_remove("match", "1.0", END)
        w.txt.tag_configure("match", background="orange")
        count = IntVar()
        addition_factor = 0
        index = "1.0"
        while True:
            try:
                s = w.txt.search(self.entry.get(), index, END, count=count, regexp=True)
                end = f"{s}+{count.get()}c"
                w.txt.tag_add("match", s, end)
                w.txt.see(s)
                addition_factor += 1
                index = f"1.0+{addition_factor}c"
                w.txt.bind(
                    "<Button-1>",
                    lambda event_data: w.txt.tag_remove("match", "1.0", END),
                )
                w.root.update()
            except:
                break
        if self.entry.get() in w.txt.get("1.0", END):
            return True
        else:
            return False

    def find_and_replace_window(self):
        self.f_r_win = Toplevel(w.root)
        self.f_r_win.title("Find and Replace")
        self.find_button2 = ttk.Button(
            self.f_r_win,
            text="          Find        ",
            command=lambda: self.find(),
            width=20,
        )
        self.find_all_button = ttk.Button(
            self.f_r_win,
            text="          Find all      ",
            command=lambda: self.find_all(),
            width=20,
        )
        self.entry = Entry(self.f_r_win, width=75)
        self.f_r_win.geometry("457x140")
        self.f_r_win.resizable(False, False)
        self.replace_entry = Entry(self.f_r_win, width=75)
        self.replace_button = ttk.Button(
            self.f_r_win,
            text="          Replace           ",
            command=lambda: self.replace(),
            width=20,
        )
        self.replace_all_button = ttk.Button(
            self.f_r_win,
            text="          Replace all       ",
            command=lambda: self.replace_all(),
            width=20,
        )
        self.entry.pack()
        self.replace_entry.pack()
        self.replace_all_button.pack(side=BOTTOM)
        self.replace_button.pack(side=BOTTOM)
        self.find_all_button.pack(side=BOTTOM)
        self.find_button2.pack(side=BOTTOM)

    def replace(self):
        try:
            if self.find() == True:
                ranges = [str(i).strip("<>") for i in w.txt.tag_ranges("match")]
                w.txt.replace(ranges[0], ranges[-1], self.replace_entry.get())
        except:
            return

    def replace_all(self):
        try:
            if self.find_all() == True:
                ranges = [str(i).strip("<>") for i in w.txt.tag_ranges("match")]
                all_occurences = len(ranges) - 1
                while all_occurences > 0:
                    w.txt.replace(
                        ranges[all_occurences - 1],
                        ranges[all_occurences],
                        self.replace_entry.get(),
                    )
                    all_occurences -= 2
        except:
            return

    def binding_keys(self):
        w.root.bind_all("<Control-f>", lambda event: self.find_window())
        w.root.bind_all("<Control-F>", lambda event: self.find_window())
        w.root.bind_all("<Control-h>", lambda event: self.find_and_replace_window())
        w.root.bind_all("<Control-H>", lambda event: self.find_and_replace_window())
