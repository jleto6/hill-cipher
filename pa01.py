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
char_buffer = {}
i=0
for char in plaintext_content:
    char_buffer.append(char)
    #print(char_buffer[i])
    i+=1
i=0
for i in range (0, len(plaintext_content), 2):
    
    try:
        print(char_buffer[i])
        print(char_buffer[i+1])
    except:
        print("out of range")

    print("")
    i+=2    

print("------")
print("")


# Pieces of the key
#print(key_content[1][1])
matrix_size = int(key_content[0][0])
key_buffer = []
for i in range(1, matrix_size + 1):
    for j in range(0, matrix_size):
        #print(key_content[i][j])
        print(key_content[i][j], end=" ")

    print("")



'''=============================================================================
| I Joseph Letobar 5658506 affirm that this program is
| entirely my own work and that I have neither developed my code together with
| any another person, nor copied any code from any other person, nor permitted
| my code to be copied or otherwise used by any other person, nor have I
| copied, modified, or otherwise used programs created by others. I acknowledge
| that any violation of the above terms will be treated as academic dishonesty.
+============================================================================'''