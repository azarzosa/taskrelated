import pyibl
import random

import matplotlib.pyplot as plt

from tqdm import tqdm

PARTICIPANTS = 30
ROUNDS = 50
NOISE = 0.25
DECAY = 0.5
DEFAULT_UTILITY = 30


def run(rounds, participants):
    right_taken = 0
    right_turns = [0] * rounds
    left_turns = [0] * rounds
    points_lost = [0] * rounds
    points_gained = [0] * rounds
    trap_chance = 60
    points_chance = 40
    a = pyibl.Agent(default_utility=DEFAULT_UTILITY, noise=NOISE, decay=DECAY)
    for p in tqdm(range(participants)):
        a.reset()
        for r in range(rounds):
            c = a.choose("left", "right")
            if right_taken == 5 or c == "left":
                chance = random.random()
                # left_turns[r] += 1
                if chance <= trap_chance:
                    a.respond(-10)
                    # points_lost[r] += 1
                    if right_taken == 5:
                        right_taken = 0
                    continue
                elif chance <= points_chance:
                    a.respond(10)
                    # points_gained[r] += 1
                    if right_taken == 5:
                        right_taken = 0
                    continue
            elif c == "right":
                # increase treasure chance decrease trap but reward no points
                a.respond(0)
                points_chance -= 5
                right_turns[r] += 1
    return right_turns
    # return points_gained
    # return [n / participants for n in right_turns]


def main():
    plt.plot(run(ROUNDS, PARTICIPANTS))
    plt.ylim([0, 50])
    # plt.ylabel("points gained")
    plt.ylabel("right door taken")
    plt.xlabel("round")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
