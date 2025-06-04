import tkinter as tk
from tkinter import messagebox

TARGET_X = 200
TARGET_Y = 100
TOLERANCE = 30

class SimplePuzzle:
    def init(self, root):
        self.root = root
        self.root.title("Перевірка: Встав пазл")
        self.canvas = tk.Canvas(root, width=400, height=300, bg="white")
        self.canvas.pack()

        # Місце, куди вставити
        self.canvas.create_rectangle(TARGET_X, TARGET_Y, TARGET_X+50, TARGET_Y+50, fill="lightgray", outline="black", dash=(3, 2))
        self.piece = self.canvas.create_rectangle(50, 200, 100, 250, fill="blue")

        self.drag_data = {"x": 0, "y": 0}

        self.canvas.tag_bind(self.piece, "<ButtonPress-1>", self.start_drag)
        self.canvas.tag_bind(self.piece, "<B1-Motion>", self.do_drag)
        self.canvas.tag_bind(self.piece, "<ButtonRelease-1>", self.stop_drag)

    def start_drag(self, event):
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y

    def do_drag(self, event):
        dx = event.x - self.drag_data["x"]
        dy = event.y - self.drag_data["y"]
        self.canvas.move(self.piece, dx, dy)
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y

    def stop_drag(self, event):
        x1, y1, x2, y2 = self.canvas.coords(self.piece)
        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2

        if abs(center_x - (TARGET_X + 25)) < TOLERANCE and abs(center_y - (TARGET_Y + 25)) < TOLERANCE:
            messagebox.showinfo("Успіх", "✅ Ви людина!")
        else:
            messagebox.showerror("Помилка", "❌ Невірне розташування.")

# Запуск
if name == "main":
    root = tk.Tk()
    app = SimplePuzzle(root)
    root.mainloop()