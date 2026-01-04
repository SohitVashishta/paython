"""
1.  Asks the user for a number as input.
2.  Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.  Displays the calculated results.

"""
import math

num = float(input("Enter a number: "))

sqrt_result = math.sqrt(num)
log_result = math.log(num)
sin_result = math.sin(num)

print("Square root of", num, "is", sqrt_result)
print("Logarithm of", num, "is", log_result)
print("Sine of", num, "is", sin_result)



