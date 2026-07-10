def add_two_numbers() -> int:
    user_input = input()
    pieces = user_input.split(",")
    

    sum = (int(pieces[0]) + int(pieces[1])) 

    return sum



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
