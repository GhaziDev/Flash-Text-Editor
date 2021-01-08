import tkinter as tk
from window import w
from menubar import menubar
from files import File
import subprocess


class Run:

    def __init__(self):
        self.file = File()
        self.file.file_menu()
        self.run = tk.Menu(menubar.toolbar, tearoff=False)
        self.run.add_command(label="Run", command=lambda: self.run_it())
        menubar.toolbar.add_cascade(label="Run", menu=self.run)
        self.binding_keys()

    def run_it(self):
        self.file.save_file()
        try:
            if self.file.f.name.endswith(".py"):
                subprocess.Popen(["python", self.file.f.name], shell=True)
            elif self.file.f.name.endswith(".js"):
                subprocess.Popen(["node", self.file.f.name], shell=True)
            else:
                print("File is not defined to run")
        except AttributeError:
            return

    def binding_keys(self):
        w.root.bind_all("<F5>", lambda event: self.run_it())


'''bind a key for run,
and it should check file extension,
to run it in the suitable programming language.'''
# Running a program need a file, so the run and compile file has File object
