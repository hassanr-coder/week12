'''
Rayaan Hassan
CMSC 111
Spring 2026
Week 12 Assignment 3
Code Helper - Gemini Google Ai
'''

import random
import tkinter as tk
from tkinter import PhotoImage

# Set up the main window
root = tk.Tk()
root.title("Dice Simulator")


def roll_dice():
	# Generate two random integers between 1 and 6 to simulate rolling two dice
	die1 = random.randint(1, 6)
	die2 = random.randint(1, 6)

	# Update the images in the labels 
	new_img1 = PhotoImage(file=f"dice_{die1}.png")
	new_img2 = PhotoImage(file=f"dice_{die2}.png")

	label1.config(image=new_img1)
	label1.image = new_img1  # Keep a reference.
	label2.config(image=new_img2)
	label2.image = new_img2  # Keep a reference.

	# print results to the terminal
	print(f"Rolled: {die1} and {die2}")


# Load initial placeholder images for the dice
img1 = PhotoImage(file='dice_1.png')
img2 = PhotoImage(file='dice_1.png')

# Layout for the dice images
dice_frame = tk.Frame(root)
dice_frame.pack(pady=20)

label1 = tk.Label(dice_frame, image=img1)
label1.image = img1  
label1.pack(side="left", padx=5)

label2 = tk.Label(dice_frame, image=img2)
label2.image = img2
label2.pack(side="left", padx=5)

# Instruction text
instruction_label = tk.Label(root, text="Click to Roll the Dice", font=("Arial", 14))
instruction_label.pack(pady=10)

# Roll Button
roll_button = tk.Button(root, text="🎲 Roll Dice 🎲", font=("Arial", 14), command=roll_dice)
roll_button.pack(pady=20)

root.mainloop() #