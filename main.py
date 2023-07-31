# orangutype-py shows user what to type challenges user to type it
# Libraries imports
import os
import time
import msvcrt


# Startup and variables
print("Setting up...")
promptStr= "There once was a man that lived on the butte of a mountain"
prompt = promptStr.split()
final = []
word = ""
print(prompt)

response = []
time.sleep(2)

# Main game loop
while (True):
    # gets input
    char = msvcrt.getch()
    if char != b' ':
        word += char.decode('ASCII')
    else:
        response.append(word)
        word = ""
    print("char: " + str(char))
    print("word: " + word)
    print(response)


