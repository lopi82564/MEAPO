import tkinter as tk

root = tk.Tk()
root.title("Дуги и секторы")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

canvas.create_oval(50, 50, 350, 350, fill="lightgray")

canvas.create_arc(70, 70, 350, 350, start=100, extent=40, style=tk.ARC, outline="red", width=3)
canvas.create_arc(50, 50, 350, 350, start=240, extent=90, style=tk.CHORD, outline="blue", width=3, fill="blue")
canvas.create_arc(50, 50, 350, 350, start=0, extent=60, style=tk.PIESLICE, outline="green", width=3, fill="green")
canvas.create_arc(50, 50, 350, 350, start=160, extent=30, style=tk.PIESLICE, outline="purple", width=3, fill="purple")

root.mainloop()
