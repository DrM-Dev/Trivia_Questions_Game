class QuizBrain:
    def __init__(self, the_question_list):
        self.answer = None
        self.real_answer = None
        self.question_number = 0
        self.current_question = None
        #-------------------
        self.question_list = the_question_list
        #-------------------
        self.player_score = 0
    #_________________________________________now time to make it ASK these questions and CHECK if your answer is RIGHT/WRONG :)
    def next_question(self):
        current_question = self.question_list[self.question_number] #------>we are referring to the objects made in that CLASS by "self"
                                                                            #and that way we can access the attributes that we MADE!!
        #self.question_number +=1 #since we detected the question number...now let's add 1 so we can get Q.1 AND to move on the next question :)
                                                                                                                    #|
        self.answer = input(f"Q.{self.question_number+1}-{current_question.q_text}, [True / False]?").lower()       #|
                                                                                                                    #|
        #_____formating input
        if self.answer == "true" or self.answer == "t":
            self.answer = "True"
        elif self.answer == "false" or self.answer == "f":
            self.answer = "False"

        self.real_answer = current_question.a_text  #FATALL mistake...no NEEDD TO CALL self. if you are taking an OBJECT FROM AN OUTSIDE SOURCE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
                                              #ALSO remember what we called the attributes for the OBJECTS we stored in the questions_bank list!
                                              #here:
                                              #      self.q_text = question
                                              #      self.a_text = answer
                                #just like in Trivia_Questions_Game.py:
        # print(question_bank[1].q_text) #--->that's how you get the question-text
        # print(question_bank[1].q_answer) #--->that's how you get the answer-text

    # _________________________________________NOW let's make a METHOD that gives True/False values depending on your answers
                        #and with it...we control a WHILE-LOOP that keeps looping through the questions using the method of [next_question]
    #|
    def checking_questions(self):
        # print(f"DEBUG: {self.answer} and {self.real_answer} ")
        # -------------
        #_______________________MOVING TO NEXT QUESTION:
        self.question_number +=1
        #_______________________
        #--------------
        if self.answer == self.real_answer:
            #-----
            self.player_score += 1
            #-----
            print("You got it right!")
            print(f"Your current score:{self.player_score}/{len(self.question_list)}")
            print("\n")
            return True
        else:
            print("Wrong :(")
            print(f"Your current score:{self.player_score}/{len(self.question_list)}")
            print(f"The correct answer is:[{self.real_answer}]")
            print("\n")
            return False


    def still_have_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            print(f"You have completed the quiz! your final score is: \n{self.player_score}")
            return False
