from tkinter import *
from window import w
from menubar import menubar
from files import File
import os
import subprocess

# Running a program need a file, so the run and compile process has a file object
class Run:
    def __init__(self):
        self.file = File()
        self.file.file_menu()
        self.run = Menu(menubar.toolbar, tearoff=False)
        self.run.add_command(label="Run", command=lambda: self.run_it())
        menubar.toolbar.add_cascade(label="Run", menu=self.run)
        self.binding_keys()

    def run_it(self):
        try:
            self.file.save_file()
            if self.file.f.name.endswith(".py"):
                subprocess.Popen(["python", self.file.f.name], shell=True)
            elif self.file.f.name.endswith(".js"):
                subprocess.Popen(["node", self.file.f.name], shell=True)

        except:
            print("Error")

    def binding_keys(self):
        w.root.bind_all("<F5>", lambda event: self.run_it())


# bind a key for run, and it should check file extension to run it in the suitable programming language, if it was txt file, it should open notepad.