class QuizBrain:
    def __init__(self, q_list):
        self.question_num = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1
        user_ans = input(f"Q.{self.question_num}: {current_question.text} (True/False): ")
        self.check_answer(user_ans, current_question.answer)

    def still_has_questions(self):
        if self.question_num < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You are correct!")
            self.score += 1
        else:
            print("You are wrong")
            print(f"The correct answer is {correct_answer}")
        print(f"Your score is {self.score}/{self.question_num}\n")
