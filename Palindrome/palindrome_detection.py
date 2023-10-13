def is_palindrome(word):
    stack = [char for char in word]
    reversed_word = ''
    while stack:
        reversed_word += stack.pop()
    return word == reversed_word


def find_palindromes_in_file(file_path):
    with open(file_path, 'r') as file:
        words = file.read().split()
        return [word for word in words if is_palindrome(word)]


palindrome_file_path = 'palindrome.txt'
palindromes = find_palindromes_in_file(palindrome_file_path)
print("Palindromes in the file:", palindromes)
