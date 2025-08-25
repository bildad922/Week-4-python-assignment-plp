## Python File Program
This program was created to demonstrate fundamental file handling concepts in Python in a simple, step-by-step manner.

## Code Explanation
import os: This imports the os module, which lets the program interact with the operating system to check for file existence.

with open(...): This is the best practice for file handling in Python. It automatically closes the file when the program is done with it, even if an error occurs.

.read() & .upper(): The .read() method reads the entire file content into a string, and .upper() converts all characters to uppercase.

try...except: This block is used for error handling to prevent the program from crashing if a file isn't found or an I/O error occurs.