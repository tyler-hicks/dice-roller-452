from random import randrange

def rand_num_gen(integer):
    # generates a random number between 1 and the number of sides a die has
    # Updated on April 22 to include print statements for max or min results on 20-sided die
    result = randrange(1, integer+1)
    if integer == 20 and result == 20:
        print("Critical success: ", end="")   # needed end statement so that user didn't get confused and think critical success or failure applied to different roll
    if integer == 20 and result == 1:
        print("Critical failure: ", end="")
    return result

def roller(list):
    # strips the list of inputs further, differentiating between die rolls and pure bonuses or penalties
    try:
        accumulator = []
        for i in list:
            stripped_strings = i.strip()
            if 'd' in stripped_strings:
                secondary_split = i.split('d')   # Because "XdY" is typical for roleplaying games dice format, needed to split between number of die and sides of the die
                number = int(secondary_split[0])
                sides = int(secondary_split[1])
                if number < 0:  # relates to negative numbers, if you need to subtract a die roll from another roll
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
    except ValueError:
        # ValueError was the main type of error that came up in testing, and was 99% of the time related to format
        # This will make sure the user understands that there was an error while allowing the program to continue to run
        print("Incorrect format! Be sure to add a plus or minus sign in between each input, and adhere to the format for dice rolls and multipliers.")
        print("Refer to the ReadMe if you are continuing to have trouble for more information", end="")
        accumulator = []
        return accumulator
    else:
        return accumulator

def output(list):
    # returns the displayed results, both the math portion as well as the total
    string_accumulator = []
    total = 0
    for i in list:
        string = str(i)
        string_accumulator = string_accumulator + [string]
        total = total + i
    if len(string_accumulator) > 1:  # Didn't want to display XX = XX, so built in this filter
        math = " + ".join(string_accumulator)
        display_list = [math] + ["="] + [str(total)]   # needed to make the display a variable and also print how I wanted it to. Needed to use .join to do that.
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
       DICE ROLLER V1.0""")

history = []
while True: # will keep the input coming up forever, until user inputs close
    inp = str(input('Roll, history, or close?: '))
    inp = inp.lower()
    if inp == 'roll':
        # Main part of code
        dice_input = str(input("Enter your dice roll: ")).lower()
        multiplier = 1 # Makes the standard multiplier 1, so that if users don't enter one, the for-loop below still works
        if 'x' in dice_input:
            multiplier_split = dice_input.split()
            dirtymultiplier = multiplier_split.pop(-1) # because the multiplier should be the last element in the user input, this takes it out and makes it the new value for multiplier
            multiplier = int(dirtymultiplier.strip('x'))
            dice_input = " ".join(multiplier_split)
        if '-' in dice_input:  # Accounts for minuses being in statements, originally a big oversight
            negative_split = dice_input.split()
            neg_counter = 0
            for i in negative_split: # iterates through the user input, turning -'s into +'s and applying a - to the following element
                if i == '-':
                    negative_split[neg_counter] = '+'
                    negative_split[neg_counter + 1] = '-' + negative_split[neg_counter + 1]
                neg_counter = neg_counter + 1
            dice_input = " ".join(negative_split)
        initial_split = dice_input.split('+')   # splits it up on +'s so it's just dice and numbers.
        for x in range(multiplier):
            accumulator = roller(initial_split)
            display = output(accumulator)
            if display != '0': # Because 0 should only be for rolls that have ValueErrors, this filter accounts for that
                print(display)
            else:
                display = 'ERROR'
                print("")
            history = history + [(dice_input, display)]
            accumulator = []  # need to reset accumulator in each for loop to keep from displaying all past results
    elif inp == "history":  # prints out past rolls. Uses a list of tuples to accumulate all rolls
        if len(history) == 0:
            print('no history yet')
        else:
            counter = 1
            for i in history:
                print('roll #', counter, ' was ', i[0], ' and the result was ', i[1], sep='')
                counter = counter + 1
    elif inp == "close":
        print("""
          _________ 
         | o       |  
         |         |  
         |       o |  
         '---------'  
       THANKS FOR USING
         DICE ROLLER!""")
        break     # break is the only thing that will close out the while True loop.
    else:  # accounts for all other commands that would display an error otherwise
        print("Invalid Command. Please enter roll, history, or close.")
