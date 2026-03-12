#File:homework4. py
# --- Lists ---
foods = ["sushi", "tacos", "steak", "burgers", "fries"]
print(foods[1])
print(foods[-1])
foods.append("pizza")
foods.insert(0, "apple")
"""
I encountered this error:
TypeError: list.append() takes exactly one argument
I originally wrote: foods.append(o, "apple")
I thought that I could add apple to a specific index using append(). I fixed it by looking up a function that does inserts.
"""
foods.remove(foods[2])
print(len(foods))
for food in foods:
    print(food.upper())
new_foods_list = [foods[0], foods[-1]]
if "potato" in new_foods_list:
    print("A potato!")
else:
    print("No potato!")
# --- slicing and Striding
numbers = list(range(21))
def get_first_15(numbers):
    return numbers[:15] # goes from index 0 to 14 giving us 15 numbers
def get_every_5th(list):
    return list[::5] # step 5 makes it return every 5 numbers
def reverse_and_stride(list):
    reverse = list[::-1] # reverses the order of the list and sets it equal to a new variable
    every_3rd = reverse[::3] # takes every 3rd element
    return every_3rd
step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)
print(f"Final list is {step3}")
# --- Nested Lists
numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(numbers[2])
print(numbers[1][1])
numbers.append([10, 11, 12])
def sum_nested(nested_list): 
    total = 0 # initialize the problem so we can start counting
    for i in nested_list: # goes through each row
        for item in i: # goes through each item and then adds them to the total
            total += item
    return total
def create_5x5():
    list5x5 = [] # makes the outer brackets that will hold the different rows
    current_number = 1 # makes sure that we start from 1 and go up
    for i in range(5): # this will makes the 5 rows 
        row = [] #sets up the row skeleton so we can add numbers to it
        for j in range(5): # loops 5 times so we can add five nums to each row
            row.append(current_number) # adds the current num to the row
            current_number += 1 # adds one to the current num so we can keep adding the nect number
        list5x5.append(row) # adds the complete row of 5 numbers to the 5x5 grid 
    return list5x5
my_5x5_list = create_5x5()
def replace_multiple_3(nested_list):
    for i in range(len(nested_list)): # runs through each row and the len just makes it general where any form of list can work with this func.
        for j in range(len(nested_list[i])):
            if nested_list[i][j] != "?" and nested_list[i][j] % 3 == 0:
                nested_list[i][j] = "?"
    return nested_list
question_mark_5x5_list = replace_multiple_3(my_5x5_list)
"""
I encountered this error:
TypeError: not all arguments converted during string fomratting.
I originally wrote: for j in range(len(nested_list[i])): if j % 3 == 0:
I thought that j would represent the number itself but its just like a placeholder. I fixed it by using the column row indexing to get the value of the current position.
"""
def add_elemen_not_marks(grid):
    total = 0 #initialize the count
    for row in grid:
        for i in row:
            if i != "?":
                total += i
    return total
sum_no_question_marks = add_elemen_not_marks(question_mark_5x5_list)
# --- Dictionaries ---
ages = {"Katie": 30, "Mariam": 42, "Safia": 25, "Mira": 48}
print(ages["Katie"])
ages["Mira"] = 100
ages["Milana"] = 52
del ages["Mariam"]
for name in ages:
    print(name, ages[name])
# favorite
favorite = sum_nested(numbers)
print(favorite)