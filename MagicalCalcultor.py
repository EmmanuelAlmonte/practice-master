import re 
import turtle

turtle.speed)(0)

print("Our Magical Calculator")
print("Type 'quit' to exit\n")
previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ''
    if previous == 0:
        equation = input('Enter equation: ')
    else:
        equation = input(str(previous))


    if equation == 'quit':
        run = False
    else:
        equation = re.sub('[A-Za-z,.:()" "]', ' ', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)



while run:
    performMath()