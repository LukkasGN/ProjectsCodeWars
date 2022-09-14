
num = 493193
soma = 0
i = 0
list_numbers = [int(a) for a in str(num)]

while len(list_numbers) > 1:
    for x in range(len(list_numbers)):
        soma = soma + list_numbers[x]
    list_numbers = [int(x) for x in str(soma)]
    soma = 0

    list_numbers_int = list_numbers[0]

    print(list_numbers_int)


#sum = [list_numbers[0] + list_numbers[1]]

#print(sum)
#print(soma)
#print(len(list_numbers))