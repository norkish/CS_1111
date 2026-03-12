def encrypt_via_caesar_cypher(_message, _offset):
    _encrypted_message = ""

    for c in _message:
        ascii_val = ord(c)
        new_ascii_val = ascii_val + _offset
        if new_ascii_val > ord('z'):
            _encrypted_char = chr(new_ascii_val - 26)
        else:
            _encrypted_char = chr(new_ascii_val)

        _encrypted_message = _encrypted_message + _encrypted_char

    return _encrypted_message


def decrypt_via_caesar_cypher(_message, _offset):
    _decrypted_message = ""

    for c in _message:
        ascii_val = ord(c)
        new_ascii_val = ascii_val - _offset
        if new_ascii_val < ord('a'):
            _decrypted_char = chr(new_ascii_val + 26)
        else:
            _decrypted_char = chr(new_ascii_val)

        _decrypted_message = _decrypted_message + _decrypted_char

    return _decrypted_message


#given a string and an integer
message = input("Input your message, please: ")
offset = int(input("Input the key, please: "))

encrypted_message = encrypt_via_caesar_cypher(message, offset)
print(encrypted_message)
decrypted_message = decrypt_via_caesar_cypher(encrypted_message, offset)
print(decrypted_message)
