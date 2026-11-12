import tkinter as tk
import random

# Game settings
WIDTH = 600
HEIGHT = 400
SIZE = 20

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="green")
        self.canvas.pack()
        
        self.direction = "Right"
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.food = self.create_food()
        self.score = 0
        
        self.label = tk.Label(root, text=f"Score: {self.score}", font=("Arial", 14))
        self.label.pack()
        
        self.root.bind("<KeyPress>", self.change_direction)
        self.update_game()

    def create_food(self):
        x = random.randint(0, (WIDTH // SIZE) - 1) * SIZE
        y = random.randint(0, (HEIGHT // SIZE) - 1) * SIZE
        return (x, y)

    def change_direction(self, event):
        key = event.keysym
        if key == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif key == "Down" and self.direction != "Up":
            self.direction = "Down"
        elif key == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif key == "Right" and self.direction != "Left":
            self.direction = "Right"

    def update_game(self):
        head_x, head_y = self.snake[0]
        
        if self.direction == "Up":
            head_y -= SIZE
        elif self.direction == "Down":
            head_y += SIZE
        elif self.direction == "Left":
            head_x -= SIZE
        elif self.direction == "Right":
            head_x += SIZE
            
        new_head = (head_x, head_y)

        # Game Over check
        if (head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT or new_head in self.snake):
            self.canvas.create_text(WIDTH/2, HEIGHT/2, text=f"GAME OVER!\nScore: {self.score}", fill="white", font=("Arial", 24), justify="center")
            return

        self.snake.insert(0, new_head)

        # Food khaya?
        if new_head == self.food:
            self.score += 1
            self.label.config(text=f"Score: {self.score}")
            self.food = self.create_food()
        else:
            self.snake.pop()

        # Drawing
        self.canvas.delete("all")
        # Food
        self.canvas.create_oval(self.food[0], self.food[1], self.food[0]+SIZE, self.food[1]+SIZE, fill="red")
        # Snake
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x+SIZE, y+SIZE, fill="black")

        self.root.after(100, self.update_game)

# Game start karo
root = tk.Tk()
game = SnakeGame(root)
root.mainloop()