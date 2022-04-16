import platform
import tkinter as tk
import tkmacosx as tkmac
from game_page import GamePage


class InstructionPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # create canvas for frame
        self.background_canvas = tk.Canvas(self, bg='black', width=900, height=675)
        self.background_canvas.configure(background='black')
        self.background_canvas.pack(fill="both", expand=True)

        # displays background image for the entire page
        self.display_background_image()

        # displays the text instructions for the problem solving game
        self.display_instructions()

        # displays the start game button
        self.start_button()


    def display_background_image(self):
        background_image = tk.PhotoImage(file="images/instruction_image.png")

        #set image in canvas
        self.background_canvas.create_image(0,0, image=background_image, anchor="nw")

        # keep a reference of the image object
        self.background_canvas.image = background_image


    def display_instructions(self):
        data = self.open_txt()
        # create text box for instructions on canvas
        if platform.system() == 'Darwin':
            self.background_canvas.create_text(75, 100, text=data, font=('Helvetica', 20), anchor='nw', fill='black')
        else:
            self.background_canvas.create_text(75, 100, text=data, font=('Helvetica', 14), anchor='nw')


    def start_button(self):
        ''' Creates and displays start button '''

        # button command
        command = lambda: [self.controller.show_frame(GamePage), self.hide_frame()]

        if platform.system() == 'Darwin':
            start_button = tkmac.Button(self, text='Start Game', bg='black', fg='#f2edcf', width=150, command=command)
        else:
            start_button = tk.Button(self, text='Start Game', bg='black', fg='#f2edcf', width=25, command=command)
        button_window = self.background_canvas.create_window(500,550, anchor='nw', window=start_button)


    def hide_frame(self):
        self.pack_forget()


    def open_txt(self):
        with open('instructions.txt', 'r') as file:
            data = file.read()
        return data


