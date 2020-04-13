from random import randrange

neg_counter = 0
neg_accumulator = []

dice_input = str(input("Enter your dice roll: "))
if '-' in dice_input:
    negative_split = dice_input.split()
    for i in negative_split:
        if i == '-':
            negative_split[neg_counter] = '+'
            negative_split[neg_counter + 1] = '-' + negative_split[neg_counter + 1]
        neg_counter = neg_counter + 1
    dice_input = " ".join(negative_split)
initial_split = dice_input.split('+')

accumulator = []

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
