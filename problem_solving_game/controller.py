import tkinter as tk
from tkinter import ttk
from game_page import GamePage
from instruction_page import InstructionPage


class Controller(tk.Tk):
    # __init__ function for class controller
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self, bg='black')
        container.pack(side="top", fill="both", expand=True)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (InstructionPage, GamePage):
            frame = F(container, self)

            # initializing frame of that object from
            # InstructionPage, GamePage
            # for loop
            self.frames[F] = frame

        # show instruction page first
        self.show_frame(InstructionPage)


    def show_frame(self, page):
        ''' show current frame '''

        frame = self.frames[page]
        frame.pack()


