from random import randrange

# format should be AdB + CdD +... + modifier, where the variables and modifier are integers.
# Point users to readme file for full format rules.
# Going off Dungeons and Dragons 5th Edition rules as standard format.
# This standard means 20 sided die (d20) behave differently in that modifiers apply to each roll, not just to the total.
# Will document other exceptions as they come up.


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

        print(accumulator)

        string_accumulator = []
        total = 0

        for i in accumulator:
            string = str(i)
            string_accumulator = string_accumulator + [string]
            total = total + i
        math = " + ".join(string_accumulator)
        print(math, '=', total)
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

    print(accumulator)

    string_accumulator = []
    total = 0

    for i in accumulator:
        string = str(i)
        string_accumulator = string_accumulator + [string]
        total = total + i
    math = " + ".join(string_accumulator)

    print(math, '=', total)
