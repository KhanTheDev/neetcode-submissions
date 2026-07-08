from typing import List, Dict

def create_dict(name: str, age: int) -> Dict[str, int]:
    new_dic = {name:age}
    return new_dic

def list_to_dict(words: List[str]) -> Dict[str, int]:
    new_dict = {}
    count = 0
    for element in words:
        new_dict[element] = count
        count+=1

    return new_dict




# don't modify code below this line
print(create_dict("Alice", 25))
print(create_dict("Jane", 35))
print(create_dict("Joe", 45))

print(list_to_dict(["Alice", "Jane", "Joe"]))
print(list_to_dict(["Apple", "Banana", "Watermelon", "Pineapple"]))
