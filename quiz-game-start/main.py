from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

list1 = []
for i in question_data:
    question_text = i["text"]
    question_ans = i["answer"]
    question1 = Question(question_text, question_ans)
    list1.append(question1)


quiz = QuizBrain(list1)
while quiz.still_has_questions():
    quiz.next_question()
print("You have completed the Quiz !!!!")
print(f"Your final score is {quiz.score}/{quiz.question_num}")
