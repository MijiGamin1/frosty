# Frosty v1.21
# What is Frosty?  
Frosty is an esolang created by MijiGamin1 just for fun. The entire point of the language is that every variable is stored as a list of integers, and the language revolves around changing and manipulating these integers.  

Frosty was named after SNOBOL (more specifically, SNOBOL 4), a language from 1967 which is widely regarded to be the first language to implement hash maps, the system of data storage that Frosty relies upon, as well as Frosty The Snowman, to stick with the winter theme and because he's my favorite Christmas-related character.

# How do I run a Frosty program?
## Requirements:
* The latest version of [Python](https://www.python.org/) installed
* Some kind of text editor

## Running the program:
1. Place the interpreter.py file and the .fy file (your program) in the same folder/directory.
2. In your terminal, navigate to the directory of your files with `cd`.
3. Type `python interpreter.py` in the teminal.  
         * (Note: you may change the name of interpreter.py if you don't want to type all that. The name has no effect on the program's ability to function.)
5. Give the name of your Frosty file when inputted.
6. Sit back and watch your Frosty program run!

Please report any issues in the Issues tab!

# Syntax and Documentation
## Adding to lists
Frosty is built off of lists of integers signified and referenced by a key, which is also an integer.  

To add a number to a list, do the command `+` followed by the key of the list you're adding to, as well as the number you're adding to it.
Examples:
```
+0/5/ # Adds 5 to list 0
+10/50/ # Adds 50 to list 10
+100/500/ # Adds 500 to list 100
```
(Note: there are no comments in Frosty. The `#` is merely for documentational purposes only.)

## Editing the contents of lists
Adding to lists is cool and all, but what if I want to edit a number I've already added? That's where the `~` command comes in. 

To edit a number in a list, use the `~` command, followed by the key of the list you want to edit, the index of the list you want to edit (indexes start at 0), and what you want to edit that index to.
Examples:
```
~0/0/10/ # Changes index 0 of list 0 to 10
~1/10/100/ # Changes index 10 of list 1 to 100
~10/100/1000/ # Changes index 100 of list 10 to 1000
```

## Removing from lists
If you'd like to completely remove a number from a list, use the `$` command, followed by the same syntax in the `~` command, but minus the number at the end. 

The removed number will be "popped" from the list, with the next number taking its place, the next number after that doing the same, and so on and so forth.
Examples:
```
$0/0/ # Removes index 0 from list 0
$1/5/ # Removes index 5 from list 1
$5/25/ # Removes index 25 from list 5
```

## Referencing lists in your code
These lists aren't just for storing data, they can be referenced as values later in your code.

To do this, replace any* parameter with the following formatting: `*[key]-[index]*`
Examples:
```
+1/*0-0*/ # Adds the value of list 0 index 0 to list 1
~2/2/*1-1*/ # Changes the value of list 2 index 2 to the value of list 1 index 1
-3/*2-2*/ # Removes the index equivalent to the value of list 2 index 2 from list 3 (I don't know 𝘸𝘩𝘺 you'd do this, but you can.)
```

To use the length of a list as a value, replace the key with `_`, and the index with the key.
Examples:
```
+1/*_-0*/ # Adds the length of list 0 to list 1
+7/*_-5*/ # Adds the length of list 5 to list 7
```
*There are a few exceptions, namely the first parameter of `+`, the first parameter of `:`, and the parameter of `#`, and any other code I'm not touching again with a 39.5 foot pole.

## Printing
At the moment we've just been focusing on things happening within the code, but what if you want to show something to the user? That's where printing comes in.

There are four printing commands: print number (`.`), print ASCII (`,`), print whole list in number form (`\`), and print whole list in ASCII form (`!`).

### Single character printing
To print out a single character, use the `.` or `,` commands as detailed above, followed by the number you'd like to print.
Examples:
```
.10/ # Prints "10" to the console
,104/ # Prints "h" to the console
.*0-0*/ # Prints the value of list 0 index 0 to the console
```

### List printing
To print out a full list, use the `\` or `!` commands as detailed above, followed by the list of which you'd like to print the values of out.

Lists printed as numbers (`\`) will print out in the standard Python list format (Ex: `[8, 16, 30, 32, 46, 84]`), while lists printed as ASCII characters will print out as a string, with each letter in the string corresponding to the ASCII value of a number in the list.
Examples:
```
\0/ # Prints out the entirety of list 0 in number form
!1/ # Prints out the entirety of list 1 in ASCII form
```

## User input
You can ask integer input from the user using the `@` command, which changes the value of a specified index of a specified list. 

To use it, use the `@` command, followed by the list you're changing, followed by the index you're changing.
Examples:
```
@0/0/ # Changes the value of list 0 index 0 to a value the user inputted
@1/5/ # Changes the value of list 1 index 5 to a value the user inputted
```

## Arithmetic
Frosty has five arithmetic operators: addition (`a`), subtraction (`s`), multiplication (`x`), division (`d`), and modulo (`m`).

These operators change a specified index from a specified list to the result of these mathematical equations.
Examples:
```
a0/0/5/5/ # Adds 5+5 and sets list 0 index 0 to the result
x1/1/4/*2-2*/ # Multiplies 4 and the value of list 2 index 2 and sets list 1 index 1 to the result
d3/3/15/4/ # Divides 15/4 and sets list 3 index 3 to the value (Note: division rounds the result, as I don't want to deal with decimals.)
```

## Loops
### Starting a loop
In Frosty, loops are defined with two characteristics: the ID, and the amount of times to loop.

The ID is important for identifying the loop, as well as creating the blockade to end it. Obviously, declaring how many times it must loop is also important.

To start a for loop, use the `:` command, followed by the ID, as well as how many times you want the loop to repeat minus one (the looping runs on an index system). 
Examples:
```
:0/5/ # Loop with ID 0 that will loop 6 times
:1/9/ # Loop with ID 0 that will loop 10 times
:2/*0-0*/ # Loop with ID 0 that will loop the value of list 0 index 0 times
```

### Referencing a loop's iterator
In Frosty, you can reference the "iterator" in parameters, which is the current loop being taken (out of the total loops allocated).  
For example, if the loop is declared as `:0/4/`, the iterator will change from 4 to 3, 2, 1, then 0.

To reference this iterator, use the standard reference formatting, but with slight tweaks: `i-[id of loop]`.
Examples:
```
+1/*i-0*/ # Adds the iterator of loop 0 to list 1
~3/0/*i-1*/ # Changes the value of list 3 index 0 to the iterator of loop 1
.*i-3*/ # Prints out the iterator
```

### Ending a loop
To signify the end boundary of a loop, use the `#` command, followed by the ID of the loop you want to end.
Examples:
```
#0/ # End boundary of loop 0
#2/ # End boundary of loop 2
```

## Conditionals
There are three types of conditional operators in Frosty: less than (`<`), greater than (`>`), and equals to (`=`).

To use these them, use the operator, followed by the two numbers you'd like to compare, then the ID of the end of the conditional statement. 
Examples:
```
>4/3/0/ # Continues as normal, as 4 > 3
<5/3/1/ # Goes to ending of ID 1, as 5 !< 3
=7/*0-0*/7/ # Continues as normal if list 0 index 0 is 7, else goes to ending of ID 7
```

If the comparison turns out to be false, the program will continue from the first instance of the ending identifier.
To signify the ending identifier, use the `}` command, followed by the ID of the if statement.
Examples:
```
}0/ # If conditional with an ID of 0 is false, the code continues here
}2/ # If conditional with an ID of 2 is false, the code continues here
```



