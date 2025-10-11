# 3.1 List Operations 

favorite_foods = ["pasta", "pizza", "prosciutto sandwhich", "dumplings", "breakfast buritto"]

# 1.
print(favorite_foods[1])

# 2.
print(favorite_foods[-1])

# 3.
favorite_foods.append("grapes")

# 4. 
favorite_foods.insert(0,"apple")
print(favorite_foods)

# 5.
favorite_foods.remove("prosciutto sandwhich")
print(favorite_foods)

# 6. 
print(len(favorite_foods))

#  7.
def uppercase_foods(some_list):
    for food in some_list:
        return food.upper()
    
print(uppercase_foods(favorite_foods))

# 8.
print(favorite_foods[::4])

# 9.
def potato_checker(list):
    if "potato" in list:
        return "A potato!"
    else:
        return "No potato!"
print(potato_checker(favorite_foods))


# 3.2 Slicing and Striding

numbers = list(range(0,21))

# 1.
def get_first_fifteen(list):
    return list[0:16]
2.
def get_every_fifth(list2):
    return list2[::5]

# 3.
def reverse_and_stride(list3):
    return list3[::-1]
print(reverse_and_stride(get_every_fifth(get_first_fifteen(numbers))))

# 3.3 Nested Lists
# 3.3.1 Nested List Operations

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# 1.
print(numbers[2])

# 2. 
print(numbers[1][1])

# 3. 
numbers.append([10, 11, 12])

# 4.
def sum_nested(nested_list):
    for row in nested_list:
        print(sum(row)) 

sum_nested(numbers)

# 3.4 Create a 5x5 List 


def five_by_five(things):
    nestedlist = [

    ]
    a = 0
    b = 5
    first_list = things[a:b]
    for first_list in things:
        if b <= len(things):
            nestedlist.append(things[a:b])
            a += 5
            b += 5
    return nestedlist
print(five_by_five(list(range(1,26))))

# 1.
first_five_by_five = five_by_five(list(range(1,26)))

def questioned_five_by_five(nested_list):
    questioned_list = []
    for row in nested_list:
        new_row = []
        for number in row:
            if number % 3 == 0:
                new_row.append("?")
            else:
                new_row.append(number)
        questioned_list.append(new_row)
    return questioned_list

print(questioned_five_by_five(first_five_by_five))

# 2.
second_five_by_five = questioned_five_by_five(first_five_by_five)

def sum_questioned_five_by_five(nested_list):
    sum = 0
    for row in nested_list:
        for number in row:
            if number != "?":
                sum += number
    return sum
                 
print(sum_questioned_five_by_five(second_five_by_five))

# 4. Dictionaries

# 4.1 Dictionary Operations

ages = { 
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}

# 1.

print(ages["Katie"])

# # 2.

ages["Mira"] = 100
print(ages)

# 3.

ages["Milana"] = 52
print(ages)

# 4.

ages.pop("Mariam")
print(ages)

#  5.

for key, value in ages.items():
    print(key, value)


# 5.2 In Your VS Code Terminal

# Favorite function:
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def sum_nested(nested_list):
    for row in nested_list:
        print(sum(row))
sum_nested(numbers)




