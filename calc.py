#creating a calculator that will save the previous answer
# and able to perform further calculation with the answer

import re

print("My First Python Calculator")
print("Type 'q' to quit")

previous = 0 #hold result of previous result
run = True

def performMath():
    global run
    global previous
    equation = ""

    # to display either first time calc or previous answer to the equation
    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))

    if equation == "q":
        # quit the program
        print("Goodbye!")
        run = False
    else:
        # using regax to remove alphabets and punctuations
        equation = re.sub('[a-zA-Z,;.()" "]', '', equation)

        # check if its calc start
        if previous == 0:
            # using eval function to do math calculation
            previous = eval(equation)
        else:
            # otherwise perform calc with the previous entered number
            previous = eval(str(previous) + equation)

while run:
    performMath()
