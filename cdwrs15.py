"""
Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question 
is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. 

Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'
"""

def maskify(cc):
    
    if cc == "":
        return ""

    quant_numbers = len(cc)

    if quant_numbers <= 4:
        return cc

    four_last = str(cc[(quant_numbers-4)]) + str(cc[(quant_numbers-3)]) + str(cc[(quant_numbers-2)]) + str(cc[(quant_numbers-1)])
    
    num_hash = quant_numbers - 4

    ans = ""

    while num_hash != 0:
        ans = ans + "#"
        num_hash = num_hash - 1
    
    ans = ans + four_last

    return ans

print(maskify("123"))