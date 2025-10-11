# Homework5.py

# 3 Homeowrk 1 + 2 Review
# 3.1 Vocabulary Review

# 1. Git is the software allowing you to track changes in repositories.
# Github is the hub or system that follows this changes. It is a website.

# 2. Command line is where commands are entered. Terminal is the software that outputs the commands.

# 3. Local is on your computer. Remote is through the internet.

# 4. Version control is wht allows you to revert to previos versions of a file

# 5. The area where changes are prepared to be sent through Git

# 6. moves the file to staging area

# 7. saves the file and prepares for transfer

# 8. moves file to the remote repository

# 9. checks the status of saved files

# 10. takes files from remote to local

# 11. shows path of directories

# 12. lists whats inside of current directory

# 13. opens directory

# 14. opens a file or text

# 15. creates file of text

# 16. allows you to move directories

# 17. removes directory

# 18. display content of txt or file.


# 3.2 A Directory Tree

# Questions:

# 1. pwd

# 2. ls

# 3. cd ../brianna_repo
# git commit
# git pull

# 4. cp ../judy_decal/homework/homework.py

# 5. cd ../judy_decal/homework

# 6. nano homework.py

# 7. git add
# git commit
# git push

# 8. This error means that the file she attempted to push has
# different information remotly. To fix this, Judy must first use git pull,
# git commit, and then send the changes to the remote repository

# 9. cd ../../Recent/

# 3.3 Draw Your Directory Tree

# 4. Homework 3 Review

# 4.1 Data Types

def checkDataType(something):
    print(type(something))
checkDataType(3.14)
checkDataType(True)

# 4.2

def evenOrOdd(number):
    if number == 0:
        print("That's 0")
    elif number % 2 != 0:
        print("Odd")
    elif number % 2 == 0:
        print("Even")
evenOrOdd(7)
evenOrOdd(10)
evenOrOdd(0)

# 5 Loops

numbers = [1, 2, 3, 4, 5]

def sumWithLoop(list):
    total = 0
    for num in list:
        total = total + num
    print(total)
sumWithLoop(numbers)

# 6. Homework 4 Review

# 6.1 Lists

def duplicateList(list):
    newlist = []
    for string in list:
        newlist.append(string)
        newlist.append(string)
    print(newlist)
duplicateList(["a", "b", "c"])

# 6.2 Debugging

def square(num):
    return num * num
print(square(9))
# They forgot to include the colon after the first line of the function

# 7. Running Your Code

# 7.1 VS Code

# 7.2 In Your VS Code Terminal

# Favorite Function:
def duplicateList(list):
    newlist = []
    for string in list:
        newlist.append(string)
        newlist.append(string)
    print(newlist)
duplicateList(["a", "b", "c"])