"""In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or 
equal to n. For example: 5! = 5 * 4 * 3 * 2 * 1 = 120. By convention the value of 0! is 1.
Write a function to calculate factorial for a given input. If input is below 0 or above 12 throw an exception of type ValueError"""

def factorial(n):
    
    ansr = 1
    counter = n
    numbers_to_be_mult = []

    if n < 0 or n > 12:
        raise ValueError()

    if n == 0:
        ansr == 1
    
    while counter != 0:
        numbers_to_be_mult.append(counter)
        counter = counter - 1

    for valor in range(len(numbers_to_be_mult)):
        ansr = ansr * numbers_to_be_mult[valor]

    return ansr

print(factorial(13))