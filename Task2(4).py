# weiting to a file
print("Enter the text to write to the file:")
text1=input()
file1 = open('output.txt', 'w')
file1.write(text1 + "\n")
print("Data successfully written to output.txt")
file1.close()
# Appending to the file
print("Enter the additional text to append:")
text2 = input()
file2 = open('output.txt', 'a')
file2.write(text2 + "\n")
print("Data successfully appended")
file2.close()
# Reading the file content
print("Final content on the output.txt:\n")
text3 = input()
file3 = open('output.txt', 'a')
file3.write(text3 + "\n")
print("Learning file handling in python.")
file3.close()

