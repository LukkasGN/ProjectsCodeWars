"""In this little assignment you are given a string of space separated numbers, 
and have to return the highest and lowest number."""

def high_and_low(numbers):
    
    highest_number = 0
    lowest_number = 0
    numbers_ans = 0
    num_array = []
    numbers1 = numbers.split(" ")

    for x in numbers1:
        num_array.append(int(x))

    print(numbers)

    highest_number = max(num_array)

    lowest_number = min(num_array)

    numbers_ans = str(highest_number) + " " + str(lowest_number)

    print(numbers_ans)
    

high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")
