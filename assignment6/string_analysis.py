def is_vowel(char):
    return char.lower() in ['a', 'e', 'i', 'o', 'u']


def longest_continual_substring(word, check_func):
    longest_substring = ""
    current_substring = ""

    for char in word:
        if check_func(char):
            current_substring += char
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring
        else:
            current_substring = ""

    return longest_substring


def longest_continual_prefix(word, check_func):
    prefix = ""

    for char in word:
        if check_func(char):
            prefix += char
        else:
            break

    return prefix


def longest_continual_suffix(word, check_func):
    suffix = ""
    reversed_word = word[::-1]

    for char in reversed_word:
        if check_func(char):
            suffix = char + suffix
        else:
            break

    return suffix
