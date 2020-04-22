from random import randrange

def rand_num_gen(integer):
    result = randrange(1, integer+1)
    if integer == 20 and result == 20:
        print("critical success: ", end="")
    if integer == 20 and result == 1:
        print("critical failure: ", end="")
    return result

def roller(list):
    accumulator = []
    for i in list:
        stripped_strings = i.strip()
        if 'd' in stripped_strings:
            secondary_split = i.split('d')
            number = int(secondary_split[0])
            sides = int(secondary_split[1])
            if number < 0:
                number = -number
                for x in range(number):
                    result = rand_num_gen(sides)
                    accumulator = accumulator + [-result]
            else:
                for x in range(number):
                    result = rand_num_gen(sides)
                    accumulator = accumulator + [result]
        else:
            accumulator = accumulator + [int(i)]
    return accumulator

def output(list):
    string_accumulator = []
    total = 0
    for i in list:
        string = str(i)
        string_accumulator = string_accumulator + [string]
        total = total + i
    if len(string_accumulator) > 1:
        math = " + ".join(string_accumulator)
        display_list = [math] + ["="] + [str(total)]
        display = " ".join(display_list)
    else:
        display = str(total)
    return display

print("""          _________ 
         | o     o |  
         |    o    |  
         | o     o |  
         '---------'  
       DICE ROLLER V0.5""")

history = []
while True:
    inp = str(input('roll, history, or close?: '))
    inp = inp.lower()
    if inp == 'roll':
        print("Autobots, roll out")
        dice_input = str(input("Enter your dice roll: "))
        neg_counter = 0
        multiplier = None
        if 'x' in dice_input:
            multiplier_split = dice_input.split()
            dirtymultiplier = multiplier_split.pop(-1)
            multiplier = int(dirtymultiplier.strip('x'))
            dice_input = " ".join(multiplier_split)
        if '-' in dice_input:
            negative_split = dice_input.split()
            for i in negative_split:
                if i == '-':
                    negative_split[neg_counter] = '+'
                    negative_split[neg_counter + 1] = '-' + negative_split[neg_counter + 1]
                neg_counter = neg_counter + 1
            dice_input = " ".join(negative_split)
        initial_split = dice_input.split('+')
        if multiplier is not None:
            for x in range(multiplier):
                accumulator = roller(initial_split)
                display = output(accumulator)
                print(display)
                history = history + [(dice_input, display)]
                accumulator = []
        else:
            accumulator = roller(initial_split)
            display = output(accumulator)
            print(display)
            history = history + [(dice_input, display)]
    elif inp == "history":
        print('historical!')
        if len(history) == 0:
            print('no history yet')
        else:
            counter = 1
            for i in history:
                print('roll #', counter, ' was ', i[0], ' and the result was ', i[1], sep='')
                counter = counter + 1
    elif inp == "close":
        print("closing time!")
        break
    else:
        print("Invalid Command. Please enter roll, history, or close.")
