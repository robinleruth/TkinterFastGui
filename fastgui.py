import tkinter as tk

class Navbar(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

class Toolbar(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

class Statusbar(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(parent, text="Initialisation faite...")

        self.label.pack()

    def set(self, text):
        self.label['text'] = text

class Main(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

    def test(self):
        self.parent.statusbar.set("a")

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.statusbar = Statusbar(self)
        self.toolbar = Toolbar(self)
        self.navbar = Navbar(self)
        self.main = Main(self)

        self.statusbar.pack(side="bottom", fill="x")
        self.toolbar.pack(side="top", fill="x")
        self.navbar.pack(side="left", fill="y")
        self.main.pack(side="right", fill="both", expand=True)


root = tk.Tk()
MainApplication(root).pack(side="top", fill="both", expand=True)
root.mainloop()
