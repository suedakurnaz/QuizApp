import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import json

class StyledQuizApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("700x500")
        self.root.title("Python Quiz")
        self.username = ""
        self.avatar_path = ""
        self.questions = self.load_questions()
        self.current_question = 0
        self.score = 0
        self.user_answers = []
        self.total_questions = len(self.questions)
        self.animal_files = ["animal1.png", "animal2.png", "animal3.png", "animal4.png", "animal5.png"]
        self.start_screen()

    def load_questions(self):
        with open("questions.json", "r", encoding="utf-8") as f:
            return json.load(f)

    def start_screen(self):
        self.clear_window()
        self.root.configure(bg="#2c3e50")
        tk.Label(self.root, text="Enter Your Name:", font=("Helvetica", 14), fg="white", bg="#2c3e50").pack(pady=10)
        self.name_entry = tk.Entry(self.root, font=("Helvetica", 14))
        self.name_entry.pack(pady=5)

        tk.Label(self.root, text="Choose Your Character", font=("Helvetica", 14), fg="white", bg="#2c3e50").pack(pady=10)
        self.avatar_frame = tk.Frame(self.root, bg="#2c3e50")
        self.avatar_frame.pack()

        self.avatar_images = []
        self.avatar_buttons = []
        for i, file in enumerate(self.animal_files):
            path = os.path.join("animals", file)
            img = Image.open(path).resize((80, 80))
            photo = ImageTk.PhotoImage(img)
            self.avatar_images.append(photo)
            btn = tk.Button(self.avatar_frame, image=photo, command=lambda p=path: self.select_avatar(p))
            btn.grid(row=0, column=i, padx=10)
            self.avatar_buttons.append(btn)

        self.start_btn = tk.Button(self.root, text="Start Quiz", font=("Helvetica", 14), bg="#27ae60", fg="white", command=self.start_quiz)
        self.start_btn.pack(pady=20)

    def select_avatar(self, path):
        self.avatar_path = path
        for btn in self.avatar_buttons:
            btn.config(relief=tk.RAISED)
        idx = self.animal_files.index(os.path.basename(path))
        self.avatar_buttons[idx].config(relief=tk.SUNKEN)

    def start_quiz(self):
        name = self.name_entry.get()
        if not name.strip():
            messagebox.showwarning("Input Error", "Please enter your name.")
            return
        if not self.avatar_path:
            messagebox.showwarning("Selection Error", "Please select a character.")
            return
        self.username = name.strip()
        self.show_question()

    def show_question(self):
        self.clear_window()
        self.root.configure(bg="#2c3e50")
        question_data = self.questions[self.current_question]

        topic = question_data["topic"]
        self.topic_label = tk.Label(self.root, text=f"Exercise: {topic}", font=("Helvetica", 16, "bold"), fg="white", bg="#2c3e50")
        self.topic_label.pack(pady=10)

        self.question_label = tk.Label(self.root, text=question_data["question"], font=("Helvetica", 14), fg="white", bg="#2c3e50", wraplength=650)
        self.question_label.pack(pady=10)

        self.options_frame = tk.Frame(self.root, bg="#2c3e50")
        self.options_frame.pack()

        for opt in question_data["options"]:
            btn = tk.Button(self.options_frame, text=opt, font=("Helvetica", 12), width=60,
                            command=lambda o=opt: self.check_answer(o))
            btn.pack(pady=5)

        self.progress_canvas = tk.Canvas(self.root, width=600, height=10, bg="white", highlightthickness=0)
        self.progress_canvas.pack(pady=20)
        bar_length = int((self.current_question / self.total_questions) * 600)
        self.progress_canvas.create_rectangle(0, 0, bar_length, 10, fill="#27ae60", width=0)

    def check_answer(self, selected):
        correct = self.questions[self.current_question]["answer"]
        topic = self.questions[self.current_question]["topic"]
        self.user_answers.append({
            "question": self.questions[self.current_question]["question"],
            "topic": topic,
            "selected": selected,
            "correct": correct,
            "is_correct": selected == correct
        })

        if selected == correct:
            self.score += 1
            self.root.configure(bg="#27ae60")
        else:
            self.root.configure(bg="#c0392b")

        self.root.after(700, self.next_question)

    def next_question(self):
        self.current_question += 1
        if self.current_question < self.total_questions:
            self.show_question()
        else:
            self.show_result()

    def show_result(self):
        self.clear_window()
        self.root.configure(bg="#2c3e50")
        tk.Label(self.root, text=f"Quiz Completed, {self.username}!", font=("Helvetica", 18, "bold"), fg="white", bg="#2c3e50").pack(pady=10)
        tk.Label(self.root, text=f"Your Score: {self.score} / {self.total_questions}", font=("Helvetica", 14), fg="white", bg="#2c3e50").pack(pady=10)

        wrong_by_topic = {}
        for ans in self.user_answers:
            if not ans["is_correct"]:
                wrong_by_topic[ans["topic"]] = wrong_by_topic.get(ans["topic"], 0) + 1

        table_frame = tk.Frame(self.root, bg="#2c3e50")
        table_frame.pack(pady=10)

        tk.Label(table_frame, text="Topic", font=("Helvetica", 12, "bold"), width=30, fg="white", bg="#2980b9").grid(row=0, column=0)
        tk.Label(table_frame, text="Wrong Count", font=("Helvetica", 12, "bold"), width=15, fg="white", bg="#2980b9").grid(row=0, column=1)

        for i, (topic, count) in enumerate(wrong_by_topic.items(), start=1):
            tk.Label(table_frame, text=topic, font=("Helvetica", 11), width=30, fg="white", bg="#34495e").grid(row=i, column=0)
            tk.Label(table_frame, text=str(count), font=("Helvetica", 11), width=15, fg="white", bg="#34495e").grid(row=i, column=1)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def run(self):
        self.root.mainloop()