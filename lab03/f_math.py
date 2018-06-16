from random import choice,randint
# from eval import calc
import eval


x = randint(1,10)
y = randint(1,10)
list_op = ["+","-","*","/"]
op = choice(list_op)
# res = -9999
# if op == "+":
#     res = x + y
# elif op == "-":
#     res = x-y
# elif op == "*":
#     res = x * y
# elif op == "/":
#     res = x / y

res = eval.calc(x,y,op)
err = choice([-1,0,1])   
display_res = res + err
print("{0} {1} {2} = {3}".format(x,op,y,display_res))

user_choice = input("Y/N: ").upper()
if err == 0 and user_choice == "Y":
    print("Yay")
elif err != 0 and user_choice == "N":
    print("Yay")
else:
    print("Wrong")


    
