import tkinter as tk

class InstructionPage:
    def __init__(self):
        self.instruction_window = tk.Tk()
        self.instruction_window.title('Instructions')
        self.instruction_window.geometry("900x675")
        self.instruction_window.configure(background='black')

        # create canvas for window
        self.background_canvas = tk.Canvas(self.instruction_window, width=900, height=675)
        self.background_canvas.pack(fill="both", expand=True)

        #gui = InstructionPage()

        # displays background image for the entire page
        self.display_background_image()

        # displays the text instructions for the problem solving game
        self.display_instructions()

        # displays the start game button
        self.start_button()

        self.instruction_window.mainloop()


    def display_background_image(self):
        background_image = tk.PhotoImage(file="images/instruction_image.png")

        #set image in canvas
        self.background_canvas.create_image(0,0, image=background_image, anchor="nw")

        # keep a reference of the image object
        self.background_canvas.image = background_image


    def display_instructions(self):
        data = self.open_txt()
        # create text box for instructions on canvas
        self.background_canvas.create_text(75, 100, text=data, font=('Helvetica', 14), anchor='nw')


    def start_button(self):
        start_button = tk.Button(self.instruction_window, text='Start Game', bg='black', fg='#f2edcf', highlightbackground='#000000',
                                 width=20, command=self.instruction_window.destroy)
        button_window = self.background_canvas.create_window(500,550, anchor='nw', window=start_button)


    def open_txt(self):
        with open('instructions.txt', 'r') as file:
            data = file.read()
        return data


