
def is_palindrome2(candidate_string):
    return candidate_string == candidate_string[::-1]

def is_palindrome(candidate_string):
    if len(candidate_string) <= 1:
        return True
    else:
        # for i starting at 0
        for i in range(len(candidate_string)):
            # check that the ith character equals the -(i+1)th
            if candidate_string[i] != candidate_string[-(i+1)]:
                # if they're the different, it's not a palindrome
                return False

        return True

for s in ["race car", "abba", "a", "palindrome", ""]:
    print("Is", s, "a palindrome? ", is_palindrome2(s))
