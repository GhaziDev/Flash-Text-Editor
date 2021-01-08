from window import w
from menubar import menubar
from right_click_menu import rcm
from edit import Edit
from view import View
from search import Search
from theme import Themes
from interpret_and_compile import Run
from tools import Tools
t = Themes()
r = Run()
e = Edit()
v = View()
s = Search()
tl = Tools()
e.edit_menu()
v.view_menu()
s.search_menu()
t.theme_menu()
tl.tools_menu()
t.dark_theme()
w.root.config(menu=rcm.rightclickmenu)
w.root.config(menu=menubar.toolbar)
w.footer_elements()

if __name__ == "__main__":

    w.root.mainloop()
