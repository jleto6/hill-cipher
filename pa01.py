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
#print("Arguments:", key, plaintext)

# Open key
try: 
    with open(key, 'r') as file:
        key_content = [line.strip().split() for line in file]  # Strip each line
        print(key_content)  # Now it's a clean list
except:
    print("Error reading key text")

# Open plaintext
try: 
    with open(plaintext, 'r') as file:
        plaintext_content = file.read().replace("\n", "")

except:
    print("Error reading key text")




print("")
# Matrix multiplication
print("")


# Plaintext

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
for i in range (0, len(plaintext_content), 2,):
    
    try:
        print(char_buffer["character"][i], end=" ")
        print(char_buffer["numerical"][i])

        print(char_buffer["character"][i+1], end=" ")
        print(char_buffer["numerical"][i+1])

    except:
        print("out of range")

    print("")

print("------")
print("")


# Pieces of the key
#print(key_content[1][1])
matrix_size = int(key_content[0][0])
for i in range(1, matrix_size + 1):
    for j in range(0, matrix_size):
        print(key_content[i][j], end=" ")
    print("")

# Multiply
print("")
print("-----")

result0 = int(key_content[1][0]) * int(char_buffer["numerical"][0])
result1 = int(key_content[1][1]) * int(char_buffer["numerical"][1])
final_result0 = chr(((result0 + result1)%26) + ord('A'))
print(final_result0)

result2 = int(key_content[2][0]) * int(char_buffer["numerical"][0])
result3 = int(key_content[2][1]) * int(char_buffer["numerical"][1])
final_result1 = chr(((result2 + result3)%26) + ord('A'))
print(final_result1)

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