# Imagine all are lower case letters.
def character_hashing(s):
    arr = [0] * 26
    # you can declare size of 256 
    # arr = [0] * 256
    # arr[c] += 1
    for c in s:
        arr[ord(c) - ord('a')] += 1
    return arr

print(character_hashing("aaasssbcvv"))
