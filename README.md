# Tutudude_Assignment4

Task 1: Reading and Writing a File
Description

This program demonstrates how to write text to a file and then read the content back in Python. It also includes error handling using try-except.

Steps

Open (or create) a file named sample.txt in write ('w') mode.

Write multiple lines of text to the file.

Close the file after writing.

Reopen the file in read ('r') mode and print its content.

Use try-except to handle the case if the file does not exist.

Example Output
Reading file content:
Line1:This is a sample text file.
Line2:It contains multiple lines.


Task 2: Writing, Appending, and Reading a File
Description

This program demonstrates how to:

Write user input to a file (output.txt).

Append additional text to the same file.

Display the final content of the file.

Steps

Ask the user for input text and write it to output.txt (write mode 'w').

Ask for more text and append it to the file (append mode 'a').

Ask again for text and append it to the file.

Print confirmation messages after each operation.

Example

Enter the text to write to the file:
Hello, world!
Data successfully written to output.txt

Enter the additional text to append:
This is my second line.
Data successfully appended

Final content on the output.txt:
Python file handling is fun!
Learning file handling in python.
