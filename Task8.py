"""
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.


Expected Output:
 For example, if the user enters 25, the output should be:

"""
#Take user input for file name
file_name=input("Enter file name :")

#Write user input to the file
try:
    with open(file_name,'w') as file:
        file_content=input("Enter text to write to the file: ")
        file.write(file_content + "\n")
        print("\nData successfully written to the output.txt.")
except FileNotFoundError:
    print("File not found.")

#Append the few more lines to the file
try:
    with open(file_name,'a') as file:
        additional_content=input("Enter additional text to append to the file: ")
        file.write(additional_content + "\n")
        print("\nData successfully appended to the output.txt.")
except FileNotFoundError:
    print("File not found.")

#read the file content and display
try:
    with open(file_name, 'r') as file:
        print("\nFinal content of the output.txt file:")
        data=file.read()
        print(data)
except FileNotFoundError:
    print("File not found.")