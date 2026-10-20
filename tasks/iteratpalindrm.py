def is_palindrome_iterative(seq):
    left = 0
    right = len(seq) - 1
    while left < right:
        if seq[left] != seq[right]:
            return False
        left += 1
        right -= 1
    return True
print(is_palindrome_iterative("шалаш"))