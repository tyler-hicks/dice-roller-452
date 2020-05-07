# dice-roller-452
Dice Roller v1.0

This program is designed to act in lieu of rolling traditional dice. Whether for Yahtzee or Dungeons and Dragons, this program
can roll dice of any sides and add bonuses or penalties as necessary. Need to roll a bunch of dice in a row? We've got you covered.
This program is still being tweaked and while many errors are related to not following the correct format below, we're not perfect.
Feel free to let us know about any issues you have running the program and we'll try to address your concerns as quickly as
possible.

# Requirements
- Python v3.6 or higher

# How to use this program
1. Run the program in Python
2. A menu will come up asking you if you want to roll dice, look at the history of your rolls, or close the program
3. If you enter 'roll', input your roll using the format below. Press enter when you are done. The program will generate
your roll and show you the resulting total.
4. If you enter 'history', press enter and you'll be taken to a list of your past rolls and their results.
5. Once your results have been brought up, you'll be returned to the main menu and you can select roll, history, or close.
6. Once you're finished with the program, enter 'close', and the program will end. Be warned, your roll history will not
be saved.

# Format
Format is similar to how many role-playing games format their dice rolls, and is very important to making sure the program
works as intended. When the program asks for your dice input, you'll enter an integer for the number of dice you want to roll,
followed by the letter 'd' for dice or die, followed by another integer for the number of sides the die has.
## EXAMPLES:
- One six-sided die being rolled would look like this: 1d6
- Two twenty-sided dice being rolled would look like this: 2d20
## MULTIPLE DICE
If you want to add more dice, add a space, a plus or a minus sign, depending on whether you want to add or subtract those rolls
from the overall total, and another space, and then simply follow the steps above again.
## EXAMPLES:
- One six-sided die plus one four-sided die would like this: 1d6 + 1d4
- Two twelve-sided die minus three eight-sided die would look like this: 2d12 - 3d8
## BONUSES/PENALTIES
In role-playing games, there are often modifiers that you can add or subtract from your dice rolls. To do that in this dice
roller, simply add a space, a plus or a minus sign, and another space, followed by an integer.
## EXAMPLES:
- Three ten-sided die plus seven: 3d10 + 7
- One twenty-sided die plus one eight-sided die plus one four-sided die minus two: 1d20 + 1d8 + 1d4 - 2
## MULTIPLIERS
In role-playing games, you might want to roll multiple times in a row with the same modifiers or die, such as when attacking in
5th Edition Dungeons and Dragons. To do that in this dice roller, simply add the letter 'x' followed by an integer to the end of
your input.
## EXAMPLES:
- One twenty-sided die plus five, twice: 1d20 + 5 x2
- One twenty-sided die minus one four-sided die plus one eight-sided die plus twelve, four times: 1d20 - 1d4 + 1d8 + 12 x4

# History
One of the functions of this dice roller is to be able to look at your past rolls and results. The results and die rolls will
appear in the order that you input them. Any errors will simply show up as "ERROR". Note that when closing the program, this
dice roller will not save your results. Each new session of this dice roller is started from scratch.

# Upcoming Features
- Advantage / Disadvantage
- Searching for specific rolls in history
- Better ASCII art
- Further fine-tuning



