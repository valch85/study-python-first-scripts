# Write a program that prints the numbers from 1 to n. 
# But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. 
# For numbers which are multiples of both three and five print “FizzBuzz”.

def fizzBuzz(n):
    # Write your code here
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print ("FizzBuzz")
        elif i% 3 == 0:
            print ("Fizz")
        elif i % 5 == 0:
            print ("Buzz")
        else:
            print(i)

fizzBuzz(15)

""" Expected Output:
    1
    2
    Fizz
    4
    Buzz
    Fizz
    7
    8
    Fizz
    Buzz
    11
    Fizz
    13
    14
    FizzBuzz
"""