# PROBLEM-SOLVING SIMULATION GAME
In order to collecte data for cognitive behavior in video game rewards we created a simple single player binary choice game. This data will be used to create compare and improve our model. 
## GAME INSTRUCTIONS
This game contains 50 rounds, the purpose is to gain as many points as possible.
Each round you will be given a choice of either entering the left or right door.

If the player chooses the left door, it is possible that it contains a poison
dart trap or a treasure chest. If the player receives a poison dart trap the
player will get a point deduction. If there is a treasure then the player
will receive a point increase.

If the player chooses the right door there are no point deductions or increase,
however in the next round the probability that the player receives points for
a treasure chest is decreased and the amount of points received for a treasure
chest is increased.

The player is only allowed to choose the right door 5 times before having to
select the left door. Once the left door has been chosen the player will be
allowed to choose the right door again. When the player has chosen the right
door 5 times the bonus values will reset.
## HOW TO RUN
The gui used in the game is pythons native tkinter libarary. Both mac and windows user do not need to install this libaray. To run the game simply run the main.py file either in the terminal or in an ide. A CSV file will be generated which will contain the statistics of the game played by the user.
### MAC USERS
Mac users will need to install the python libarary tkmacosx either using 'pip install tkmacosx' or installing it as a package into your ide.
### WINDOWS USERS
Do not need to install anything

