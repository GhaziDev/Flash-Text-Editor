from tkinter import ttk
from tkinter import *
from window import w
from menubar import menubar
from tkinter import messagebox
from right_click_menu import rcm
from edit import Edit
from view import View
from search import Search
from files import File
from theme import Themes

t = Themes()
f = File()
e = Edit()
v = View()
s = Search()
f.file_menu()
e.edit_menu()
v.view_menu()
s.search_menu()
t.theme_menu()
t.dark_theme()
w.root.config(menu=rcm.rightclickmenu)
w.root.config(menu=menubar.toolbar)
w.count_elements()


if __name__ == "__main__":

    w.root.mainloop()
