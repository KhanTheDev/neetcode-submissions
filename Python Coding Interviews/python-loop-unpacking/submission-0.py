from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    highestScore = 0
    name = ""
    for score in scores:
        x,y = score[0], score[1]
        if y > highestScore:
            highestScore = y
            name = x
    return name

# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
