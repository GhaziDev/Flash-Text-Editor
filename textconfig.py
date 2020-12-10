"""Made  a class for text configuration, so it is possible and easier to 
control text configurations around all widgets at once,also can be used to edit some other widgets background"""


class TextConfig:
    def __init__(self):
        self.insertbackground = "white"
        self.background = "#282828"
        self.foreground = "white"
        self.selectbackground = "blue"
        self.font_family = "Consolas"
        self.font_size = 15


txtconfig = TextConfig()
