import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from window import *
from menubar import *
from theme import *


class File:
    def __init__(self):
        self.file_counter = 0
        self.filemenu = Menu(menubar.toolbar, tearoff=False)
        self.binding_keys()

    def file_menu(self):
        self.filemenu.add_command(
            label="New file        Ctrl+N", command=lambda: self.new_file()
        )
        self.filemenu.add_command(
            label="Open File      Ctrl+O", command=lambda: self.open_file()
        )
        # self.filemenu.add_command(label='Save              Ctrl+S',command=lambda:self.save_file())
        self.filemenu.add_command(
            label="Save as         Ctrl+Shift+S", command=lambda: self.save_file_as()
        )
        self.filemenu.add_command(
            label="Close file      Ctrl+K", command=lambda: self.close_file()
        )
        self.filemenu.add_command(label="Exit", command=lambda: self.exit())
        menubar.toolbar.add_cascade(label="File", menu=self.filemenu)

    def open_file(self):
        try:
            f = filedialog.askopenfile(
                mode="r",
                initialdir="/",
                title="Select A File",
                filetype=(("files", "*.txt"), ("all files", "*.*")),
            )
            filename = os.path.basename(f.name)
            txt, tb = w.tab.add_tab(f"{filename}")
            txt.config(
                undo=True,
                insertbackground="white",
                font=("Terminal", 15),
                height=w.height,
                width=w.width,
            )
            txt.insert("1.0", f.read())
            txt.pack()
            tb.pack()
            self.file_counter += 1
        except:
            return

    def save_file_as(self):
        try:
            for i in w.tab.txt_collection:
                self.f = filedialog.asksaveasfile(
                    mode="w",
                    defaultextension=".txt",
                    initialdir="/",
                    title="Select A File",
                    filetype=(("files", "*.txt"), ("all files", "*.*")),
                )
                self.f.write(i.get("1.0", END))
                self.f.close()
                w.tab.notebook.tab(
                    w.tab.notebook.select(), text=os.path.basename(self.f.name)
                )
                return
        except:
            return

    """def save_file(self):
        try:
            current_tab=str(self.f.name)[::-1].replace('/',f'/{w.tab.notebook.tab(w.tab.notebook.select(),"text")}',0)
            current_tab=current_tab[::-1]
            print(current_tab)
            for i in range(self.file_counter,len(w.tab.txt_collection)):    
                    get=w.tab.txt_collection[i].get('1.0',END)
                    f=open(current_tab,'w')
                    f.write(get)
                    f.close()
        except:
            self.save_file_as()
        """
    # this method is under maintanance

    def new_file(self):
        txt, tb = w.tab.add_tab(f"Untitled")
        txt.config(
            undo=True,
            insertbackground="white",
            font=("Terminal", 15),
            height=w.height,
            width=w.width,
        )
        txt.pack()
        tb.pack()
        t = Themes()

    def close_file(self):
        for current_tab in w.tab.notebook.winfo_children():
            if str(current_tab) == w.tab.notebook.select():
                current_tab.destroy()
                self.file_counter -= 1
                return

    def exit(self):
        exit_win = Toplevel(w.root)
        exit_win.title("")
        windowWidth = exit_win.winfo_reqwidth()
        windowHeight = exit_win.winfo_reqheight()
        positionRight = int(exit_win.winfo_screenwidth() / 2 - windowWidth / 2)
        positionDown = int(exit_win.winfo_screenheight() / 2 - windowHeight / 2)
        exit_win.geometry(f"+{positionRight}+{positionDown}")
        exit_win.resizable(False, False)
        exit_label = Label(exit_win, text="Are you sure you want to quit?")
        save_button = ttk.Button(
            exit_win, text="Save", command=lambda: self.save_file_as()
        )
        exit_button = ttk.Button(
            exit_win, text="Quit", command=lambda: w.root.destroy()
        )
        cancel_button = ttk.Button(
            exit_win, text="Cancel", command=lambda: exit_win.destroy()
        )
        exit_label.pack(side=TOP)
        save_button.pack(side=LEFT)
        exit_button.pack(side=RIGHT)
        cancel_button.pack(side=RIGHT)

    def binding_keys(self):
        w.root.bind_all("<Control-n>", lambda event: self.new_file())
        w.root.bind_all("<Control-N>", lambda event: self.new_file())
        w.root.bind_all("<Control-o>", lambda event: self.open_file())
        w.root.bind_all("<Control-O>", lambda event: self.open_file())
        # w.root.bind_all('<Control-s>',lambda event:self.save_file())
        # w.root.bind_all('<Control-S>',lambda event:self.save_file())
        w.root.bind_all("<Control-Shift-s>", lambda event: self.save_file_as())
        w.root.bind_all("<Control-Shift-S>", lambda event: self.save_file_as())
        w.root.bind_all("<Control-k>", lambda event: self.close_file())
        w.root.bind_all("<Control-K>", lambda event: self.close_file())
