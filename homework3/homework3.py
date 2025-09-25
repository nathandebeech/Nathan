# 3.1 Say Goodbye

def say_goodbye(name):
    print("Goodbye,", name)

say_goodbye("Nathan")

# 3.2 Area of Circle

def area_of_circle(radius):
    print(radius ** 2 * 3.14)

area_of_circle(5)

# 4.1 Subtract, Multiply, and Divide

def subtract(a, b):
    return a - b

print(subtract(40, 5))

def multiply(c, d):
    return c * d

print(multiply(7, 5))

def divide(e, f):
    return e // f

print(divide(70, 2))

# 5.1 What Should I Wear?

def what_should_I_wear(Temperature):
    return(min(temperature), max(temperature))

temperature = [65, 50, 67, 58, 61, 62, 67, 67, 67]

print(what_should_I_wear(temperature))

# 5.2 Check if it's the Weekend

def is_weekday(day):
    if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
        return "True"
    elif day == "Saturday" or day == "Sunday":
        return "False"
    else:
        return "Not valid day"

print(is_weekday("Sunday")) 
# I attempted to assign an integer to each day and then make 1-5 be a weekday, but I could not get the code to work. How would I do that?

# 5.3 Fuel Efficiency Calculator

def fuel_efficiency(a, b):
    return a / b, "mpg"


print(fuel_efficiency(50, 4))

# 5.4 Secret Code

def encrypt_data(n):
    Last_digit = n % 10    # This provides the remainder of the number when divided by 10 (Last digit)
    remaining = n // 10    # provides the number divided by 10, no remainder
    digits = len(str(n))
    return Last_digit * 10**(digits-1) + remaining
print(encrypt_data(14245473))

# 6.1 Oski Stole Your Power


def powerless_power(x, y):
    something = 1
    for num in range(y):
        something *= x
    return something
    
print(powerless_power(3, 3))

# 6.2.1 For Loops

nums = [3, -44, 800, 8, 10]

def min_value(nums):
    possible_min_num = nums[0] #makes first number minimum number
    for num in nums:
        if num < possible_min_num:
            possible_min_num = num # if num is less than first num, then num becomes new minimum
    return possible_min_num

print(min_value(nums))

def max_value(nums):
    possible_max_num = nums[0] # first number is the possible max
    for num in nums:
        if num > possible_max_num:
                possible_max_num = num
    return possible_max_num

print(max_value(nums))

# 6.2.2 While loops

integers = [34, 4, 5, -124, 3]

def min_while(integers):
    n = 1
    minimum = integers[0]
    while n < len(integers):
          if integers[n] < minimum:
              minimum = integers[n]
          n += 1
    return minimum

print(min_while(integers))

def max_while(integers):
    n = 1
    maximum = integers[0]     # the maximum is the first integer before compared to others
    while n < len(integers):
          if integers[n] > maximum:
              maximum = integers[n]
          n += 1
    return maximum

print(max_while(integers))

# 6.3 Calculate the Sum

def weird_sum(n):
    total = 0     # starts at 0
    for digit in str((n)):
        total += int(digit)
    return total
       
print(weird_sum(2468))           # Review this one!!

# 7.1 In Your VS Code Terminal

z = 12523
result = encrypt_data(z)

print(f"The result from Encrypted Data (5.4) with z = {z} is {result})") # {z} is the imputed value for z, {result} is the result of inputing {z} into the function

# Average_vowels.py Questions

# 1. Counting Vowels

def counting_vowels_and_consonants(string):
    total_vowels = 0
    total_consonants = 0
    vowels = ["a", "e", "i", "o", "u", "y"]    # Why is sometimes vowel, so I placed it here
    consonants = ["b", "c,", "d", "f", "g", "h", "j,", "k", "l", "m", "n", "p,", "q", "r", "s", "t", "v,", "w", "x", "z"]
    for letter in string:
        if letter in vowels:
            total_vowels += 1
        if letter in consonants:
            total_consonants += 1
    return total_vowels, total_consonants

print(counting_vowels_and_consonants("54iowqoir3thasd"))  # I didnt use the hint for this problem but my function still works. Is that okay?


# 2. Average Vowels

def average_vowels(paragraph):
    period = ["."]
    total_sentences = 0
    for character in paragraph:
        if character in period:
            total_sentences +=1
    total_vowels = 0
    vowels = ["a", "e", "i", "o", "u", "y"]    # Why is sometimes vowel, so I placed it here
    for letter in paragraph:
        if letter in vowels:
            total_vowels += 1
    average = total_vowels // total_sentences
    return average

print(average_vowels("I love tomatoes so much. The make any food they are added to absolutely amazing.For example, when a tomato is of very good quality, it can drastically improve the taste of a sandwich. It adds a crisp while also adding juice to create a well balanced and wonderful result."))