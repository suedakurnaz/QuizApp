import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import json

from quiz_logic import QuizManager

class StyledQuizApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Python Quiz App")
        self.root.geometry("800x600")
        self.root.configure(bg="#2c3e50")

        self.username = ""
        self.avatar_path = ""
        self.animal_files = [
            "animal1.png", "animal2.png", "animal3.png",
            "animal4.png", "animal5.png", "animal6.png"
        ]
        self.selected_avatar_index = None
        self.question_index = 0

        with open("questions.json", "r", encoding="utf-8") as f:
            self.questions = json.load(f)
        self.manager = QuizManager(self.questions)

        self.score = 0
        self.user_answers = []
        self.option_buttons = []

        self.start_screen()
        self.root.mainloop()

    def start_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Adınızı Girin:", bg="#2c3e50", fg="white", font=("Arial", 14)).pack(pady=10)

        self.name_entry = tk.Entry(self.root, font=("Arial", 12))
        self.name_entry.pack(pady=5)

        tk.Label(self.root, text="Avatarınızı Seçin:", bg="#2c3e50", fg="white", font=("Arial", 14)).pack(pady=10)

        avatar_frame = tk.Frame(self.root, bg="#2c3e50")
        avatar_frame.pack(pady=10)

        self.avatar_buttons = []
        for i, file in enumerate(self.animal_files):
            path = os.path.join("animals", file)
            if os.path.exists(path):
                img = Image.open(path).resize((80, 80))
                photo = ImageTk.PhotoImage(img)
                btn = tk.Button(avatar_frame, image=photo, command=lambda i=i: self.select_avatar(i))
                btn.image = photo
                btn.grid(row=0, column=i, padx=5)
                self.avatar_buttons.append(btn)

        tk.Button(self.root, text="Quiz'e Başla", font=("Arial", 12), command=self.start_quiz).pack(pady=20)

    def select_avatar(self, index):
        self.selected_avatar_index = index
        self.avatar_path = os.path.join("animals", self.animal_files[index])

    def start_quiz(self):
        name = self.name_entry.get().strip()
        if name:
            self.username = name
            self.show_question()

    def show_question(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.option_buttons = []

        if self.avatar_path:
            avatar_img = Image.open(self.avatar_path).resize((100, 100))
            self.avatar_photo = ImageTk.PhotoImage(avatar_img)
            tk.Label(self.root, image=self.avatar_photo, bg="#2c3e50").pack(pady=(10, 5))

        question_data = self.questions[self.question_index]

        tk.Label(self.root, text=f"Exercise: {question_data['topic']}",
                 font=("Arial", 16, "bold"), fg="white", bg="#2c3e50").pack(pady=(5, 5))

        tk.Label(self.root, text=question_data["question"],
                 font=("Arial", 14), fg="white", bg="#2c3e50", wraplength=700, justify="center").pack(pady=(5, 15))

        for option in question_data["options"]:
            btn = tk.Button(self.root, text=option, width=50, font=("Arial", 12),
                            bg="white", command=lambda opt=option: self.check_answer(opt))
            btn.pack(pady=5)
            self.option_buttons.append(btn)

        # İlerleme çubuğu geri eklendi
        progress = ((self.question_index + 1) / len(self.questions)) * 100
        self.progress_bar = ttk.Progressbar(self.root, length=600, mode='determinate')
        self.progress_bar['value'] = progress
        self.progress_bar.pack(pady=20)

    def check_answer(self, selected):
        correct = self.questions[self.question_index]["answer"]

        for btn in self.option_buttons:
            if btn['text'] == correct:
                btn.configure(bg="green", fg="white")
            elif btn['text'] == selected:
                btn.configure(bg="red", fg="white")

        if selected == correct:
            self.score += 1

        self.user_answers.append({
        "question": self.questions[self.question_index]["question"],
        "selected": selected,
        "answer": correct,
        "topic": self.questions[self.question_index]["topic"],
        "is_correct": selected == correct
        })    
        

        for btn in self.option_buttons:
            btn.configure(state="disabled")

        self.root.after(1000, self.next_question)



    def next_question(self):
        self.question_index += 1
        if self.question_index < len(self.questions):
            self.show_question()
        else:
            print("Tüm sorular bitti. Sonuç ekranı gösteriliyor.")
            self.show_result()

    
    
    
    def show_result(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Avatar gösterimi
        if self.avatar_path:
            avatar_img = Image.open(self.avatar_path).resize((100, 100))
            self.avatar_photo = ImageTk.PhotoImage(avatar_img)
            avatar_label = tk.Label(self.root, image=self.avatar_photo, bg="#2c3e50")
            avatar_label.pack(pady=(30, 10))

        # Başlık ve skor bilgisi
        title = tk.Label(self.root, text=f"🎉 Tebrikler, {self.username}!", font=("Arial", 20, "bold"),
                         fg="white", bg="#2c3e50")
        title.pack(pady=(0, 5))

        score = tk.Label(self.root, text=f"📊 Skorunuz: {self.score} / {len(self.questions)}", font=("Arial", 14),
                         fg="white", bg="#2c3e50")
        score.pack(pady=(0, 20))

        # Konu bazlı yanlış analizi
        wrong_by_topic = {}
        for answer in self.user_answers:
              if not answer["is_correct"]:
                wrong_by_topic[answer["topic"]] = wrong_by_topic.get(answer["topic"], 0) + 1


        table_frame = tk.Frame(self.root, bg="#2c3e50")
        table_frame.pack(pady=10)

        tk.Label(table_frame, text="🚧 Geliştirmen Gereken Konular", font=("Arial", 14, "bold"), width=30, fg="white", bg="#2980b9").grid(row=0, column=0)
        tk.Label(table_frame, text="Yanlış Sayısı", font=("Arial", 14, "bold"), width=15, fg="white", bg="#2980b9").grid(row=0, column=1)

        for i, (topic, count) in enumerate(wrong_by_topic.items(), start=1):
            tk.Label(table_frame, text=topic, font=("Helvetica", 11), width=30, fg="white", bg="#34495e").grid(row=i, column=0)
            tk.Label(table_frame, text=str(count), font=("Helvetica", 11), width=15, fg="white", bg="#34495e").grid(row=i, column=1)

            
        if not wrong_by_topic:
            no_mistake = tk.Label(self.root, text="🎉 Harika! Tüm konularda başarılı oldunuz.", font=("Arial", 14),
                                  fg="white", bg="#2c3e50")
            no_mistake.pack(pady=10)

        # Kapat butonu
        close_btn = tk.Button(self.root, text="Kapat", font=("Arial", 12), command=self.root.destroy, bg="white")
        close_btn.pack(pady=30)
