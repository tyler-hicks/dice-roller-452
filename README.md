## dice-roller-452
Dice Roller v0.5

This program will roll dice, multiple dice, any dice! 2 sides, 100 sides,
1000 sides. This project is in the development stage, so features may be missing
or not yet working.

## REQUIREMENTS
- Python
- Jupyter Notebook?
- Add more requirements?

## Usage
1. Run the program
2. Tell the program whether you want to roll some dice, look at the history of your rolls, or close the program.
3. If rolling, input your dice roll in the format: XdY +- XdY +-... Z, where X is the number of a type of dice, and Y is the number of sides
You can add as many dice as you want, with whatever sides you want. Example: 1d6 + 2d4 + 6d8 + 9
    (Format is important. Please add a space between the + or - and the variables.)
4. You can now roll multiple times by adding 'x#' to the end of your equation. For example: 1d20 + 1d6 + 7 x3. This will roll
those dice 3 times in a row and give you 3 separate results.
5. Press enter and you'll get your results. The program will display the results of each dice roll in the order that
they were input, as well as the total.
6. You'll be taken back to the main menu, and choose whether you want to roll, look at the history, or close the program.

## Upcoming Features
- Advantage / Disadvantage -- Only view the higher of two rolls or the lower of two rolls. (Possibly add a D or A to the
beginning of the XdY + XdY... + Z formula? I haven't figured it out yet)
- Fine-tuning the program, coming up with custom error messages for not inputting roll correctly.
