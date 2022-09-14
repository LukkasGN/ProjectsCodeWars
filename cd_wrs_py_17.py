"""

A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence 
"The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

"""

def is_pangram(s):

    count = 0
    
    all_letters = ["p", "o", "i", "u", "y", "t", "r", "e", "w", "q", "l", "k", "j", "h", "g", "f", "d", "s", "a", "m", "n", "b", "v", "c", "x", "z",] 
    
    s = s.lower().replace(" ", "")

    while True:
        for letter in s:
           
            if letter in all_letters:
                count = count + 1
                all_letters.remove(letter)    
            
        if count == 26:
            return True
        if count != 26:
            return False

print(is_pangram("The quick brown fox jumps over the lazy dog"))