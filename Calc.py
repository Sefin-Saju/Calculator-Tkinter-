import tkinter as tk

def click(event):
    text=event.widget.cget("text")

    if text =="=":
        try:
            result=str(eval(screen.get()))
            screen.set(result)
        except:
            screen.set("Error")
    elif text =="C":
        screen.set("")
    else:
        screen.set(screen.get() + text)


root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="Arial 20", justify="right")
entry.pack(fill="both", ipadx=8, pady=10, padx=10)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn in row:
        b = tk.Button(frame, text=btn, font="Arial 18")
        b.pack(side="left", expand=True, fill="both")
        b.bind("<Button-1>",click)

root.mainloop()
