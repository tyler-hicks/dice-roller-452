from random import randrange

# format should be AdB + CdD +... + modifier, where the variables and modifier are integers.
# Point users to readme file for full format rules.
# Going off Dungeons and Dragons 5th Edition rules as standard format.
# This standard means 20 sided die (d20) behave differently in that modifiers apply to each roll, not just to the total.
# Will document other exceptions as they come up.

dice_input = str(input("Enter your dice roll: "))
initial_split = dice_input.split('+')
# print(initial_split)
accumulator = []

for i in initial_split:
    stripped_strings = i.strip()
    # print(stripped_strings)
    if 'd' in stripped_strings:
        secondary_split = i.split('d')
        # print(secondary_split)
        number = int(secondary_split[0])
        sides = int(secondary_split[1])
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
# if users are only rolling one die, total and the result should be the same
if len(string_accumulator) == 1:
    print(total)
else:
    print(math, "=", total)

# pretty good. Need to account for d20 rolls and advantage / disadvantage, as well as exceptions such as users not following correct format.
# Could add additional features such as getting a 1 or 20 on a d20 roll.
# need to also start github article and narrative

# d20 idea: add some sort of variable to the result of a 20 sided die roll to distinguish it from other die
# can filter out or pop out those rolls, get rid of the variable and print separately

# to make a history function, could make this a function where users get prompts to make another roll
# could make another accumulator of past rolls
# could add an option to clear history as well

# choice = eval(input("Roll, history, or close?:")
# if choice == "roll" or "Roll":
#   go into roll dice function
# elif choice == "history" or "History":
#   bring up for loop that prints out history of results. history would be list. maybe make dictionary for searching?
# elif choice == "Close" or "close":
#   clear history and print some goodbye
# else:
#   print "unknown command" and repeat the prompt.
# research says 'while' loops may be needed to keep repeating the prompt
