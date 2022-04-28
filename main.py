import tkinter as tk
from tkinter import ttk


class PlayingFieldFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self._create_widgets()

    def _create_widgets(self):
        for i in range(11):
            for j in range(11):
                b = tk.Button(text="", height=2, width=5)
                b.grid(row=i, column=j)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("A* search")
        self.geometry("495x500")
        self.resizable(0, 0)



if __name__ == "__main__":
    app = App()
    PlayingFieldFrame(app)
    app.mainloop()




