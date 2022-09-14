"""Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. 
No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455."""

def sum_two_smallest_numbers(numbers):
    
    first_lowest = 9999999999999999999999999999
    second_lowest = 9999999999999999999999999999
    sum = 0
    
    for number in numbers:
        if number < first_lowest:
            first_lowest = number
    for number in numbers:
        if number < second_lowest and number != first_lowest:
            second_lowest = number
    sum = first_lowest + second_lowest
    
    return sum

print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))