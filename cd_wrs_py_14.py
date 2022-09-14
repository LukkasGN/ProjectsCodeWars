"""
Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

12 ==> 21
513 ==> 531
2017 ==> 2071

If the digits can't be rearranged to form a bigger number, return -1

Pick the number, tear it appart, reordenate and compare to the biggest number to define witch is the biggest
"""

def next_bigger(n):
    
    dict_numbers = {

    }
    biggest_number = "-9999999"
    str_n = [str(n).split()]

    #Code

    for numbers in range(len(str_n)):
        
        for number in numbers:
            print(number)

        # return str_n[numbers]
    
    pass

print(next_bigger(12))