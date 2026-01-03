"""
Task 2: Sum of Integers from 1 to 50 Using a Loop

Problem Statement: Write a Python program that:
1.   Uses a for loop to iterate over numbers from 1 to 50.
2.   Calculates the sum of all integers in this range.
3.   Displays the final sum.

Expected Output:
The program should return:

"""
total=0
for i in range(1,50):
   total+=i
print(f"The sum of numbers from 1 to 50 is :",total)

#take input from user
total=0
num=int(input("Enter the range of sum :"))
for i in range(1,num):
    total+=i
print(f"The sum of numbers from 1 to {num} is :",total)