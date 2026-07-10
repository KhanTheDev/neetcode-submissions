def add_two_numbers() -> int:
    user_input = input()
    pieces = user_input.split(",")
    newList = []
    for piece in pieces:
        newList.append(int(piece))

    sum = newList[0] + newList[1]

    return sum



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
