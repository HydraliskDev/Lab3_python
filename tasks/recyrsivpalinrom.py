def is_palindrome_recursive(seq):
    if len(seq) <= 1:              
        return True
    if seq[0] != seq[-1]:          
        return False
    return is_palindrome_recursive(seq[1:-1])   
print(is_palindrome_recursive("шалаш"))