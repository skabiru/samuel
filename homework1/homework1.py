#File:homework1. py
# --- Variables and Data Types ---
a = 10
print(a)
print(type(a)) # an integer, a whole number with no decmials
b = 1.5
print(b)
print(type(b)) # a float, fractional number or number with a decimal point
c = 3j
print(c)
print(type(c)) # a complex number, used to write imaginary numbers
d = "hello"
print(d)
print(type(d)) # string, words or text
e = [1, 2, 3]
print(e)
print(type(e)) # list, a collection of items(changeable)
f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # dictionary, collection of key and value pairs
g = (1, 2)
print(g)
print(type(g)) # tuple, list of items (contents are unchangeable)
h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # list with strings as the items
i = True
print(i)
print(type(i)) # boolean (True or False)
j = None
print(j)
print(type(j)) # nonetype, having no value or null value
k = [True, "blue", 12]
print(k)
print(type(k)) # list, with different data types
l = str(14)
print(l)
print(type(l)) # str, the str function turns 14 into a string
m = 1e4
print(m)
print(type(m)) # float, scientific notation results in a float
#Questions:
# 1. There were 9 different data types
# 2. int, float, complex, string, list, dictionary, tuple, bool, nonetype
# 3. b,m = float  ,  str = d,l  ,  list = e, h, k
# 4. a string. because str() changes 14 an interger to a string. str() is a function that changes the input into a string.
# 5. n = {4, 6, 7} , print(type(n)) , a set - unique unordered items

# --- Booleans ---
print(10 > 9) # True, 10 is greater than 9 
print(10 == 9) # False, 10 is not equal to 9
print(10 <= 9) # False a 10 is not less than or equal to 9 
bool("abc") # True, bool treats a str as being true if there are characters inside
bool(123) # True, any non zero number is treated as being true
bool(["apple", "banana", "cherry"]) # True, the list is not empty 
bool(True) # True, true is always true
bool(False) # False, bool of false is false
bool(0) # False, 0 is treated as being 
bool("") # False, the string is empty
bool(" ") # True, even though it looks empty, python reads the space created as being a character
bool(()) # False, the tuple is empty
bool([]) # False as the list is empty
bool({}) # False as the dict is empty
bool(True and False) # False, and requires both sides to be true in order for the whole thing to be true
bool(True and True) # True, both statements are true
bool(False and False) # False, as none of the statements are true
bool(True or False) # True, or only requires one side to be true in order for the whole thing to be true
bool(True or True) # True, atleast one side is true
bool(False or False) # False, none of the sides are true
bool(not(False)) # True, the not false on the inside becomes true
bool(not(True)) # False as the not true becomes false
# Questions:
# 1. Things that represent "nothing" such as empty strings(spaces count like a character", none, 0, any other thing being empty returns False while everything else True
# 2. Bool(" ") being True was suprising as it looks like there is nothing.
# 3. bool([60]) true because the list is not empty
# 4. bool(None) returns false as python sees None as being False

