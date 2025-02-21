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

# Get arguments
key = sys.argv[1]
plaintext = sys.argv[2]

#--- Open key ---#
try: 
    with open(key, 'r') as file:
        key_content = [line.strip().split() for line in file]  # Strip each line and make it a nested list
        print("")
        print(f"Key Content: \n{key_content}")  # Print  
except:
    print("Error reading key text")
print("------------------")

#--- Plaintext ---#

# Open plaintext
try: 
    with open(plaintext, 'r') as file:
        plaintext_content = file.read().replace("\n", "")
except:
    print("Error reading key text")

# Dict storing character and its numerical value in alphabet
char_buffer = {
    "character" : [],
    "numerical" : [],
}
i=0
for char in plaintext_content:
    char_buffer["character"].append(char)

    # Convert to number
    if char.isdigit():
        char_buffer["numerical"].append(char)
    else:
        char = char.upper()
        char = ord(char) - ord('A')
        char_buffer["numerical"].append(char)
    i+=1
i=0
group_buffer = []

# Create a nested list for the plaintext groups
for i in range (0, len(plaintext_content), 2,):
    try:
        group_buffer.append([char_buffer["character"][i], char_buffer["character"][i+1]])
    except:
        print("out of range")
print("")
print(f"Plaintext content (grouped): \n{group_buffer}")
print("")

group_length = (len(plaintext_content))/2
group_length = int(group_length)

for i in range (0, group_length):
    try: 
        print(group_buffer[i])
    except Exception as e:
        print(f"Out of range:{e}")    
print("")
print("------")
print("")

# Pieces of the key
print("The Key \n")
matrix_size = int(key_content[0][0])
for i in range(1, matrix_size + 1):
    for j in range(0, matrix_size):
        print(key_content[i][j], end=" ")
    print("")

# Multiply
print("")
print("------")
print("")

k=-1
for h in range((len(plaintext_content))):
    #print(h)
    for i in range(1, matrix_size + 1):
        k+=1
        for j in range(matrix_size):
            result0 = int(key_content[i][j]) * int(char_buffer["numerical"][k])
          
            result1 = int(key_content[i][j]) * int(char_buffer["numerical"][k+1])           

            print(f"{i} | {key_content[i][j]}*{char_buffer["numerical"][k]}|{char_buffer['character'][k]} = {result0}")
            print(f"{i} | {key_content[i][j]}*{char_buffer["numerical"][k+1]}|{char_buffer['character'][k+1]} = {result1}")
            
            final_result0 = ((result0 + result1)%26)

            final_result0 = final_result0 + ord('A')

            print(f"The final result is: {chr(final_result0)}")
            print("")

print(plaintext_content)
print("---+--")        

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