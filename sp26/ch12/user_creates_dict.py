user_data = {}

for key in ["first name", "last name", "address", "email"]:
    user_response = input(key.capitalize() + ": ")
    user_data[key] = user_response

print(user_data)
