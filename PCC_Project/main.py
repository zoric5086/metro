import subprocess
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk


def launch_program(program_path, *args):
    try:
        subprocess.run(["python", program_path] + list(args), check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error launching program: {e}")

def on_button_click(value):
        if value is not None:
            print("Entered value:", value)
        if __name__ == "__main__":
            # Example usage:
            program_path = "PCC.py"
            launch_program(program_path, str(value))


# Create the main window
root = tk.Tk()
root.overrideredirect(1)
root.title("Button Example")

# Create a button to open the prompt window


image_path = "Metro.png"  # Replace with the actual path to your image
original_image = Image.open(image_path)
width, height = 50, 50
resized_image = original_image.resize((width, height))
image0 = ImageTk.PhotoImage(resized_image)
image0 = ImageTk.PhotoImage(resized_image.convert("RGBA"))
button = tk.Button(root, image=image0, compound=tk.LEFT, command=lambda: on_button_click(0))
button.pack(pady=0)


# Load the image
image_path = "Ligne1.png"  # Replace with the actual path to your image
original_image = Image.open(image_path)
width, height = 50, 50
resized_image = original_image.resize((width, height))
image1 = ImageTk.PhotoImage(resized_image)
image1 = ImageTk.PhotoImage(resized_image.convert("RGBA"))
button = tk.Button(root,  image=image1, compound=tk.LEFT,command=lambda: on_button_click(1))
button.pack(pady=0)

image_path = "Ligne4.png"  # Replace with the actual path to your image
original_image = Image.open(image_path)
width, height = 50, 50
resized_image = original_image.resize((width, height))
image4 = ImageTk.PhotoImage(resized_image)
image4 = ImageTk.PhotoImage(resized_image.convert("RGBA"))
button = tk.Button(root, image=image4, compound=tk.LEFT, command=lambda: on_button_click(4))
button.pack(pady=0)


image_path = "Ligne14.png"  # Replace with the actual path to your image
original_image = Image.open(image_path)
width, height = 50, 50
resized_image = original_image.resize((width, height))
image14 = ImageTk.PhotoImage(resized_image)
image14 = ImageTk.PhotoImage(resized_image.convert("RGBA"))
button = tk.Button(root, image=image14, compound=tk.LEFT, command=lambda: on_button_click(14))
button.pack(pady=0)

# Start the main event loop
root.mainloop()