import pyibl
import random

import matplotlib.pyplot as plt


PARTICIPANTS = 30
ROUNDS = 50
NOISE = 0.25
DECAY = 0.5
DEFAULT_UTILITY = 5

def run() -> int:
    # keep track of everytime wait is chosen
    wait_chosen = [0] * ROUNDS
    a = pyibl.Agent(default_utility=DEFAULT_UTILITY, noise=NOISE, decay=DECAY)

    for p in range(PARTICIPANTS):
        a.reset()

        # empty dict for new participant
        delayed_responses = {}

        # keep track of previous choice
        previous = None

        for r in range(ROUNDS):
            if r % 10 == 0 or r == 0:
                print(r)

                # if the previous choice was wait then give 70% chance that it will be choice again
                if previous == 'wait' and random.random() > 0.30:
                    choice = a.choose('wait')
                else:
                    choice = a.choose('wait', 'receive')

                # update previous for next round
                previous = choice

                if choice == 'receive':
                    a.respond(10)
                else:
                    # if choice is wait, delay feedback
                    delayed_responses[choice] = a.respond()
                    wait_chosen[r] += 1
                a.instances()
        # calculate payoff if the participant only choose to wait
        payoff = 15 if len(delayed_responses) == 5 else 10
        for key in delayed_responses:
            delayed_responses[key].update(payoff)

    return [ n / PARTICIPANTS for n in wait_chosen ]


def main():
    plt.plot(range(1, ROUNDS + 1), run())
    plt.ylim([0, 1])
    plt.ylabel("Probability of Wait Chosen")
    plt.xlabel("round")
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
