"""Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements."""

def move_zeros(lst):
    
    lst_final = []
    total_zeros = 0

    for x in lst:
        if x != 0:
            lst_final.append(x)
        else:
            total_zeros = total_zeros + 1
    
    for x in range(total_zeros):
        lst_final.append(0)
    
    return lst_final

print(move_zeros([1, 0, 1, 2, 0, 1, 3]))