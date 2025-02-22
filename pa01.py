'''====================================================================
| Assignment: pa01 - Encrypting a plaintext file using the Hill cipher
|
| Author: Joseph Letobar
| Language: Python
| python3 pa01.py kX.txt pX.txt
| where kX.txt is the keytext file
| and pX.txt is plaintext file
| Note:
| All input files are simple 8 bit ASCII input
| All execute commands above have been tested on Eustis
|
| Class: CIS3360 - Security in Computing - Spring 2025
| Instructor: McAlpin
| Due Date: 2/23
+==================================================================='''

import sys
import math

# Get arguments
key = sys.argv[1]
plaintext = sys.argv[2]

#--- Open key ---#
try: 
    with open(key, 'r') as file:
        key_content = [line.strip().split() for line in file]  # Strip each line and make it a nested list
        matrix_size = int(key_content[0][0]) # Store the matrix size
        del key_content[0]  # Then delete the identifier from the key content
        print("")
        print(f"Key Content: \n{key_content}")  # Print  
except:
    print("Error reading key text")
print("")

# Print the key
print("The Key:")
try:
    for i in range(matrix_size):
        for j in range(0, matrix_size):
            print(key_content[i][j], end=" ")
        print("")    
except:
    print("Error")

#--- Plaintext ---#

# Open plaintext
try: 
    with open(plaintext, 'r') as file:
        plaintext_content = file.read().replace("\n", "")
        plaintext_content = "".join(c for c in plaintext_content if c.isalnum())
except:
    print("Error reading key text")

print("")
print(f"Raw Plaintext Content: \n{plaintext_content}")
print("")

# Dict storing character and its numerical value in alphabet
char_buffer = {
    "character" : [],
    "numerical" : [],
}
# Convert the plaintext letters to numerical values
i=0
numerical_values = []
for char in plaintext_content:
    char_buffer["character"].append(char)

    # If current plaintext value is already a number (and note at which position its at for later)
    if char.isdigit():
        numerical_values.append(i)
        char = int(char)
        char_buffer["numerical"].append(char)
    # Else, convert to number
    else:
        char = char.upper()
        char = ord(char) - ord('A')
        char_buffer["numerical"].append(char)
    i+=1
i=0
original_group_buffer = []
group_buffer = []

# Create a nested list for the plaintext groups
for i in range (0, len(plaintext_content), 2,):
    try:
        original_group_buffer.append([char_buffer["character"][i], char_buffer["character"][i+1]])
        group_buffer.append([char_buffer["numerical"][i], char_buffer["numerical"][i+1]])
    except:
        print("out of range")

group_length = (len(plaintext_content))/2
group_length = int(group_length)

print("")
print(f"Grouped Numerical Plaintext Content: ")
for i in range (0, group_length):
    try: 
        print(group_buffer[i])
    except Exception as e:
        print(f"Out of range:{e}")    
print("")

# Multiply
print("-----------------------")
print("")

#'''
results = []
# Go through amount of plaintext
for i in range((len(group_buffer))):
    # Row of matrix
    for j in range(matrix_size):
        current_plaintext = int(group_buffer[i][j])
        inner_list = []
        # Column of matrix
        for k in range(matrix_size):
            current_key = int(key_content[j][k])
            print(f"Multiplication: {current_plaintext} * {current_key}")
            result = (current_plaintext * current_key)
            inner_list.append(result)
        results.append(inner_list)
print()
#print(results)


# Group results into lists
main_grouped_list = []
i=0
while i < len(plaintext_content):
    grouped_list = []
    for j in range(matrix_size):
        try: 
            grouped_list.append(results[i])
        except:
            print("out of RANGE")    
        i+=1
    main_grouped_list.append(grouped_list)
print(main_grouped_list)

# Do arithmetic on groups
#print(len(main_grouped_list))

i = 0
# Go list by list
result_list = []
while i < len(main_grouped_list):
    # Inner elements
    current_list = []
    for j in range(matrix_size):
        try: 
            current = main_grouped_list[i][j]
            addition = sum(current)
            print(addition)
            modulo = (addition % 26)
            print(modulo)
            current_list.append(modulo)
        except:
            print("out of RANGE")    
    i+=1
    result_list.append(current_list)

print()
#print(result_list)
print()
print("-----------------------")
print()

# Convert to ciphertext
i=0
for sublist in result_list:    # Outer elements
    for num in sublist:
        if i in numerical_values: # If it was already a number
            print(num, end="")
        # Else, convert to letter
        else:
            character = num + ord('A')
            character = chr(character)
            character = character.lower()
            print(character, end="")
        i+=1
'''
result0 = int(key_content[l][k]) * int(group_buffer[i][j])

result1 = int(key_content[l][k+1]) * int(group_buffer[i][j])           

print(f"{i} | {key_content[l][k]}*{group_buffer[i][j]}|{original_group_buffer[i][j]} = {result0}")

print(f"{i} | {key_content[l][k+1]}*{group_buffer[i][j]}|{original_group_buffer[i][j]} = {result1}")

final_result0 = ((result0 + result1)%26)
final_result0 = final_result0 + ord('A')

print(f"The final result is: {chr(final_result0)}")
print("")
'''
#''' 

"""
result0 = int(key_content[1][0]) * int(char_buffer["numerical"][0])
result1 = int(key_content[1][1]) * int(char_buffer["numerical"][1])
final_result0 = chr(((result0 + result1)%26) + ord('A'))
print(final_result0, end="")

result2 = int(key_content[2][0]) * int(char_buffer["numerical"][0])
result3 = int(key_content[2][1]) * int(char_buffer["numerical"][1])
final_result1 = chr(((result2 + result3)%26) + ord('A'))
print(final_result1, end = "")
"""

'''
print(result0)
print(result1)
print(result2)
print(result3)
'''


"""
print(f"key content: {key_content[i][j]}")
print(f"char buffer: {char_buffer["numerical"][1]}")
result = int(key_content[i][j]) * int(char_buffer["numerical"][1])
print(f"RESULT: {result}")
"""

print("")

print("")



'''=============================================================================
| I Joseph Letobar 5658506 affirm that this program is
| entirely my own work and that I have neither developed my code together with
| any another person, nor copied any code from any other person, nor permitted
| my code to be copied or otherwise used by any other person, nor have I
| copied, modified, or otherwise used programs created by others. I acknowledge
| that any violation of the above terms will be treated as academic dishonesty.
+============================================================================'''