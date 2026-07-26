def open_console():
    print("=== Developer Console ===")
    print("Type your debug commands here (implement your own parser).")

tk.Button(root, text="Developer Console", command=open_console).pack(pady=5)
commands = {
    "god": lambda: print("God Mode enabled"),
    "fly": lambda: print("Fly Mode enabled"),
    "givecoins": lambda: print("Added 1000 test coins"),
}

def run_command(cmd):
    cmd = cmd.lower().strip()
    if cmd in commands:
        commands[cmd]()
    else:
        print("Unknown command")
