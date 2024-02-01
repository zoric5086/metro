import tkinter as tk
from PIL import Image, ImageTk

class SpriteAnimation(tk.Tk):
    def __init__(self, sprite_path, sprite_width, sprite_height, columns, rows, frames):
        super().__init__()

        self.sprite_width = sprite_width
        self.sprite_height = sprite_height
        self.columns = columns
        self.rows = rows
        self.frames = frames

        self.canvas = tk.Canvas(self, width=self.sprite_width, height=self.sprite_height)
        self.canvas.pack()

        self.sprite_image = Image.open(sprite_path)
        self.sprites = self.get_sprites()

        self.current_frame = 0

        self.bind("<Right>", self.start_animation)

    def get_sprites(self):
        sprites = []
        tmp_frame =1
        for row in range(self.rows):
            for col in range(self.columns):
                x = col * self.sprite_width
                y = row * self.sprite_height
                sprite = self.sprite_image.crop((x, y, x + self.sprite_width, y + self.sprite_height))
                sprite = ImageTk.PhotoImage(sprite)
                tmp_frame = tmp_frame +1
                if tmp_frame < self.frames:
                    sprites.append(sprite)
        return sprites

    def animate(self):
        self.canvas.delete("all")
        print(self.current_frame)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.sprites[self.current_frame])
        if self.current_frame < self.frames-3:
            self.current_frame = (self.current_frame + 1) % (self.columns * self.rows)
        else:
            self.current_frame =0

            # self.after(50, self.animate)  # Changez la durée entre chaque frame en millisecondes (ajustez selon vos besoins)

    def start_animation(self, event):
        self.animate()

if __name__ == "__main__":
    sprite_path = "sprite.png"  # Remplacez par le chemin de votre fichier PNG
    sprite_width = 127
    sprite_height = 147
    #143.9345
    columns = 7
    rows = 4
    frames = 27

    app = SpriteAnimation(sprite_path, sprite_width, sprite_height, columns, rows, frames)
    app.mainloop()
