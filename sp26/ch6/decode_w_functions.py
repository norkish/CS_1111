def get_nonnegative_int_from_user(prompt_string):
    user_num = int(input(prompt_string))
    assert user_num == abs(user_num)
    return user_num


def decode(num_characters):
    _message = ""
    for i in range(num_characters):
        next_char_int = get_nonnegative_int_from_user("Next character's ASCII number: ")
        next_char = chr(next_char_int)
        _message = _message + next_char
    return _message


n = get_nonnegative_int_from_user("How many characters in your message? ")
message = decode(n)
print(message)
