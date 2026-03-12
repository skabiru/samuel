#File:homework3. py
# --- Say Goodbye ---
def say_goodbye(name): # prints a goodbye message with a persons name
    print("Goodbye,", name)
# --- Area of a Circle ---
def circle_area(radius):
    # takes the radius plugs it into a formula and returns the area
    pi = 3.14 # approximates pi to be 3.14
    area = pi * (radius ** 2) # plugs variables into the formula for finding area and gets the area
    print(area) # prints the resulting area

# --- Subtract, Multiply and Divide ---
def subtract(a, b):
    # subtracts b from a and returns the result
    return a - b
def multiply(a, b):
    # multplies a and b then returns the result
    return a * b
def divide(a, b):
    # divides a by b amount of times then returns the result
    return a / b 

# --- What Should I Wear? ---
def max_min_temps(temps):
    #gets the min and max using built in functions and returns their values inside a tuple
    return (min(temps), max(temps))
# --- Check if its the weekend ---
def is_weekend(day):
    #checks if day equals 6 or 7 as those values correspond to the wekeend
    if day == 6 or day == 7:
    #if either of them is true it will return true 
        return True
    else:
        return False # returns this statement if the number is neither 6 nor 7
# --- Fuel Efficiency Calculator
def fuel_efficiency(miles, gallons):
    #takes in miles and gallons and divides miles by gallons to get the mpg
    mpg = miles/gallons
    return mpg # returns the fuel efficiency as mpg
# --- Secret Code ---
def encrypt_data(number):
    # get the last number and the numbers before the last number
    if len(str(number)) < 2: # this is cause if its just one number we dont need to change anything
        return number
    last_number = number % 10
    numbers_before = number // 10
    factor = len(str(numbers_before))
    # move the last to first then add the rest of the numbers behind it
    encrypted = last_number * (10 ** factor) + numbers_before # in the example this would make 50000 + 1234
    return encrypted

# --- Loops ---
def power_func(x, y):
    #set the an initial value. in this case the lowest answer we can get is 1 as anything to the power of 0 is one
    result = 1 
    # loops y times in order to multiply the result by x y times
    for i in range(y):
        result *= x
    return result

def min_value(numbers):
    # make the first number the least
    curr_min = numbers[0] # gets the first number of the list
    #iterate thru the list and if its finds a smaller number it will replace the current min
    for num in numbers:
        if num < curr_min:
            curr_min = num
    return curr_min

def max_value(numbers):
    # same as above but flips the sign and the current min to current max
    curr_max = numbers[0]
    for num in numbers:
        if num > curr_max:
            curr_max = num
    return curr_max

def min_value_while(numbers):
    #set current min as the first numeber and start the while loop counter at 0
    i = 0
    curr_min = numbers[0]
    # loops through the numbers once it gets to the last numbers and runs it will stop as the i would be the same as the len of the numbers
    while i < len(numbers):
        if numbers[i] < curr_min: # compares the numbers and repaces the current min if it finds a smaller number in the list
            curr_min = numbers[i]
        # adds 1 to i each time we go through this process to keep track of the number of numbesr we have gone thorugh
        i += 1
    return curr_min

def max_value_while(numbers):
    # same concept as above
    i = 0
    curr_max = numbers[0]
    # loops through the numbers once it gets to the last numbers and runs it will stop as the i would be the same as the len of the numbers
    while i < len(numbers):
        if numbers[i] > curr_max: # if it finds a bigger number it will replace the current max
            curr_max = numbers[i]
        i += 1
    return curr_max

def sum_digits(interger):
    # start the total at 0 and add each number to the total
    result = 0 
    # change the int to a str so u can loop through it and add the digits
    for i in str(interger):
        result += int(i)
    return result

x = 2
y = 3
result = power_func(x,y) 
print(f"The result of Oski Stole Your Power (5.1) with x = {x} and y = {y} is {result}.")