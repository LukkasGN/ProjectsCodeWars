"""
Write a function that, given a string of text (possibly with punctuation and line-breaks), 
returns an array of the top-3 most occurring words, in descending order of the number of occurrences.

"""

def top_3_words(text):
    
    ans = []
    texto = text.replace(" ", "").lower()
    text_arr = [texto]
    counter = 0
    max = -999999

    for word in text_arr:
        for letter in word:
            counter = word.count(letter)
            print(counter)
        
        
    #return text_arr

    
    return ans

print(top_3_words("a a a  b  c c  d d d d  e e e e e"))