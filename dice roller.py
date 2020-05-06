from random import randrange

# below generates a random number between 1 and the number of sides a die has
# Updated on April 22 to include print statements for max or min results on 20-sided die
def rand_num_gen(integer):
    result = randrange(1, integer+1)
    if integer == 20 and result == 20:
        # needed end statement so that user didn't get confused and think critical success or failure applied to different roll
        print("critical success: ", end="")
    if integer == 20 and result == 1:
        print("critical failure: ", end="")
    return result

# Below strips the list of inputs further, differentiating between die rolls and pure bonuses or penalties
# Is used multiple times due to multiplier function added on April
def roller(list):
    try:
        accumulator = []
        for i in list:
            stripped_strings = i.strip()
            # Because "XdY" is typical for roleplaying games dice format, needed to split between number of die and sides of the die
            if 'd' in stripped_strings:
                secondary_split = i.split('d')
                number = int(secondary_split[0])
                sides = int(secondary_split[1])
                # relates to negative numbers, if you need to subtract a die roll from another roll
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
    # ValueError was the main type of error that came up in testing, and was 99% of the time related to format
    # This will make sure the user understands that there was an error while allowing the program to continue to run
    except ValueError:
        print("Incorrect format! Be sure to add a plus or minus sign in between each input, and adhere to the format for dice rolls and multipliers.")
        print("Refer to the ReadMe if you are continuing to have trouble for more information", end="")
        accumulator = []
        return accumulator
    else:
        return accumulator

# Below returns the displayed results, both the math portion as well as the total
def output(list):
    string_accumulator = []
    total = 0
    for i in list:
        string = str(i)
        string_accumulator = string_accumulator + [string]
        total = total + i
    # Didn't want to display XX = XX, so built in this filter
    if len(string_accumulator) > 1:
        math = " + ".join(string_accumulator)
        # needed to make the display a variable and also print how I wanted it to. Needed to use .join to do that.
        display_list = [math] + ["="] + [str(total)]
        display = " ".join(display_list)
    else:
        display = str(total)
    return display

print("""
          _________ 
         | o     o |  
         |    o    |  
         | o     o |  
         '---------'  
       DICE ROLLER V0.9""")

history = []
# will keep the input coming up forever, until user inputs close
while True:
    inp = str(input('roll, history, or close?: '))
    inp = inp.lower()
    if inp == 'roll':
        # Main part of code
        print("Autobots, roll out")
        dice_input = str(input("Enter your dice roll: ")).lower()
        neg_counter = 0
        # Sets up multiplier ability in code. Can roll dice multiple times in a row by inputting "x#' at the end of the input
        # Useful for times when bonuses or penalties apply across multiple rolls
        multiplier = None
        if 'x' in dice_input:
            multiplier_split = dice_input.split()
            dirtymultiplier = multiplier_split.pop(-1)
            multiplier = int(dirtymultiplier.strip('x'))
            dice_input = " ".join(multiplier_split)
        # Accounts for minuses being in statements, originally a big oversight
        if '-' in dice_input:
            negative_split = dice_input.split()
            for i in negative_split:
                if i == '-':
                    negative_split[neg_counter] = '+'
                    negative_split[neg_counter + 1] = '-' + negative_split[neg_counter + 1]
                neg_counter = neg_counter + 1
            dice_input = " ".join(negative_split)
        # splits it up on +'s so it's just dice and numbers.
        initial_split = dice_input.split('+')
        if multiplier is not None:
            for x in range(multiplier):
                accumulator = roller(initial_split)
                display = output(accumulator)
                print(display)
                history = history + [(dice_input, display)]
                # need to reset accumulator in each for loop to keep from displaying all past results
                accumulator = []
        else:
            accumulator = roller(initial_split)
            display = output(accumulator)
            if display != '0':
                print(display)
            else:
                print("")
            history = history + [(dice_input, display)]
    # prints out past rolls. Uses a list of tuples to accumulate all rolls
    elif inp == "history":
        print('historical!')
        if len(history) == 0:
            print('no history yet')
        else:
            counter = 1
            for i in history:
                print('roll #', counter, ' was ', i[0], ' and the result was ', i[1], sep='')
                counter = counter + 1
    # break is the only thing that will close out the while True loop.
    elif inp == "close":
        print("closing time!")
        break
    # accounts for all other commands that would display an error otherwise
    else:
        print("Invalid Command. Please enter roll, history, or close.")
