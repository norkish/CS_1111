# determine if a string is a valid DNA string
# given a string, check that it only has A, C, T, or G characters
ACCEPTABLE = "ACTG"

def validate(_candidate):
    valid_dna = ""

    # for each character
    for i in range(len(_candidate)):
        if _candidate[i] in ACCEPTABLE:
            # check that it's either A,C,T, or G
            valid_dna = valid_dna + _candidate[i]
    return valid_dna == candidate


def validate2(_candidate):
    # for each character
    for i in range(len(_candidate)):
        if _candidate[i] not in ACCEPTABLE:
            # check that it's either A,C,T, or G
            return False
    return True


def validate3(_candidate):
    valid_dna_count = 0

    # for each character
    for i in range(len(_candidate)):
        if _candidate[i] in ACCEPTABLE:
            # check that it's either A,C,T, or G
            valid_dna_count = valid_dna_count + 1
    return valid_dna_count == len(candidate)


def validate4(_candidate):
    invalid_dna_count = 0

    # for each character
    for i in range(len(_candidate)):
        if _candidate[i] not in ACCEPTABLE:
            # check that it's either A,C,T, or G
            invalid_dna_count = invalid_dna_count + 1
    return invalid_dna_count == 0

while True:
    candidate = input("Input candidate DNA sequence: ")

    # if we get to the end, and haven't rejected, we're golden
    if validate2(candidate):
        print("Candidate is acceptable")
    else:
        print("Candidate not acceptable")
      
