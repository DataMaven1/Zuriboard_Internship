# check if a word is an anagram
# Example
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True

def find_anagrams(string1, string2):

    if (sorted(string1) == sorted(string2)):
        return (True)
    else:
        return (False)

print(find_anagrams("rescue", "secure"))

