from random import randrange

history = []

while True:
    inp = input('roll, history, or close?: ')
    if inp == 'roll':
        dice_input = str(input("Enter your dice roll: "))
        neg_counter = 0
        multiplier = None

# below function stays outside loop
        if 'x' in dice_input:
            multiplier_split = dice_input.split()
            dirtymultiplier = multiplier_split.pop(-1)
            multiplier = int(dirtymultiplier.strip('x'))
            dice_input = " ".join(multiplier_split)
# below function stays outside loop
        if '-' in dice_input:
            negative_split = dice_input.split()
            for i in negative_split:
                if i == '-':
                    negative_split[neg_counter] = '+'
                    negative_split[neg_counter + 1] = '-' + negative_split[neg_counter + 1]
                neg_counter = neg_counter + 1
            dice_input = " ".join(negative_split)
# below can stay outside loop?
        initial_split = dice_input.split('+')
# this should be inside loop?
        accumulator = []
# everything below should definitely be inside loop

        if multiplier is not None:
            for x in range(multiplier):
                for i in initial_split:
                    stripped_strings = i.strip()
                    if 'd' in stripped_strings:
                        secondary_split = i.split('d')
                        number = int(secondary_split[0])
                        sides = int(secondary_split[1])
                        if number < 0:
                            number = -number
                            for x in range(number):
                                result = randrange(1, sides)
                                accumulator = accumulator + [-result]
                        else:
                            for x in range(number):
                                result = randrange(1, sides)
                                accumulator = accumulator + [result]
                    else:
                        accumulator = accumulator + [int(i)]
                string_accumulator = []
                total = 0
                for i in accumulator:
                    string = str(i)
                    string_accumulator = string_accumulator + [string]
                    total = total + i
                math = " + ".join(string_accumulator)
                print(math, '=', total)
                history = history + [(dice_input, total)]
                accumulator = []
                string_accumulator = []
        else:
            for i in initial_split:
                stripped_strings = i.strip()
                if 'd' in stripped_strings:
                    secondary_split = i.split('d')
                    number = int(secondary_split[0])
                    sides = int(secondary_split[1])
                    if number < 0:
                        number = -number
                        for x in range(number):
                            result = randrange(1, sides)
                            accumulator = accumulator + [-result]
                    else:
                        for x in range(number):
                            result = randrange(1, sides)
                            accumulator = accumulator + [result]
                else:
                    accumulator = accumulator + [int(i)]
            string_accumulator = []
            total = 0
            for i in accumulator:
                string = str(i)
                string_accumulator = string_accumulator + [string]
                total = total + i
            math = " + ".join(string_accumulator)
            print(math, '=', total)
            history = history + [(dice_input, total)]
    elif inp == 'history':
        print('historical!')
        if len(history) == 0:
            print('no history yet')
        else:
            counter = 1
            for i in history:
                print('roll #', counter, 'was', i[0], 'and the result was', i[1])
                counter = counter + 1
    elif inp == 'close':
        print('closing time!')
        break
    else:
        print('invalid command.')
