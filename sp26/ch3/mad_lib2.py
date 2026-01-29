name = input("Give me the name of a famous person: ")
noun1 = input("Give me a noun: ")
noun2 = input("Give me a plural noun: ")
noun3 = input("Give me a plural noun: ")
noun4 = input("Give me a plural noun: ")
noun5 = input("Give me a plural food: ")
clothing = input("Give me a plural article of clothing: ")
verb = input("Give me a verb in 3rd person singular form: ")
verb2 = input("Give me a verb in 3rd person singular form: ")
adjective = input("Give me an adjective: ")
number = int(input("Give me a number: "))
decimal = float(input("Give me a decimal value: "))
print(name + " wanders into the " + noun1 + " of " + str(number) + "\n" +
    noun2 + " while they’re away. " + name + " eats their "+ noun5 + ",\n"
    "sits in their " + noun4 + ", wears all " + str(number*2) + " of their " + clothing + ".\n"
    "---can you believe it? " + str(number*2) + "!---"
    "and " + verb + " in their " + noun3 + ", breaking\n"
    "and sampling exactly " + str(decimal) + " everything (that's " +
    str(decimal * 2.0 * number) + " " + clothing + ")  until \n" + name + " finds what’s 'just right.'\n"
    "When the " + noun2 + " return, they discover " +
    name + " " + adjective + ". \n" + name +
    " wakes up, " + verb2 + ", and runs away.")


# print("Is there a difference","here")
# print("Is there a difference" + " here")