# --- Operators ---
# Arithmetic Operators
print(10 + 5) # 15, + performs addition
print(10 - 5) # 5, - performs subtraction
print(2 * 4) # 8, * performs multiplication 
print(6 / 3) # 2.0 , / performs division (returns a float)
print(5 % 2) # 1, divides the first by the second but only returns the remainder
print(3 ** 2) # 9, ** returns the first number raised to the second
print(15 // 2) # 7, divides the first by the second but only returns the quotient

# Comparison Operators
print(5 == 2) # False, 5 does not equal 2
print(10 != 10) # False, the symbol means does not equal but in this case the two numbers are equal
print(2 < 5) # True, 2 is less than 5.
print(12 > 5) # True, 12 is greater than 
print(5 <= 6) # True, 5 is always less than or equal to 6
print(1 >= 10) # False, 1 is never greater than or equal to 10

#--- Assignment Operators ---
x = 5 
x += 5
print(x) # 10, adds x to 5 and reassigns the value of x to 10
x -= 4
print(x) # 6 as it takes 4 away from x which is 10 from the step above
x *= 3
print(x) # 18 as it multiplies 3 by x which is 6 from the step above

# --- Logical Operators ---
# 1. And checks both sides and returns true only if both sides are true . True = (6 < 8) and (1 == 1),False = (6 < 8) and (1 == 5)
# 2. or checks both sides and returns true if one of the sides are true. True = (6 < 8) or (1 ==9), False = (6 > 8) or (1 == 45)
# 3. not refuses a booleans value. true: not(False), false: not(True)

# --- More Questions: ---
# 1. / does standard division of the first number by the second and returns the result as a float while // only returns the qoutient of the division ignoring remainder if there are any
# 2. % divides the fist by the second and returns the remainder of the division while // only returns the qouetient gotten from the division.
# 3. I would use % to return the remainder. 5 % 2 would return 1.
# 4. It performs the arithmetic operator between the variable given and number and reassigns the answer to the variable. Doing both arithmetic and reassigning.

# --- Strings ---
my_string = "hello"
print(my_string) # prints hello
print(my_string[0]) # prints h 
print(my_string[1]) # prints e
print(my_string[2]) # prints l
print(my_string[3]) # prints l
print(my_string[4]) # prints o
print(my_string[-1]) # prints o (goes back the other way starting from -1)
print(my_string[1:3]) # prints el, the characters starting from my_string[1] until my_string[3] but does not include it.
print(my_string[0:5:2]) # prints hlo , some logic as above but this time it takes a step of 2 meaning it would go from 0 to 2 to 4
print(len(my_string)) # prints 5 the number of characters in the word
print(my_string + "goodbye") # prints hellogoodbye,connects the two words together
print(7 * my_string) # prints hello 7 times all connected to each other

# ---Questions---
# 1. A technique to extract a portion of a sequence. the basic syntax in python uses brackets that have information inside such as the start, stop and the step it should take when slicing. we use this above in the strings section.
name = "Oski"
print("Hello, my name is", name)
# 2. It returns Hello, my name is Oski
name = "Oski"
print(f"Hello, my name is {name}")
# 3. Even though written differently is returns the same thing as above.
# 4. The second one uses f-strings which is an easy way to input variables into our strings. They are easier to read and are more common than the first method.

# --- Terminal Commands ---

# cd
# Changes directories. Use it to move from one folder to another
# Example: cd homework1

# ls 
# list files and folders in current working directory. use it to look up the files and folder of the directory you are currently  in
# Example: ls 

# ls -a
# lists all files and folders in the current working directory even those that are hidden. use when you want to see all files including the hidden ones.
# Example: ls -a

# mkdir
# makes a new directory in the current working directory. use it when you want to make a new directory.
# mkdir homework2

# cat
# prints out all the contents of a file. use when you want to see what is inside a file.
# cat datatypes.py

# pwd
# prints (shows) the current working directory. use when you want to see what directory you are currently in.
# pwd

# cd.. 
# moves you up to the parent directory. use when u want to go back to the main directory.
# cd..

# cd.
# refers to the current directory. not really used as it does not change anything.
# cd.

# cd~
# takes you back to the primary user directory. use it if you want to go all the way back to the user directory.
# cd~

# cp 
# copies a file or directory from one place to another. use if you want to duplicate content from one place to another
# cp datatypes.py new_file.py

# mv 
# moves files to a new location or renames the files.
# mv datatypes.py new_file.py

# rm
# removes a file permanently. use when you want to delete a file.
# rm datatypes.py

# clear 
# clears the terminal. use when you want a clean terminal.
# clear

# grep
# searches for a specific string of text in a file. use when you want to find a specific string.
# grep "ls" homework1.py

# Questions: 
# 1. touch - creates a new empty file (touch homework.py). man - opens up the manual for a command (man ls). echo - prints texts to the terminal (echo "my_script").
# 2. ls only shows visible files while ls -a shows all the files including the hidden ones.
# 3. A file that starts with a dot. they are usually hidden to keep the folder clean.
# 4. -l shows the long format (ls -l). -r recursive allowing you to delete or copy entire directories and their content (rm -r samuel). -i searches for tect regardless of uper or lowercase characters (grep -i "hello" homework1.py).