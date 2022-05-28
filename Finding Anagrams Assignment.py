# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
   
    str1 = word
    str2 = anagram
    if len(str1) == len(str2):
        sort_str1 = sorted(word)
        sort_str2 = sorted(anagram)

        if sort_str1 == sort_str2: 
            
            return True
        else:
            return False
print(find_anagram('pots','spot'))
    

