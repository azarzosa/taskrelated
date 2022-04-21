import tkinter as tk
import platform
from game_logic import Game


class GamePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # initialize game object
        self.game = Game()

        # create game frame
        self.game_frame = tk.Frame(self, width=900, height=675)
        self.game_frame.pack()

        # images to be used
        self.text_box_background = tk.PhotoImage(file="images/bg_scroll-1.png")
        self.treasure_chest      = tk.PhotoImage(file='images/treasure_chest.png')
        self.poison_trap         = tk.PhotoImage(file='images/Poison_Trap.png')

        # create canvas for frame
        self.background_canvas = tk.Canvas(self.game_frame, bg='black', width=900, height=675)
        self.background_canvas.pack(fill="both", expand=True)

        # canvas text boxes global variables used in order to clear
        self.text = self.background_canvas.create_text(175, 100, text='', font=('Helvetica', 14), anchor='nw')
        self.point_box = self.background_canvas.create_text(620, 10, text=self.game.get_total_points(),
                                                                fill='white', font=('Helvetica', 14), anchor='nw')
        self.rounds = self.background_canvas.create_text(750, 10, text=self.game.get_rounds(), fill='white',
                                                             font=('Helvetica', 14), anchor='nw')
        # call methods to display buttons, text and background images
        self.right_button()
        self.left_button()
        self.display_background_image()
        self.display_text_box()
        self.display_text()
        self.display_points()
        self.display_rounds()


    def left_button(self):
        '''
        Creates the left door button
        '''

        # creates the button widget
        if platform.system() == 'Darwin':
            self.left_door_button = tkmac.Button(self.game_frame, text='Left Door', bg='black', fg='#f2edcf',
                                                width=150, height=75, command=self.left_door_event)
        else:
            self.left_door_button = tk.Button(self.game_frame, text='Left Door', bg='black', fg='#f2edcf', width=25, height=5, command=self.left_door_event)

        # adds button widget to a new window on the background canvas
        self.left_button_window = self.background_canvas.create_window(250, 500, anchor='nw', window=self.left_door_button)


    def right_button(self):
        '''
        Creates the right door button
        '''

        # create button widget
        if platform.system() == 'Darwin':
            self.right_door_button = tkmac.Button(self.game_frame, text='Right Door', bg='black', fg='#f2edcf',
                                               width=150, height=75, command=self.right_door_event)
        else:
            self.right_door_button = tk.Button(self.game_frame, text='Left Door', bg='black', fg='#f2edcf',
                                               width=25, height=5, command=self.right_door_event)

        # add button widget to a new window on the background canvas
        self.right_button_window = self.background_canvas.create_window(475, 500, anchor='nw', window=self.right_door_button)


    def display_background_image(self):
        '''
        uses canvas object to display a background image
        '''

        # get background image
        background_image = tk.PhotoImage(file="images/Door.png")

        #set image in canvas
        self.background_canvas.create_image(0,0, image=background_image, anchor="nw")

        # keep a reference of the image object
        self.background_canvas.image = background_image


    def display_text(self, message=None, font_size=14):
        '''
        displays center message box
        :param data: message to be displayed
        :param font_size: text font size, default value = 14
        '''

        data = 'You see a lever in the center of the room, in front of that lever are \n' \
               'two doors. The left door has a {:.2f} chance that it contains a  treasure\n' \
               'chest, otherwise a poison dart trap. The right door has a 100% chance \n' \
               'that it does not contain a trap or treasure but another lever that \n' \
               'will lead you to another room with higher rewards. What do you do?'.format(self.game.get_current_percentage())
        message = data if message == None else message
        if platform.system() == 'Darwin':
            self.text = self.background_canvas.create_text(175, 100, text=message, font=('Helvetica', 18),
                                                           anchor='nw', fill='black')
        else:
            self.text = self.background_canvas.create_text(175, 100, text=message, font=('Helvetica', font_size),
                                                           anchor='nw')


    def display_text_box(self):
        ''' Creates a text box with a background image '''

        text_box = self.background_canvas.create_image(125, 50, image=self.text_box_background, anchor='nw')


    def display_points(self):
        ''' Displays the players current total points.  '''

        point_message = 'Points: {}'.format(self.game.get_total_points())
        if platform.system() == 'Darwin':
            self.point_box = self.background_canvas.create_text(500,10, text=point_message, fill='white',
                                                            font=('Helvetica', 20), anchor='nw')
        else:
            self.point_box = self.background_canvas.create_text(500, 10, text=point_message, fill='white',
                                                            font=('Helvetica', 14), anchor='nw')
        point_bg_box = self.background_canvas.create_rectangle(self.background_canvas.bbox(self.point_box), fill='black')
        self.background_canvas.tag_lower(point_bg_box, self.point_box)


    def display_rounds(self):
        ''' Displays the  '''
        round_message = 'Current Round: {}'.format(self.game.get_rounds())
        if platform.system() == 'Darwin':
            self.rounds = self.background_canvas.create_text(700,10, text=round_message, fill='white',
                                                         font=('Helvetica', 20), anchor='nw')
        else:
            self.rounds = self.background_canvas.create_text(700, 10, text=round_message, fill='white',
                                                             font=('Helvetica', 14), anchor='nw')
        rounds_box = self.background_canvas.create_rectangle(self.background_canvas.bbox(self.rounds), fill='black')
        self.background_canvas.tag_lower(rounds_box, self.rounds)


    def right_door_event(self):
        '''
        right door button event calls the game instance to activate event.
        Clears screen and re-displays with current info.
        '''

        # activate the right door game event
        self.game.right_door_event()

        # record current game to csv file
        self.game.record_game()

        # clear canvas text and rounds
        self.clear_all()

        # re-display rounds and scenario text
        self.display_all()

        # check if game is over
        if self.game.get_rounds() == 50:
            self.game_over()
        # check if the right door has been chosen 5 times
        elif self.game.get_right_count() == 5:
            self.right_door_button['state'] = 'disabled'


    def left_door_event(self):
        ''' Left door event calls game instance to activate event. Clears and re-displays screen with current info '''

        # activate the left door game event
        self.game.left_door_event()

        # record current game to csv file
        self.game.record_game()

        # clear canvas
        self.clear_all()

        # re-display new information
        self.display_all()

        # check if game is over
        if self.game.get_rounds() == 50:
            self.game_over()
        # check if the right door has not been chosen 5 times
        if self.game.get_right_count() < 5:
            self.right_door_button['state'] = 'normal'


    def game_over(self):
        ''' When all rounds have been used, the buttons are disabled and total points are shown '''

        # clear canvas text and rounds
        self.clear_all()

        # display new message
        message = '\n\t Thank you for participating\n\n\tTotal Points: {}'.format(self.game.get_total_points())
        self.display_text(message, 20)


    def hide_frame(self):
        ''' hides self (frame) from the screen. Allows for transition through pages '''

        self.pack_forget()


    def clear_all(self):
        ''' Clears all canvas objects from screen '''

        # clear canvas text objects
        self.background_canvas.delete(self.point_box)
        self.background_canvas.delete(self.rounds)
        self.background_canvas.delete(self.text)

        # clear canvas buttons
        self.background_canvas.delete(self.right_button_window)
        self.background_canvas.delete(self.left_button_window)


    def display_all(self):
        ''' Displays all canvas objects on the screen '''

        self.display_rounds()
        self.display_points()
        self.display_text()
        self.right_button()
        self.left_button()
