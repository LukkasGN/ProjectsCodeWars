"""Given an array of integers, find the one that appears an odd number of times.
There will always be only one integer that appears an odd number of times."""

def find_it(seq):
    
    ansr = 0
    times_appeared = 0

    for x in seq:
        times_appeared = seq.count(x)
        if times_appeared % 2 != 0:
            ansr = x
        else:
            pass
    
    return ansr

print(find_it([0,1,0,1,0]))