import random
import os
import csv

REWARD_POINTS    = 10           # represents the amount of points given to players for finding a treasure chest
BONUS_POINTS     = 0            # represents the amount of bonus points for chosing the right door
PERCENTAGE       = 0.60         # probability of getting a treasure chest
ROUNDS           = 0           # number of game rounds
BONUS_PERCENTAGE = 0.0          # probability that should be deducted from the base percentage
RIGHT_COUNT      = 0            # number of times the right door has been chosen

class Game:

    def __init__(self):
        self.__right_chosen     = 0
        self.__left_chosen      = 0
        self.__total_points     = 0
        self.__reward_points    = REWARD_POINTS
        self.__rounds           = ROUNDS
        self.__percentage       = PERCENTAGE
        self.__bonus_percentage = BONUS_PERCENTAGE
        self.__bonus_points     = BONUS_POINTS
        self.__right_count      = RIGHT_COUNT


    def get_total_points(self) -> int:
        ''' Returns the total number of points '''

        return self.__total_points


    def get_right_chosen(self) -> int:
        ''' Returns the number of times right choice was chosen '''

        return self.__right_chosen


    def get_left_chosen(self) -> int:
        ''' Returns the number of times left choice was chosen '''

        return self.__left_chosen


    def get_percentage(self) -> int:
        ''' Returns the float number representing the percentage '''

        return self.__percentage


    def get_rounds(self) -> int:
        ''' Returns the int number of current rounds '''

        return self.__rounds


    def get_current_percentage(self) -> float:
        ''' Returns the current percentage -> base percentage - bonus percentage '''

        return self.__percentage - self.__bonus_percentage


    def get_right_count(self) -> int:
        ''' Returns an int value representing the number of times the right door was chosen '''

        return self.__right_count


    def increment_rounds(self) -> None:
        ''' increments current rounds by 1 '''

        self.__rounds += 1


    def increment_bonus_points(self) -> None:
        ''' Increments the bonus points by 5 '''

        self.__bonus_points += 5


    def right_chosen(self) -> None:
        ''' boolean/ 1 the right door was chosen, 0 left door was chosen(only one door can be chosen) '''

        self.__right_chosen = 1
        self.__left_chosen = 0


    def left_chosen(self) -> None:
        ''' boolean/ 0 the right door was chosen, 1 left door was chosen(only one door can be chosen) '''

        self.__left_chosen = 1
        self.__right_chosen = 0


    def increment_bonus_percentage(self) -> None:
        ''' Increments the bonus percentage by 5% '''

        self.__bonus_percentage += 0.05


    def reset(self) -> None:
        ''' resets bonus_percentage, bonus_points and right_count back to base values '''

        self.__bonus_percentage = BONUS_PERCENTAGE
        self.__bonus_points     = BONUS_POINTS
        self.__right_count      = RIGHT_COUNT


    def left_door_event(self) -> None:
        ''' handles event for when the left door button is chosen. '''

        if random.random() > self.get_current_percentage():
            self.__total_points -= 10
        else:
            self.__total_points += (self.__reward_points + self.__bonus_points)
        if self.__right_count == 5:
            self.reset()
        self.left_chosen()
        self.increment_rounds()


    def right_door_event(self) -> None:
        ''' Handles right door event when the right door button is chosen '''

        self.__right_count += 1
        self.increment_bonus_percentage()
        self.increment_bonus_points()
        self.right_chosen()
        self.increment_rounds()


    def record_game(self) -> None:
        '''
        Record the end results of the game into a pre-existing csv file
        '''

        # header information and current game data
        header = ['Right Chosen',
                  'Left Chosen',
                  'Total Points',
                  'Rounds',
                  'Percentage']
        data   = [self.get_right_chosen(),
                  self.get_left_chosen(),
                  self.get_total_points(),
                  self.get_rounds(),
                  self.get_current_percentage()]

        # check if csv exists, if yes then append, else create new with header
        if os.path.exists('game_data.csv'):
            with open('game_data.csv', 'a', newline='') as f:
                file_writer = csv.writer(f)
                file_writer.writerow(data)
        else:
            with open('game_data.csv', 'a', newline='') as f:
                file_writer = csv.writer(f)
                file_writer.writerow(header)
                file_writer.writerow(data)
