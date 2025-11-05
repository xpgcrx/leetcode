def next_lexicographical_sequence(s: str) -> str:
    letters = list(s)
    pivot = len(letters) - 2
    while 0 <= pivot and letters[pivot] >= letters[pivot+1]:
        pivot -= 1
    if pivot == -1:
        return "".join(reversed(letters))
    swap_index = len(letters) - 1
    while letters[swap_index] <  letters[pivot]:
        swap_index -= 1
    letters[pivot], letters[swap_index] = letters[swap_index], letters[pivot]
    letters[pivot+1:] = reversed(letters[pivot+1:])
    return "".join(letters)
    
