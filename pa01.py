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
import textwrap

# Get arguments
key = sys.argv[1]
plaintext = sys.argv[2]

#--- Open key ---#
try: 
    with open(key, 'r') as file:
        key_content = [line.strip().split() for line in file]  # Strip each line and make it a nested list
        matrix_size = int(key_content[0][0]) # Store the matrix size
        del key_content[0]  # Then delete the identifier from the key content
        #print(f"Key Content: \n{key_content}")  # Print  
except:
    print("Error reading key text")

# Print the key
print()
print("Key matrix:")
try:
    for i in range(matrix_size):
        for j in range(0, matrix_size):
            print(key_content[i][j], end=" ")
        print("")    
except:
    print("Error")
print()
  

#--- Plaintext ---#
# Open plaintext
try: 
    with open(plaintext, 'r') as file:
        plaintext_content = file.read().replace("\n", "")
        plaintext_content = "".join(c.lower() for c in plaintext_content if 'a' <= c.lower() <= 'z')
except:
    print("Error reading key text")

# Check if it needs padding
remainder = (len(plaintext_content)) % matrix_size
if remainder != 0:
    padding_needed = matrix_size - remainder
    plaintext_content += ('x') * padding_needed

# Print out the plaintext 
formatted_plaintext = textwrap.fill(plaintext_content, width=80)  # Wrap to 80 columns
print(f"Plaintext:\n{formatted_plaintext}")

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
    char = char.upper()
    char = ord(char) - ord('A')
    char_buffer["numerical"].append(char)
    i+=1
i=0
original_group_buffer = []
group_buffer = []

# Create a nested list for the plaintext groups
for i in range (0, len(plaintext_content), matrix_size):
    try:
        original_group_buffer.append(char_buffer["character"][i:i + matrix_size])
        group_buffer.append(char_buffer["numerical"][i:i + matrix_size])
    except:
        print("out of range")

group_length = (len(plaintext_content))/matrix_size
group_length = int(group_length)
#print(f"Group buffer: {group_buffer}")

# Multiply

#'''
results = []
#print(key_content)
# Go through amount of plaintext
for i in range((len(group_buffer))):
    plaintext_vector = group_buffer[i]
    #print(plaintext_vector)
    # Row of matrix
    for j in range(matrix_size):
        inner_list = []
        # Column of matrix
        for k in range(matrix_size):
            try:
                current_plaintext = int(plaintext_vector[k])
                current_key = int(key_content[j][k])
                #print(f"The curent plaintext{plaintext_vector[k]}", end="")
                #print(f"Multiplication: {current_plaintext} * {current_key}")
                result = (current_plaintext * current_key)
                inner_list.append(result)
            except Exception as e:
                print(f"Out of range {e}")
        results.append(inner_list)

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
#print(main_grouped_list)

# Do arithmetic on groups
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
            #print(addition)
            modulo = (addition % 26)
            #print(modulo)
            current_list.append(modulo)
        except:
            print("out of RANGE")    
    i+=1
    result_list.append(current_list)

# Convert to ciphertext
print()
i=0
ciphertext_content = ""
for sublist in result_list:    # Outer elements
    for num in sublist:
        character = num + ord('A')
        character = chr(character)
        character = character.lower()
        ciphertext_content += character
        i+=1

# Print the ciphertext
formatted_ciphertext = textwrap.fill(ciphertext_content, width=80)  # Wrap to 80 columns
print(f"Ciphertext:\n{formatted_ciphertext}")

'''=============================================================================
| I Joseph Letobar 5658506 affirm that this program is
| entirely my own work and that I have neither developed my code together with
| any another person, nor copied any code from any other person, nor permitted
| my code to be copied or otherwise used by any other person, nor have I
| copied, modified, or otherwise used programs created by others. I acknowledge
| that any violation of the above terms will be treated as academic dishonesty.
+============================================================================'''