class QuizManager:
    def __init__(self, questions):
        self.user_answers = []
        self.questions = questions

    def get_question(self, index):
        return self.questions[index]

    def check_answer(self, index, selected):
        return self.questions[index]["answer"] == selected
