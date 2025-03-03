import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Import for image handling

class RiddleGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Riddle Solving Game")
        self.window.geometry("600x400")  # Set window size
        
        # Load background image
        self.bg_image = Image.open("children_bg.png")  
        self.bg_image = self.bg_image.resize((600, 400), Image.LANCZOS)  # Resize to fit window
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        
        # Create a canvas and place background image
        self.canvas = tk.Canvas(self.window, width=600, height=400)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        self.riddles = [
            {"question": "What has keys but can't open locks?", "answer": "Piano", "hint": "It's a musical instrument."},
            {"question": "What has a head, a tail, but no body?", "answer": "Coin", "hint": "You carry it in your pocket."},
            {"question": "What comes once in a minute, twice in a moment, but never in a thousand years?", "answer": "The letter M", "hint": "It’s a letter of the alphabet."}
        ]
        self.current_riddle_index = 0

        # Create UI elements
        self.question_label = tk.Label(self.window, text=self.riddles[self.current_riddle_index]["question"], 
                                       font=("Arial", 14, "bold"), bg="#FFD700", fg="black", wraplength=500)
        self.answer_entry = tk.Entry(self.window, font=("Arial", 14))

        self.submit_button = tk.Button(self.window, text="Submit Answer", font=("Arial", 12, "bold"), bg="lightblue", command=self.check_answer)
        self.hint_button = tk.Button(self.window, text="Hint", font=("Arial", 12, "bold"), bg="lightgreen", command=self.show_hint)
        self.exit_button = tk.Button(self.window, text="Exit", font=("Arial", 12, "bold"), bg="red", command=self.exit_game)

        # Place widgets on canvas
        self.canvas.create_window(300, 50, window=self.question_label)
        self.canvas.create_window(300, 120, window=self.answer_entry, width=250, height=30)
        self.canvas.create_window(300, 170, window=self.submit_button, width=150)
        self.canvas.create_window(300, 220, window=self.hint_button, width=150)
        self.canvas.create_window(300, 270, window=self.exit_button, width=150)

    def check_answer(self):
        user_answer = self.answer_entry.get().strip()
        correct_answer = self.riddles[self.current_riddle_index]["answer"]

        if user_answer.lower() == correct_answer.lower():
            messagebox.showinfo("Correct!", "That's the right answer!")
            self.next_riddle()
        else:
            messagebox.showerror("Wrong Answer", "Oops! Try again.")

    def show_hint(self):
        hint = self.riddles[self.current_riddle_index]["hint"]
        messagebox.showinfo("Hint", hint)

    def next_riddle(self):
        self.current_riddle_index += 1
        if self.current_riddle_index < len(self.riddles):
            self.question_label.config(text=self.riddles[self.current_riddle_index]["question"])
            self.answer_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Congratulations!", "You've solved all the riddles!")
            self.window.quit()  # Exit the game

    def exit_game(self):
        self.window.quit()  # Close the game window

    def run(self):
        self.window.mainloop()

# Create and start the game
game = RiddleGame()
game.run()
