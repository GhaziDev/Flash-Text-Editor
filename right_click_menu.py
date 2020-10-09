from tkinter import *
from window import w
import keyboard
from files import File
from edit import Edit


class RightClickMenu:
    def __init__(self):
        self.rightclickmenu = Menu(w.root, tearoff=False)
        self.right_click_options()
        w.root.bind_all("<Button-3>", lambda event: self.popup(event))

    def right_click_options(self):
        self.rightclickmenu.add_command(label="Copy", command=lambda: Edit.copy(self))
        self.rightclickmenu.add_command(label="Paste", command=lambda: Edit.paste(self))
        self.rightclickmenu.add_command(label="Cut", command=lambda: Edit.cut(self))
        self.rightclickmenu.add_command(
            label="Select all", command=lambda: Edit.select_all(self)
        )
        self.rightclickmenu.add_command(
            label="New File", command=lambda: File.new_file(self)
        )
        self.rightclickmenu.add_command(
            label="Close File", command=lambda: File.close_file(self)
        )

    def popup(self, event):
        try:
            self.rightclickmenu.tk_popup(event.x, event.y)
        finally:
            self.rightclickmenu.grab_release()


rcm = RightClickMenu()
