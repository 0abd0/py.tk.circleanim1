import tkinter as tk
import random
import math


class CircleAnimation:
    def __init__(self, root):
        self.root = root
        self.root.title("Circle Animation")

        self.canvas = tk.Canvas(root, width=600, height=600, bg="white")
        self.canvas.pack()

        self.radius = 100
        self.num_fragments = 20
        self.angle_step = 360 / self.num_fragments
        self.speed = 100
        self.squares = []
        self.animation_running = True
        self.move_to_center = False

        self.colors = ["white", "red", "black", "green"]

        self.speed_scale = tk.Scale(root, from_=10, to=1000, label="Speed", orient="horizontal")
        self.speed_scale.set(self.speed)
        self.speed_scale.pack()

        self.time_label = tk.Label(root, text="Time to move to center (s):")
        self.time_label.pack()

        self.time_entry = tk.Entry(root)
        self.time_entry.pack()
        self.time_entry.insert(0, "5")  # Default time is 5 seconds

        self.start_button = tk.Button(root, text="Start", command=self.start_animation)
        self.start_button.pack()

        self.toggle_button = tk.Button(root, text="Pause", command=self.toggle_animation)
        self.toggle_button.pack()

        self.create_fragments()
        self.center_text_id = self.create_center_text()

    def create_fragments(self):
        self.squares = []
        for i in range(self.num_fragments):
            angle = math.radians(i * self.angle_step)
            x = 300 + self.radius * math.cos(angle)
            y = 300 + self.radius * math.sin(angle)
            color = random.choice(self.colors)  # Randomly choose a color
            square = self.canvas.create_rectangle(x - 5, y - 5, x + 5, y + 5, fill=color, outline=color)
            self.squares.append((square, angle))

    def create_center_text(self):
        return self.canvas.create_text(300, 300, text="0abd0", font=("Courier", 20), fill="blue")

    def start_animation(self):
        move_time = int(self.time_entry.get()) * 1000  # Convert seconds to milliseconds
        self.root.after(move_time, self.enable_move_to_center)
        self.animate()

    def enable_move_to_center(self):
        self.move_to_center = True
        # Remove the center text when moving to the center starts
        self.canvas.delete(self.center_text_id)

    def animate(self):
        if not self.animation_running:
            return

        self.speed = self.speed_scale.get()
        for square, angle in self.squares:
            if self.move_to_center:
                # Move towards the center
                x = 300
                y = 300
            else:
                # Regular random movement
                length_change = random.randint(-10, 10)
                x = 300 + (self.radius + length_change) * math.cos(angle)
                y = 300 + (self.radius + length_change) * math.sin(angle)

            color = random.choice(self.colors)  # Randomly choose a color for each update
            self.canvas.coords(square, x - 5, y - 5, x + 5, y + 5)
            self.canvas.itemconfig(square, fill=color, outline=color)

        self.root.after(self.speed, self.animate)

    def toggle_animation(self):
        self.animation_running = not self.animation_running
        if self.animation_running:
            self.toggle_button.config(text="Pause")
            self.animate()
        else:
            self.toggle_button.config(text="Resume")


if __name__ == "__main__":
    root = tk.Tk()
    app = CircleAnimation(root)
    root.mainloop()
