# ----------------------------
# PROJECT - MATH TUTOR
# ----------------------------

# in this project the idea is to create an application to practice multiplication tables
# user specify the number of random practice questions
# user is presented with a prompt ('5 x 5 = ' for example) and inputs the answer for each one of the questions
# when all questions are answered, the program will display:
# - a greeting like 'Thanks for playing'
# - number of correct answers
# - % of correct answers
# - time information presenting the time spent to answer the questions
# - all questions and answers at the end

from random import randint as r
from time import time as t

print('\n==========================')
print('MATH TUTOR')
print('==========================')

print('Welcome to Math Tutor!')
num_questions = int(input('\nInput the number of questions to be answered: '))
max_value = int(input('Input the max number to be used in each question: '))
print('Alright! Let\'s get started!')

user_answers = {}
correct_answers = {}
user_result = {}
questions = {}
num1 = 0
num2 = 0
start = t()

for i in range(num_questions):
    num1 = r(0, max_value)
    num2 = r(0, max_value)
    print(f'\nQuestion #{i+1}: {num1} x {num2} ')
    questions[i+1] = f'{str(num1)} x {str(num2)}'
    question_answer = int(input('Enter your answer: '))
    user_answers[i+1] = question_answer
    correct_answers[i+1] = num1*num2
    if correct_answers[i+1] == user_answers[i+1]:
        user_result[i+1] = 1
    else:
        user_result[i + 1] = 0
    i += 1
    end = t()

per_correct = int((sum(user_result.values())) / num_questions * 100)
print('==========================')
print('\nThank you for using Math Tutor!')
print('Here is your result:')
print(f'\nQuestions answered: {num_questions} in {round(end-start,1)} seconds')
print(f'Correct answers: {sum(user_result.values())}, which means {per_correct} % \n')

for r in range(num_questions):
    print(f'Question #{r+1}: {str(questions[r+1])} / Correct answer: {str(correct_answers[r+1])} -> '
          f'Your answer: {str(user_answers[r+1])}')
