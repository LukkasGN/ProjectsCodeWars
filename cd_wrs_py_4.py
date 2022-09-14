"""You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, 
return the middle character. If the word's length is even, return the middle 2 characters."""

def get_middle(word):
    
    len_word = len(word)
    letter = ""
    position = 0
    position2 = 0

    if len_word % 2 == 0:
        position = (len(word)/2) - 1
        position2 = (len(word)/2)
        letter = word[int(position2 - 1)], word[int(position2)]
        ans = letter[0] + letter[1]
        return(ans)
    else:
        position = (len(word)+1)/2
        letter = word[int(position - 1)]
        return(letter)

get_middle("test")