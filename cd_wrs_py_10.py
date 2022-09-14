"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number 
is negative, return 0 (for languages that do have them).

Note: If the number is a multiple of both 3 and 5, only count it once."""

def solution(number):
    
    is_multiple = []
    counter = number
    all_numbers = []
    soma = 0

    if number < 0:
        return 0

    while counter != 0:
        all_numbers.append(counter)
        counter = counter - 1

    for num in range(len(all_numbers)):
        if num % 3 == 0 or num % 5 == 0:
            is_multiple.append(num)
    
    if 0 in is_multiple:
        is_multiple.pop(0)

    for valor in is_multiple:
        soma = soma + valor

    return(soma)

print(solution(-5))