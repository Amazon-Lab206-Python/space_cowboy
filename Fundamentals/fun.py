# Odd/Even:
# Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.

def odd_even(x):
    for x in range(1,2001):
        if (x % 2 == 0):
            print "This is an even number."
        else:
            print "This is an odd number."
odd_even()



# Multiply:
# Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.

def multiply(arr, num):
    for x in range(0, len(arr)):
        arr[x] *= num
    return arr

numbers_array = [3, 6, 8, 10, 67]

print multiply(numbers_array, 5)