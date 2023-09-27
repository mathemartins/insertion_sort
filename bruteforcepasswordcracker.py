import itertools


def brute_force_password_cracker(target_password, character_set, max_length):
    for length in range(1, max_length + 1):
        for combination in itertools.product(character_set, repeat=length):
            candidate_password = ''.join(combination)
            if candidate_password == target_password:
                return candidate_password
    return None


if __name__ == '__main__':
    target_password = "secret"
    character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    max_length = 6

    cracked_password = brute_force_password_cracker(target_password, character_set, max_length)

    if cracked_password:
        print(f"Password cracked: {cracked_password}")
    else:
        print("Password not found.")

# The complexity of this algorithm is exponential (O(c^n)), where "c" is the size of the character set, and "n" is
# the maximum password length
