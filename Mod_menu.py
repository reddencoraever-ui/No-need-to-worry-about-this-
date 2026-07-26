import tkinter as tk
from tkinter import messagebox

mods = {
    "God Mode": False,
    "Infinite Stamina": False,
    "Fly Mode": False,
    "No Clip": False,
}

def toggle_mod(name):
    mods[name] = not mods[name]
    status = "ON" if mods[name] else "OFF"
    print(f"{name}: {status}")

root = tk.Tk()
root.title("My Game - Debug Menu")
root.geometry("300x250")

tk.Label(root, text="Debug / Mod Menu", font=("Arial", 16)).pack(pady=10)

for mod in mods:
    tk.Checkbutton(
        root,
        text=mod,
        command=lambda m=mod: toggle_mod(m)
    ).pack(anchor="w", padx=20)

def show_status():
    text = "\n".join(
        f"{k}: {'ON' if v else 'OFF'}"
        for k, v in mods.items()
    )
    messagebox.showinfo("Current Status", text)

tk.Button(root, text="Show Status", command=show_status).pack(pady=15)

root.mainloop()
