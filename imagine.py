import tkinter as tk

# Window banao
root = tk.Tk()
root.title("Meri Image")
root.geometry("400x400")
root.config(bg="white")

# Canvas banao - is par hum drawing karenge
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# 1. Ghar ki deewar
canvas.create_rectangle(100, 150, 300, 300, fill="#FFD6A5", outline="black", width=2)

# 2. Chhat
canvas.create_polygon(100, 150, 300, 150, 200, 50, fill="#FF6B6B", outline="black", width=2)

# 3. Darwaza
canvas.create_rectangle(170, 220, 230, 300, fill="#8D5524", outline="black", width=2)

# 4. Khidki
canvas.create_rectangle(120, 180, 160, 220, fill="skyblue", outline="black", width=2)

# 5. Suraj
canvas.create_oval(20, 20, 80, 80, fill="yellow", outline="orange", width=2)

# Text
canvas.create_text(200, 340, text="Ye Mera Ghar Hai!", font=("Arial", 14, "bold"))

root.mainloop()