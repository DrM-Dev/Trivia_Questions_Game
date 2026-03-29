#Trivia_Questions_GameV   by    Dr.M-Dev:
#DATA BASES:
from database_1 import question_data          #importing dictionary-list of "text" & "answer" keys
from database_2 import question_database2
#_____________
from question_model import Question     #importing Question CLASS
from quiz_brain import QuizBrain

print('''                                                                                                                                                  
                                                              ...::::.      ...::::::::    :.      .:.   
  5@@@@@@@@B!    &@@@@@@@&G:        ^G&@@@&P#@@@@B~          J@@@@@@@@@G.   #@@@@@@@@@@   .@@B    7@@?   
  G@@~::::J@@!   @@#     B@@.      :@@G::~&@@!::Y@@~         J@@~    ^@@B   #@@.           !@@J  .@@B    
  G@@     .@@Y   @@@    5&@#       ~@@!   B@&   :@@?         J@@:     &@#   #@@BBBBBBB      P@@: #@@.    
  7BP     .@@J   PBGGGGGB@@B       :BB^   B@&   :@@?         ~GP.     &@#   JGPYYYYYYY       &@# @@!     
  Y&&^....?@@7   #&P     J@@:  ##  ^&&~   B@&   ^@@?         ?@@7:  :7@@P   Y@& ......       ^@@@@P      
  P@@@@@@@@&?    &@B     ?@@:  ##  ~@@!   B@&   :@@?         ?@@@@@@@@#J    J&@@@@@@@@?       ?@@B  


                                                             !J!:                                                                
                                                              ^G@@&P7:                                                           
                                         .~7YGB#&&&&&&&#BG5?~:  .Y@@@@&G^                                                        
                                    :?P&@@@@@@@@@@@@@@@@@@@@@@@&G?J@@@@@&                                                        
                                .!G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P   ...                                                 
                              ~B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BG&&@@@@                                              
                            ?&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&                                             
                          7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#GYP#&J                                            
                        .B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@!                                                
                       :&@@@@@@@@@@@@@@@@J7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P                                               
                      .@@@@@@@@@@@@@@@@#:  ^&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G                                              
                      #@@@@@@@@@@@@@@&7      P@@@@@@@@@@@@@B&@@@@@@@&@@#&@@@@@@@@@@J                                             
                     !@@@@@@@@@@@@@&?         ^#@@@@&&@@@@@@#PPGB##? B@5#@#@@@@@@@@@:                                            
                     B@@@@@@@@@@@G~             ^B@@@&GG#@@@@@@@#~   .&#J@Y&@@@@@@@@G                                            
                     @@@@@@@@@@~                  .?#@@@&BGPGBBJ      .#5G&J@@@@@@@@@.                                           
                   .@@@@@@@@@7      !PB##B4^        .^JG#&&P:  ^4B###P4?!~!?@@@@@@@@^                                           
                   .@@@@@@@@#      !4~.. .~4^                 ~4~....~4^    #@@@@@@@^   .~                                      
               ~BJ :@@@@@@@@BJYYYYYYJJJJYJJJJJJJ?!.     .!?JYYYJJYYYJJJYYYYY&@@@@@@@P7: .G#?.                                   
            .?BG^  &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?...5@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?  .Y#5:                                 
          :5BJ.    @@@@@@@@@&PJJJJJJ????JJJJ5&@@@@@@@@@@@@@@@GYJJ??????JJJJJYB@@@@@@@@@Y     7BB~                               
        !GG~       .YGG@@@@B        ...       G@@@@@@@@@@@@@:     .::.        !@@@@&GP7        ^G#?                             
     .JB5:             &@@@Y      4P..P@G.    7@@@@@@@@@@@@&    ^:^B@@@P.      @@@@~             .J#5.                          
     J@J               &@@@5     G@@4Y&@@&    ?@@@@?::^#@@@&   ~@4^B@@@@#     .@@@@~              ^#&:                          
      .5#J.            &@@@5     ?@@@@@@@P    7@@@@.   ?@@@&   .@@@@@@@@Y     .@@@@~           .J#P:                            
        .?#P:          #@@@G      .JGBBY:     5@@@&    ^@@@@.    ?B&&#P^      :@@@@~         ^PBJ.                              
           ~BB!        7@@@@5.              :P@@@@J     #@@@&!.             .!&@@@&        7BG~                                 
             :5#J.      ?@@@@@@@@@@@@@@@@@@@@@@@@J      .#@@@@@@&&&&&&&@&&@@@@@@@B.     :5BY.                                   
               .J#!      .7G&&@@@@@@@@@@@@@@&&G7.         ^5#&@@@@@@@@@@@@@@@&BJ:       7!                                      


 ''')

print("******** WELCOME TO Trivia Questions Game  -   By: Dr.m DEV *********")

#==========================================================================================================
question_bank = []
database_selection = ""
no_database_selected = True
#___________SELECT QUESTION DATA BASE:
while no_database_selected:
    database_selection = input("Select question database [1 or 2]")#for testing
    # 1 = question_data   &    2 = question_database2
    if database_selection == "1" or database_selection == "2":
        no_database_selected = False
    else:
        print("<!>ERROR! INVALID INPUT! please select [1 or 2]<!>")

if database_selection == "1":
    for questions in question_data:
        question_text = questions["text"]
        question_answer = questions["answer"]
        #____now creating objects
        new_question = Question(question_text, question_answer)
        #____NOW we store these objects inside the bank! "list"
        question_bank.append(new_question)
# print(question_bank[1].q_text) #--->that's how you get the question-text
# print(question_bank[1].q_answer) #--->that's how you get the answer-text

if database_selection == "2":
    for questions in question_database2: #SAME THING JUST RE-NAME THE LIST after importing it!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        question_text = questions["question"] #SAME THING just changed the KEY to fid the dictionary of the new database-list
        question_answer = questions["correct_answer"]  #SAME THING just changed the KEY to fid the dictionary of the new database-list
        #____now creating objects
        new_question = Question(question_text, question_answer)
        #____NOW we store these objects inside the bank! "list"
        question_bank.append(new_question)
# print(question_bank[1].q_text) #--->that's how you get the question-text
# print(question_bank[1].q_answer) #--->that's how you get the answer-text


#==========================================================================================================
#==========================================================================================================QuizBrain-test1\\
input("\npress anything to start\n")
#______________________________
quiz_system_obj = QuizBrain(question_bank)   #__________________________________>Made a quiz-system using QuizBrain CLASS

#______________________________
still_asking = True #by default
#-----------------------------
while still_asking:
    quiz_system_obj.next_question()
    quiz_system_obj.checking_questions()
    have_more_questions = quiz_system_obj.still_have_questions()
    #       |           |
    # the system    the list to process, why didn't we use the METHOD"next_question()" right away? because it's referred by self...so just add it
                                                                                                             # later as " .next_question() "
    #______________________to check if the answers are right..if YES move on...if NO..then STOP THE LOOP!
    still_asking = have_more_questions
    #______________________
