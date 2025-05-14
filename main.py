import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import os
import json

# Dosya yolları
QUIZ_DATA_FILE = "quiz_data.json"
USERS_FILE = "users.json"
AVATAR_FOLDER = "avatars"

# Global kullanıcı bilgisi
current_user = None

# Kullanıcı verisini yükle/kaydet
if os.path.exists(USERS_FILE):
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        users_data = json.load(f)
else:
    users_data = []

def save_users():
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users_data, f, indent=2, ensure_ascii=False)

def get_user(username):
    for user in users_data:
        if user["username"] == username:
            return user
    return None

def add_user(username, avatar):
    user = {
        "username": username,
        "avatar": avatar,
        "results": {}
    }
    users_data.append(user)
    save_users()
    return user

# Quiz verisi
with open(QUIZ_DATA_FILE, "r", encoding="utf-8") as f:
    all_quiz_data = json.load(f)
all_topics = list(set([q["topic"] for q in all_quiz_data]))

# GUI
root = tk.Tk()
root.title("Quiz App")
root.geometry("750x650")

# Frames
declare_frames = ["login_frame", "start_frame", "quiz_frame", "result_frame", "main_menu_frame", "konu_listesi_frame", "konu_detay_frame"]
for name in declare_frames:
    globals()[name] = ttk.Frame(root)

# Login ekranı
avatar_images = {}
selected_avatar = tk.StringVar()
username_entry = tk.Entry(login_frame, font=("Helvetica", 14))

def load_avatars():
    row = 2
    col = 0
    for file in os.listdir(AVATAR_FOLDER):
        if file.endswith(".png"):
            img_path = os.path.join(AVATAR_FOLDER, file)
            img = Image.open(img_path).resize((50, 50))
            tk_img = ImageTk.PhotoImage(img)
            avatar_images[file] = tk_img

            btn = tk.Radiobutton(
                login_frame, image=tk_img, variable=selected_avatar, value=file
            )
            btn.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col == 6:
                row += 1
                col = 0

def handle_login():
    global current_user
    username = username_entry.get().strip()
    avatar = selected_avatar.get()
    if not username or not avatar:
        messagebox.showwarning("Uyarı", "Lütfen kullanıcı adı ve avatar seçin.")
        return

    user = get_user(username)
    if user:
        current_user = user
    else:
        current_user = add_user(username, avatar)

    login_frame.pack_forget()
    update_profile_header()
    show_main_menu()

