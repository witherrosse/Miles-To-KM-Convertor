How this code works (Miles to KM Converter)
This is a simple graphical program using Tkinter. You type a number in miles, click a button, and it shows you the distance in kilometers.


____________________________________________________________________________________________________________________

What is used in this code
tkinter module: to create the window, labels, entry box, and button

float() function: to convert text input to a number

round() function: to make the result a whole number

.config() method: to update the result label with new text

.grid() layout: to place widgets in rows and columns

command option: to connect the button to a function

____________________________________________________________________________________________________________________

How the converter works
Program starts
A window opens with the title "Miles to KM Converter".
You see an empty box, some labels, and a button.

User types miles
You type a number (like 10) into the entry box.

User clicks the button
The button says "Calculate".
When you click it, the program runs the miles_to_km() function.

Inside the function

It takes the number from the entry box

Converts it to a float (decimal number)

Multiplies it by 1.609 (because 1 mile = 1.609 kilometers)

Rounds the result to a whole number

Result is shown
The converted number appears next to the label that says "KM".
The label originally showed "0", but it changes to the new number.

What the user sees on screen
Row 0: [ entry box ] Miles
Row 1: equal to [ result ] KM
Row 2: [ Calculate ]

Example
User types 5 in the box

User clicks "Calculate"

Program does: 5 × 1.609 = 8.045 → rounds to 8

Screen shows: 8 next to "KM"
