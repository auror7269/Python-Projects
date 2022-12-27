
class QuizBrain:
    def __init__(self, q_list ):
        self.ques = None
        self.question_num = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_num < len(self.question_list)

    def next_question(self):
        ques = self.question_list[self.question_num]
        self.question_num += 1
        user_answer = input(f"Q.{self.question_num}: {ques.text} (True/False): ")
        self.check_answer(user_answer, ques.ans)

    def check_answer(self, us_ans, correct_ans):
        if us_ans.lower() == correct_ans.lower():
            print("You got it Right !")
            self.score += 1
        else:
            print("That's Wrong")
        print(f"The correct answer was {correct_ans}")
        print(f"Your score is {self.score}/{self.question_num}")
        print("\n")








