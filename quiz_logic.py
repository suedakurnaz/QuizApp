import json

class QuizManager:
    def __init__(self):
        with open("questions.json", "r") as f:
            self.questions = json.load(f)

    def get_question(self, index):
        return self.questions[index]

    def check_answer(self, index, selected):
        return self.questions[index]["answer"] == selected

    def total_questions(self):
        return len(self.questions)