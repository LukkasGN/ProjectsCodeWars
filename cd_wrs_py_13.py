"""Write a function dirReduc which will take an array of strings and returns an array of strings with the needless directions
 removed (W<->E or S<->N side by side).
"""

def dirReduc(arr):
    
    ansr = []
    counter = 0

    for direction in arr:
        
        while counter != len(arr):

            if direction == "NORTH" or direction == "SOUTH":
                if arr[counter + 1] == "SOUTH" or arr[counter + 1] == "NORTH":
                    pass
                else:
                    ansr.append(direction)
            counter = counter + 1

            pass

    
    return ansr

print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))