# Login bileşenleri
ttk.Label(login_frame, text="Kullanıcı Adı:", font=("Helvetica", 14)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
username_entry.grid(row=0, column=1, pady=10)
ttk.Label(login_frame, text="Avatar Seç:", font=("Helvetica", 14)).grid(row=1, column=0, sticky="w", pady=10)
load_avatars()
ttk.Button(login_frame, text="Giriş Yap", command=handle_login).grid(row=10, column=0, columnspan=6, pady=20)

# Profil üst bilgisi
profile_frame = ttk.Frame(root)
profile_name = ttk.Label(profile_frame, font=("Helvetica", 14, "bold"))
profile_avatar_label = tk.Label(profile_frame)
profile_avatar_label.pack(side="left", padx=10)
profile_name.pack(side="left")

def update_profile_header():
    profile_name.config(text=current_user["username"])
    avatar_file = current_user["avatar"]
    img = Image.open(os.path.join(AVATAR_FOLDER, avatar_file)).resize((40, 40))
    tk_img = ImageTk.PhotoImage(img)
    profile_avatar_label.config(image=tk_img)
    profile_avatar_label.image = tk_img
    profile_frame.pack(pady=5)

def show_main_menu():
    main_menu_frame.pack(pady=50)
    ttk.Label(main_menu_frame, text="Ne yapmak istersiniz?", font=("Helvetica", 18, "bold")).pack(pady=20)
    ttk.Button(main_menu_frame, text="📝 Quiz", command=go_to_quiz).pack(pady=10, ipadx=20, ipady=10)
    ttk.Button(main_menu_frame, text="📚 Konu", command=show_konu_listesi).pack(pady=10, ipadx=20, ipady=10)

def go_to_quiz():
    main_menu_frame.pack_forget()
    start_frame.pack(pady=20)

# Quiz başlama ekranı
topic_vars = {}
ttk.Label(start_frame, text="Lütfen çözmek istediğiniz konuları seçin:", font=("Helvetica", 14)).grid(row=0, column=0, columnspan=3, pady=10)
for idx, topic in enumerate(all_topics):
    var = tk.BooleanVar()
    cb = ttk.Checkbutton(start_frame, text=topic, variable=var)
    cb.grid(row=1 + idx // 3, column=idx % 3, sticky="w", padx=10, pady=5)
    topic_vars[topic] = var

def start_quiz():
    global selected_topics, filtered_quiz_data, quiz_index, score, results_by_topic

    selected_topics = [t for t, v in topic_vars.items() if v.get()]
    if not selected_topics:
        messagebox.showwarning("Uyarı", "Lütfen en az bir konu seçin.")
        return

    filtered_quiz_data = [q for q in all_quiz_data if q["topic"] in selected_topics]
    quiz_index = 0
    score = 0
    results_by_topic = {t: {"correct": 0, "total": 0} for t in selected_topics}

    start_frame.pack_forget()
    show_question_frame()

ttk.Button(start_frame, text="Start Quiz", command=start_quiz).grid(row=10, column=1, pady=20)

# Quiz ekranı
qs_label = ttk.Label(quiz_frame, wraplength=600, anchor="center")
qs_label.pack(pady=20)
choice_btns = []
for i in range(4):
    btn = ttk.Button(quiz_frame)
    btn.pack(pady=5)
    choice_btns.append(btn)

feedback_label = ttk.Label(quiz_frame)
feedback_label.pack(pady=10)
score_label = ttk.Label(quiz_frame, text="Score: 0")
score_label.pack(pady=10)

def show_question_frame():
    quiz_frame.pack(pady=20)
    show_question()

def show_question():
    if quiz_index >= len(filtered_quiz_data):
        quiz_frame.pack_forget()
        show_results()
        return

    root.config(bg="SystemButtonFace")
    question = filtered_quiz_data[quiz_index]
    qs_label.config(text=question["question"])
    feedback_label.config(text="")
    for i in range(4):
        choice_btns[i].config(text=question["choices"][i], command=lambda i=i: check_answer(i))
    score_label.config(text=f"Score: {score}/{len(filtered_quiz_data)}")

def check_answer(index):
    global quiz_index, score
    question = filtered_quiz_data[quiz_index]
    selected = question["choices"][index]
    topic = question["topic"]
    results_by_topic[topic]["total"] += 1
    if selected == question["answer"]:
        score += 1
        results_by_topic[topic]["correct"] += 1
        feedback_label.config(text="Doğru!", background="green", foreground="white")
        root.config(bg="green")
    else:
        feedback_label.config(text="Yanlış!", background="red", foreground="white")
        root.config(bg="red")
    root.after(1000, next_question)

def next_question():
    global quiz_index
    quiz_index += 1
    show_question()

# Sonuç ekranı
def show_results():
    result_frame.pack(pady=20)
    ttk.Label(result_frame, text="Quiz Sonuçları", font=("Helvetica", 18)).pack(pady=10)
    table_frame = ttk.Frame(result_frame)
    table_frame.pack()
    headers = ["Konu", "Doğru", "Toplam", "Başarı %"]
    for i, h in enumerate(headers):
        ttk.Label(table_frame, text=h, font=("Helvetica", 12, "bold")).grid(row=0, column=i, padx=10, pady=5)
    for row, (topic, data) in enumerate(results_by_topic.items(), start=1):
        correct, total = data["correct"], data["total"]
        percent = int((correct / total) * 100) if total > 0 else 0
        for col, value in enumerate([topic, correct, total, f"%{percent}"]):
            bg = "#c8e6c9" if percent >= 80 else ("#fff9c4" if percent >= 50 else "#ffcdd2")
            tk.Label(table_frame, text=value, background=bg, font=("Helvetica", 12), width=15).grid(row=row, column=col, padx=5, pady=2)
    for topic, data in results_by_topic.items():
        current_user["results"][topic] = data
    save_users()
    ttk.Label(result_frame, text=f"Toplam Başarı: %{score * 100 // len(filtered_quiz_data)}", font=("Helvetica", 16, "bold"), foreground="blue").pack(pady=20)
    ttk.Button(result_frame, text="Kapat", command=root.destroy).pack(pady=10)

# Konu listesi ve detay ekranı
konu_text = tk.Text(konu_detay_frame, wrap="word", font=("Helvetica", 12), width=80, height=25)
konu_text.pack(pady=20)
ttk.Button(konu_detay_frame, text="🔙 Geri", command=lambda: switch_frame(konu_detay_frame, konu_listesi_frame)).pack(pady=10)

with open("topics.json", "r", encoding="utf-8") as f:
    topic_contents = json.load(f)

def show_konu_listesi():
    main_menu_frame.pack_forget()
    konu_listesi_frame.pack(pady=20)

def build_konu_listesi():
    ttk.Label(konu_listesi_frame, text="Konular", font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=3, pady=10)
    for idx, topic in enumerate(all_topics):
        btn = ttk.Button(konu_listesi_frame, text=topic, width=30, command=lambda t=topic: show_konu_detay(t))
        btn.grid(row=1 + idx // 3, column=idx % 3, padx=10, pady=10)
    ttk.Button(konu_listesi_frame, text="🔙 Geri", command=lambda: switch_frame(konu_listesi_frame, main_menu_frame)).grid(row=99, column=1, pady=20)

def show_konu_detay(topic):
    konu_listesi_frame.pack_forget()
    konu_text.delete("1.0", tk.END)
    konu_text.insert(tk.END, topic_contents.get(topic, f"{topic} konusu henüz eklenmedi."))
    konu_detay_frame.pack(pady=20)

def switch_frame(hide_frame, show_frame):
    hide_frame.pack_forget()
    show_frame.pack(pady=20)

# Uygulamayı başlat
login_frame.pack(pady=30)
build_konu_listesi()
root.mainloop()
