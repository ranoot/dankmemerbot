from math import gcd
from random import choice
from time import sleep
from pynput import keyboard

from bot import bot, findHCF, findLCM


# delcare the necessary information, change if necessary
# Commands need to be functions (no parameters)

postmeme = lambda: "pls postmeme\n"+ choice(["n", "r", "e", "d"]) + "\n"

OPTIONS = [
    {"command": postmeme, "reset_time": 60},
    {"command": lambda: "pls fish\n", "reset_time": 45},
    {"command": lambda: "pls beg\n", "reset_time": 45}
]

# Choose the key to terminate the program
TERMINATE_KEY = keyboard.Key.end


# run the file
# do not edit below this line

if __name__ == "__main__":
    controller = keyboard.Controller()
    dankbot = bot(OPTIONS, controller)

    def on_press(key): # Check when "end" key is pressed
        if key == TERMINATE_KEY:
            dankbot.proceed = False
            print('Ending Program...')
            print(f"Program Runtime: {self.runtime}")
            return False

    for i in range(6): # Countdown sequence
        if i == 5:
            print("Start!")
        else:
            print(5 - i)
            sleep(1)

    with keyboard.Listener(on_press=on_press) as listener: # Keyboard Event Listener
        while dankbot.proceed:
            dankbot.run_cycle()
        listener.join()

