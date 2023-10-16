#new math. hasn't it been long enough??? we're putting in classes...
        
import random

import sys
sys.path.append("../..")
                
from i import input_function, int_input_function
from quizquestion import Quiz_Question
from student import Student

#auto generating some problems
def auto_generate_problems():
    problem_list = []
    #theremust be a better way to put all of these into a list. 
    problem_list.append(Quiz_Question("5x + 3 = 13", "2", "1", ""))
    problem_list.append(Quiz_Question("14 - 3x = 2", "4", "1", ""))
    problem_list.append(Quiz_Question("9 - 2x = 3", "3", "1", ""))
    problem_list.append(Quiz_Question("8x + 2 = 50", "6", "1", ""))
    problem_list.append(Quiz_Question("2x + 16 = 40", "12", "1", ""))
    problem_list.append(Quiz_Question("12 - 2x = 2", "5", "1", ""))
    problem_list.append(Quiz_Question("7 = 49 - 6x", "7", "1", ""))
    problem_list.append(Quiz_Question("30 + 7x = 86", "8", "1", ""))
    problem_list.append(Quiz_Question("4x + 20 = 56", "9", "1", ""))
    problem_list.append(Quiz_Question("3x - 3 = 39", "14", "1", ""))
    return problem_list

def rand_seq_generate():
    rando_seq = []
    rando = random.randint(0,9)
    for x in range(0,9):
        while rando in rando_seq:
            rando = random.randint(0,9)
        rando_seq.append(rando)
    return rando_seq

#this seems not entirely necessary, but, you know, it works
def ready_input_function():
    ready = ""
    while ready != "Y" and ready != "N":
        try:
            ready = input()
            if not ready:
                raise ValueError('empty string')
            valid = True
        except ValueError:
            print("Invalid Input!")
    return ready  

def welcome():
    name = ""
    ready = ""
    print("what is your name? ")
    name = input_function()
    print(f"welcome, {name}, to the Tutorializer.\n")
    print("Are you ready to be Tutorialized? Y/N")
    ready = ready_input_function()
    if ready == "Y":
        print("Let's go!\n\n\n")
    elif ready == "N":
        print("Too bad! You cannot escape the Tutorializer!")

#sequence of random, nonrepeating integers 0 - 9 for random problem order
rando_seq = rand_seq_generate()

#auto generate problem list
problem_list = auto_generate_problems()

#intro text
welcome()


correct = 0


for x in range (0, 9):


    #i'm trying to:
    #1. choose item x in my list of randomized, nonrepeating integers
    this_rando = rando_seq[x]
    #2. choose the problem that corresponds to the value of this_rando in my ordered problem list
    this_question = problem_list[this_rando]
    #3. execute the get_user_ans behavior for the given problem object? it actually does seem to be working
    this_question.get_user_ans()

    #also trying to check_user_ans
    this_correct = this_question.check_answer()
    correct += this_correct


print(f"\n\nCongratulations! You have answered {correct} math problems correctly!")
print(f"Your Tutorialization Level is {correct*10}%.\n")



    
      

