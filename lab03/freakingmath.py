from random import *
from eval import calc
def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(1,10)
    y = randint(1,10)
    list_op = ["+","-","*","/"]
    op = choice(list_op)
    result = 0
    if op == "+":
        result = x + y
    elif op == "-":
        result = x - y
    elif op == "*":
        result = x * y
    elif op == "/":
        result = x / y
    err = choice([-1,0,1])
    res = err + result
    return [x, y, op, res]

def check_answer(x, y, op, result, user_choice):
    resu = calc(x,y,op) 
    if  result == resu:
        # if user_choice == True:
        #     return True
        # else:
        #     return False
        return user_choice
    else:
        # if user_choice == True:
        #     return False
        # else:
        #     return True
        return not user_choice
