"""Consider a sequence u where u is defined as follows:

The number u(0) = 1 is the first one in u.
For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
There are no other numbers in u.
Ex: u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]

1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...

Task:
Given parameter n the function dbl_linear (or dblLinear...) returns the element u(n) of the ordered (with <) sequence u (so, there are no duplicates).

Example:
dbl_linear(10) should return 22"""

def dbl_linear(n):
	
    u = []
    x = 0
    y = 0
    z = 0
    counter = 1
    x_position = []

    #code

    x = 1
    u.append(x)
    x_position.append(x)

    while counter != 4800:
        for num in x_position:
            x = num
            
            y = 2 * x + 1
            z = 3 * x + 1

            if y in u:
                pass
            else:
                u.append(y)

            if z in u:
                pass
            else:
                u.append(z)

            if y in x_position:
                pass
            else:
                x_position.append(y)

            if z in x_position:
                pass
            else:
                x_position.append(z)


            counter = counter + 1
            
            if counter == 4800 :
                break

    u.sort()
    return u[n]

print(dbl_linear(30000))

"""

if y in u:
    pass
else:
    u.append(y)

if z in u:
    pass
else:
    u.append(z)

if y in x_position:
    pass
else:
    x_position.append(y)

if z in x_position:
    pass
else:
    x_position.append(z)


"""

# ------------------------------------------------------------------------------------------------------ #

"""
            u.append(y)
            u.append(z)
            x_position.append(y)
            x_position.append(z)

"""