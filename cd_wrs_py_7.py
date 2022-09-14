"""The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false."""

def generate_hashtag(s):
    
    ans = ""
    wrd_counter = 0

    ans = "#" + s.title().strip().replace(" ", "")

    for x in ans:
        wrd_counter = wrd_counter + 1
    
    if wrd_counter > 140:
        return False
    if ans == "#":
        return False
    else:
        return ans

print(generate_hashtag("Codewars Is Nice"))