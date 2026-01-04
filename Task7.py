"""
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
"""

try:
    with open("sample.txt", "w") as file:
        file.writelines("This is a sample text file.\nIt contains multiple lines of text.\nEnjoy reading!")
        file.writelines("This is the second line of the file.")
        file.writelines("This is the third line of the file.")
except Exception as e:
    print(f"An error occurred: {e}")

try:
    with open("sample.txt", "r") as file:
        content1 = file.readline()
        content2=file.readline()
        content3=file.readline()
        print(f"Line 1 {content1}")
        print(f"Line 2 {content2}")
        print(f"Line 3 {content3}")
except FileNotFoundError:
    print("File not found.")