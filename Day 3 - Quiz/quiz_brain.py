class QuizBrain:
    def __init__(self,q_list):
        self.ques_number=0
        self.score=0
        self.ques_list=q_list

    def still_has_ques(self):
        return self.ques_number<len(self.ques_list)

    def next_ques(self):
        current_ques=self.ques_list[self.ques_number]
        user_ans=input(f"Q.{self.ques_number+1} {current_ques.text} (True/False) : ").title().strip()
        
        if(user_ans==current_ques.answer):
            print("Right")
            self.score+=1
            self.ques_number+=1
        elif(user_ans!=current_ques.answer):
            print("Wrong")
            self.ques_number+=1

        print(f"The correct answer was : {current_ques.answer}")
        print(f"Your current score is : {self.score}/{self.ques_number}")