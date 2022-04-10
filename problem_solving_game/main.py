import tkinter as tk
from controller import Controller

if __name__ == '__main__':
    '''
    root = tk.Tk()
    root.geometry("900x675")
    root.configure(background='black')
    ip = InstructionPage(root)
    gp = GamePage(root)
    root.mainloop()
    '''
    game = Controller()
    game.mainloop()