def next_lexicographical_sequence(s: str) -> str:
    letters = list(s)
    pivot = len(letters) - 2
    while 0 <= pivot and letters[pivot] >= letters[pivot + 1]:
        pivot -= 1

    if pivot < 0:
        return "".join(reversed(letters))

    rightmost_successor = len(letters) - 1
    while letters[pivot] >= letters[rightmost_successor]:
        rightmost_successor -= 1

    letters[pivot], letters[rightmost_successor] = (
        letters[rightmost_successor],
        letters[pivot],
    )

    letters[pivot + 1 :] = reversed(letters[pivot + 1 :])

    return "".join(letters)
