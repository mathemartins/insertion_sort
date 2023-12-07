# main.py
from file_handler import read_file, extract_words
from string_analysis import (
    is_vowel,
    longest_continual_substring,
    longest_continual_prefix,
    longest_continual_suffix,
)


def main():
    file_name = 'lore_ipsum.txt'

    # Read file and extract words
    text = read_file(file_name)
    words = extract_words(text)

    longest_vowel_substring = ""
    longest_consonant_substring = ""
    longest_vowel_prefix = ""
    longest_consonant_prefix = ""
    longest_vowel_suffix = ""
    longest_consonant_suffix = ""

    for word in words:
        # Check for longest continual substrings of vowels and consonants
        vowel_substring = longest_continual_substring(word, is_vowel)
        consonant_substring = longest_continual_substring(word, lambda x: not is_vowel(x))

        if len(vowel_substring) > len(longest_vowel_substring):
            longest_vowel_substring = vowel_substring
        if len(consonant_substring) > len(longest_consonant_substring):
            longest_consonant_substring = consonant_substring

        # Check for longest continual prefixes of vowels and consonants
        vowel_prefix = longest_continual_prefix(word, is_vowel)
        consonant_prefix = longest_continual_prefix(word, lambda x: not is_vowel(x))

        if len(vowel_prefix) > len(longest_vowel_prefix):
            longest_vowel_prefix = vowel_prefix
        if len(consonant_prefix) > len(longest_consonant_prefix):
            longest_consonant_prefix = consonant_prefix

        # Check for longest continual suffixes of vowels and consonants
        vowel_suffix = longest_continual_suffix(word, is_vowel)
        consonant_suffix = longest_continual_suffix(word, lambda x: not is_vowel(x))

        if len(vowel_suffix) > len(longest_vowel_suffix):
            longest_vowel_suffix = vowel_suffix
        if len(consonant_suffix) > len(longest_consonant_suffix):
            longest_consonant_suffix = consonant_suffix

    # Print or store the words with the longest continual substrings, prefixes, and suffixes
    print("Longest Continual Substring of Vowels:", longest_vowel_substring)
    print("Longest Continual Substring of Consonants:", longest_consonant_substring)
    print("Longest Continual Prefix of Vowels:", longest_vowel_prefix)
    print("Longest Continual Prefix of Consonants:", longest_consonant_prefix)
    print("Longest Continual Suffix of Vowels:", longest_vowel_suffix)
    print("Longest Continual Suffix of Consonants:", longest_consonant_suffix)


if __name__ == "__main__":
    main()
