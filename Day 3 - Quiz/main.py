from ques import question_data
from ques_class import Ques
from replit import clear
from quiz_brain import QuizBrain

question_bank=[]

for questions in question_data:
    ques_text=questions["text"]
    ques_ans=questions["answer"]
    new_ques=Ques(ques_text,ques_ans)
    question_bank.append(new_ques)

clear()
quiz=QuizBrain(question_bank)
while(quiz.still_has_ques()):
    quiz.next_ques()