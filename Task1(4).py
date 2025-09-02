'''try:
    # Write to the file
    with open('sample.txt', 'w') as file1:
        file1.write("Reading file content:\nLine1:This is a sample text file.\nLine2:This contains multiple lines.")

    # Read from the file
    with open('sample.txt', 'r') as file1:
        content = file1.read()
        print(content)
except FileNotFoundError:
    print("The file sample.txt does not exist.")'''
try:    
    file1 = open('sample.txt', 'w')
    file1.write("Reading file content:\nLine1:This is a sample text file.\nLine2:It contains multiple lines.")
    file1.close()
    file1 = open('sample.txt', 'r')
    print(file1.read())
    file1.close()
except FileNotFoundError:
    print("The file sample.txt does not exist.")
file1.close()







