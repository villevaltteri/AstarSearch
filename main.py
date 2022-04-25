import tkinter as tk
from tkinter import ttk


class PlayingFieldFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)


class InputFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self._create_widgets()

    def _create_widgets(self):
        pass


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("A* search")
        self.geometry("500x500")
        self.resizable(0, 0)

    def _create_widgets(self):
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()




