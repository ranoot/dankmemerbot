# dankmemerbot
Bot to play the discord "Dank memer" bot game

You can edit the commands used by the bot by editing the `OPTIONS` variable
```
postmeme = lambda: "pls postmeme\n"+ choice(["n", "r", "e", "d"]) + "\n"

OPTIONS = [
    {"command": postmeme, "reset_time": 60},
    {"command": lambda: "pls fish\n", "reset_time": 45},
    {"command": lambda: "pls beg\n", "reset_time": 45}
]
```
The example above is the default options
To include a new option, create a new function that returns the string that you want to type, the simplest way to do so is using anoymous function expressions `lambda: <text>`, you can also write functions like `postmeme` that include logic.

Do include the `\n` as it tells the program to press ENTER.
