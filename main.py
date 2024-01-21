import random

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from UI import QuizInterface

question_bank = []
num = random.randint(0, 10)
for question in question_data["results"]:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

quiz_ui = QuizInterface(quiz)
quiz_ui.question()

# while quiz.still_has_questions():
#     quiz.next_question()

if quiz.still_has_questions() is False:
    print("you've completed the quiz")
    print(f"Your final score is {quiz.score}/{quiz.question_number}")
