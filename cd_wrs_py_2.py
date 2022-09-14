
"""Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur 
more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and 
numeric digits."""

def duplicate_count(text):
    strg = text
    answer = 0
    counter = -1
    times_per_letter = 0
    qnt_letters_rept = []
    qnt_letters_rept2 = []


    strg = strg.lower()

    while counter != len(strg):
    
        for x in strg:

            times_per_letter = strg.count(x)

            if times_per_letter > 1 :

                qnt_letters_rept.append(x)

                for e in qnt_letters_rept:
                    if e not in qnt_letters_rept2:
                        qnt_letters_rept2.append(e)

            answer = len(qnt_letters_rept2)

        counter = counter + 1

        return(answer)
        

    #print(len(strg))

duplicate_count("")