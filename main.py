import tkinter as tk
from tkinter import messagebox
import json
import random

class QuizApp:
    def __init__(self, root):
        # Main window setup
        self.root = root
        self.root.title("Quiz Application")
        self.root.geometry("600x500")
        self.root.config(bg="white")

        # Quiz variables
        self.score = 0
        self.current_q_index = 0
        self.timer_sec = 15
        self.questions = []
        # 7yrjf
        self.timer_running = False

        # Load questions from JSON file
        try:
            with open('questions.json', 'r') as f:
                self.data = json.load(f)
        except:
            messagebox.showerror("Error", "questions.json file not found!")
            root.destroy()

        # Title Label
        tk.Label(root, text="Quiz Application",
                 font=("Arial", 20, "bold"),
                 bg="white", fg="black").pack(pady=10)

        # -------- Category Selection Frame --------
        self.cat_frame = tk.Frame(root, bg="white")
        self.cat_frame.pack(pady=20)

        tk.Label(self.cat_frame, text="Select Category:",
                 font=("Arial", 12),
                 bg="white", fg="black").pack(pady=10)

        # Create buttons for each category
        for cat in self.data.keys():
            tk.Button(self.cat_frame,
                      text=cat,
                      font=("Arial", 11),
                      bg="lightblue",
                      fg="black",
                      width=20,
                      command=lambda c=cat: self.start_quiz(c)).pack(pady=5)

        # -------- Quiz Frame (Hidden initially) --------
        self.quiz_frame = tk.Frame(root, bg="white")

        # Timer Label
        self.label_timer = tk.Label(self.quiz_frame,
                                   text="",
                                   font=("Arial", 12, "bold"),
                                   fg="red",
                                   bg="white")
        self.label_timer.pack(pady=5)

        # Question Label
        self.label_ques = tk.Label(self.quiz_frame,
                                  text="",
                                  font=("Arial", 14, "bold"),
                                  wraplength=500,
                                  fg="black",
                                  bg="white",
                                  justify="left")
        self.label_ques.pack(pady=20)

        # Variable to store selected option
        self.var_opt = tk.StringVar()
# hello isse karo jor se
        # Option buttons (Radio buttons styled as normal buttons)
        self.options_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(self.quiz_frame,
                                text="",
                                variable=self.var_opt,
                                value="",
                                font=("Arial", 12),
                                bg="lightgray",
                                fg="black",
                                selectcolor="lightgreen",
                                indicatoron=0,  # makes it look like button
                                width=40,
                                pady=5)
            rb.pack(pady=5)
            self.options_buttons.append(rb)

        # Submit Button
        self.btn_next = tk.Button(self.quiz_frame,
                                 text="Submit Answer",
                                 command=self.check_ans,
                                 font=("Arial", 12, "bold"),
                                 bg="green",
                                 fg="white",
                                 width=20)
        self.btn_next.pack(pady=20)

    # Function to start quiz after selecting category
    def start_quiz(self, category):
        self.questions = self.data[category]
        random.shuffle(self.questions)  # Shuffle questions

        self.cat_frame.pack_forget()  # Hide category screen
        self.quiz_frame.pack()        # Show quiz screen

        self.show_question()

    # Function to display question
    def show_question(self):
        self.timer_sec = 15  # Reset timer

        if self.current_q_index < len(self.questions):
            self.var_opt.set(None)  # Clear previous selection

            q_data = self.questions[self.current_q_index]

            # Display question text
            self.label_ques.config(
                text=f"Q{self.current_q_index+1}: {q_data['q']}"
            )

            # Display options
            opts = q_data['options']
            for i in range(4):
                if i < len(opts):
                    self.options_buttons[i].config(
                        text=opts[i],
                        value=opts[i],
                        state="normal"
                    )
                    self.options_buttons[i].pack()
                else:
                    self.options_buttons[i].pack_forget()

            # Start timer
            if not self.timer_running:
                self.timer_running = True
                self.update_timer()
        else:
            self.show_result()

    # Timer function (runs every 1 second)
    def update_timer(self):
        if self.timer_sec > 0:
            self.label_timer.config(
                text=f"Time Left: {self.timer_sec}s"
            )
            self.timer_sec -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            self.score -= 1  # Penalty for timeout
            self.next_question()

    # Check selected answer
    def check_ans(self):
        selected = self.var_opt.get()

        # If no option selected
        if not selected:
            messagebox.showwarning("Warning", "Please select an answer!")
            return

        correct = self.questions[self.current_q_index]['ans']

        # Update score
        if selected == correct:
            self.score += 4
        else:
            self.score -= 1

        self.next_question()

    # Move to next question
    def next_question(self):
        self.root.after_cancel(self.timer_id)  # Stop timer
        self.timer_running = False
        self.current_q_index += 1
        self.show_question()

    # Show final result
    def show_result(self):
        self.quiz_frame.pack_forget()

        tk.Label(self.root,
                 text=f"Quiz Finished!\nYour Score: {self.score}",
                 font=("Arial", 18, "bold"),
                 bg="white",
                 fg="black").pack(pady=50)

        # Save score to file
        with open("leaderboard.txt", "a") as f:
            f.write(f"Score: {self.score}\n")

        tk.Button(self.root,
                  text="Exit",
                  command=self.root.destroy,
                  bg="red",
                  fg="white").pack()


# Run application
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()