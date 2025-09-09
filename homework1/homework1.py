# File: homework1. py


# --- 3.1 Variables and Data Types ---


a = 10
print(a)
print(type(a))
# a is an integer, whole number, no decimal

b = 1.5
print(b)
print(type(b))
# b is a float, number with decimal/fraction

c = 3j
print(c)
print(type(c))
# c is a complex datatype. 3j is the imaginary part of an imaginary number (j is used instead of i in python)

d = "hello"
print(d)
print(type(d))
# d is a string datatype (words!)

e = [1, 2, 3]
print(e)
print(type(e))
# e is a list. ordered things inside brackets

f = {"name": "Nathan", "favorite fruit": "pinapple"}
print(f)
print(type(f))
# f is a dictionary. This stores pairs of words

g = (1, 2)
print(g)
print(type(g))
# g is a tuple, sequences of elements

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h))
# h is a list, a changable sequence of items

i = True
print(i)
print(type(i))
# i is a boolean, true or false values

j = None
print(j)
print(type(j))
# j is a nonetype, the only possible value is none

k = [True, "blue", 12]
print(k)
print(type(k))
# k is a mixd list, a list with varrying data types

l = str(14)
print(l)
print(type(l))
# l is a string, the str() converts value into string

m = 1e4
print(m)
print(type(m))
# m is a floating-point, number in scietific notation (to the 4th power in this example)

# 1. There are 9 data types
# 2. Integer, Float, Complex, String, List, Dictionary, Tuple, Boolean, None Type, 
# 3. b and m are both floating; e, h, and k are all lists; d and l are both string
# 4.  Str() converts an the entered value into a string datatype
# 5.

n = b"Hello"
print(n)
print(type(n))
# n is a byte or binary data, they handle raw data. a fundamental way to hold information


# --- 3.2 Booleans ---


print(10>9) # True, 10 is greater than 9

print(10==9) # False, 10 is not equal to 9

print(10<=9) # False, 10 is not less than or equal to 9

print(bool("abc")) # True, something typed in the boolean means it is true

print(bool(123)) # True, same explanation as above

print(bool(["apple", "cherry", "banana"])) # True, same as above
# In the homework one document, each fruit has '' instead of " at the beginning. Was that a mistake?

print(bool(True)) # True, the input was true, so the output was true

print(bool(False)) # False, the input was false, so the output was false

print(bool(0)) # False, non zero numbers are true while zero is false

print(bool("")) # False, the string is empty, therefore false

print(bool(" ")) # Ture, there is a space in the string

print(bool(())) # False, the string is empty, therefore false

print(bool([])) # False, the string is empty, therefore false

print(bool({})) # False, the string is empty, therefore false

print(bool(True and False)) # False, both strings must be true to output true

print(bool(True and True)) # True, both strings are true

print(bool(False and False)) # False, both strings are false

print(bool(True or False)) # True, one of the strings are true

print(bool(True or True)) # True, both of the strings are true

print(bool(False or False)) # False, both strings are false

print(bool(not(False))) # True, the string is the opposite of false

print(bool(not(True))) # False, the string is the opposite of true

# 1. When there is information in the string, it is false unless there is an and or or GeneratorExit
# 2. print(bool(" "))
# 3. 
z="tomato"
print(bool("tomato"))
#4.
print(bool(False and False or False))


# --- 3.3 Operators ---
# --- 3.3.1 Arithmetic ---

print(10+5) #15, performs addition

print(10-5) # 5, performs substraction

print(2*4) # 8, performs multiplication

print(6/3) # 2.0, performs division

print(5%2) # 1, outputs the remander after division

print(3**2) # 9, raised to an exponet

print(15//2) # 7, division but rounds to the nearest whole number


# --- 3.3.2 Comparison ---


print(5 == 2) # False, True if numbers are equivalent

print(10 != 10) # False, True if numbers are nonequivalent

print(2<5) # True, less than symbol

print(12>5) # True, greater than symbol

print(5<=6) # True, equal to or greater than symbol

print(1>=10) # False, less than or equal to symbol


# --- 3.3.3 Assignments ---


x=5

x += 5 
print(x) # 10, sets variable to equal + 5

x -= 4 
print(x) # 6, sets variable to equal - 4

x *= 3
print(x) # 18, multiplies variable by 3


# --- 3.3.4 Logical ---


# 1. The operator and requires both elements to be true for an output to be True
print(False and False)

# 2. The operator or reuqires one element to be true for an output to be True 
print(False or False) 

# 3. The operator not produces and output that is oposite to the input
print(not(True))

# 1. / = division. // = rounds the answer of the division problem to the nearest whole number
# 2. % = provides remainder of division. // = rounds the answer of the division problem to the nearest whole number
# 3. The percentage sign
print(4002%4)
# 4. They assign variables values and can alter their assigned values


# --- 3.4 Strings ---


my_string = "hello"

print(my_string) # Output: hello

print(my_string[0]) # Output: h (first letter of word)

print(my_string[1]) # Output: e (second letter of word)

print(my_string[2]) # Output: l (third letter of word)

print(my_string[3]) # Output: l (fourth letter of word)

print(my_string[4]) # Output: o (fifth letter of word)

print(my_string[-1]) # Output: o (last letter of word)

print(my_string[1:3]) # Output: el (letter 1 through 3)

print(my_string[0:5:2]) # Output: hlo (takes every second indecy besides the first because it starts at h)

print(len(my_string)) # Output: 5 (number of indecies)

print(my_string + "goodbye") # Output: hellogoodbye (put the output of my_string and the word)

print(my_string * 7) # hellohellohellohellohellohellohello (prints my_string seven times)


# --- 3.4.1 Strings ---


# 1. Slicing extracts portions of a sequence or specific patterns in a sequence. Slicing occured whenever there was a : part 8 and 9 of 3.4
# 2. 
name = "Oski"
print("Hello, my name is", name) # outputed the combination of "" and the word associated with name

# 3. 
print(f"Hello, my name is {name}") # outputed the same as above

# 4. An f string is used in the latter line. This string allows a variable to be added to the string without seperation of a common


# --- 3.5 Terminal Commands ---

