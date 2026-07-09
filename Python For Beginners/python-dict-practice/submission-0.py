from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    i = 0
    newDict = {}

    while i < len(word):
        if word[i] in newDict:
            newDict[word[i]] = newDict[word[i]] + 1
        else:
            newDict[word[i]] = 1

        i += 1

    return newDict

# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
