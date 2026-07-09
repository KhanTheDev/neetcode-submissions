from typing import List

def read_integers() -> List[int]:
    user_input = str(input())
    pieces = user_input.split(",")
    newList = []
    for piece in pieces:
        newList.append(int(piece))

    return newList

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
