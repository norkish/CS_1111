NUM_INQUIRIES = 5

# Pretend that everyone has single-digit bank account numbers
# Write a program that has a list of bank balances (for security make sure some bank account numbers are invalid)
balances = [None, 55.24, None, None, None, 351.90, None, 1900.00, None, 0.00]

# Let multiple users query their bank account balances
for i in range(NUM_INQUIRIES):
    # Prompt the user for a bank account number
    acct_no = int(input("Input a bank account number (single digit): "))

    # Check if the number is valid (it isn’t None)—print an error and exit() if it is invalid
    # Note that order of boolean expressions here matters to avoid indexerror
    assert acct_no >= 0 and acct_no < len(balances) and balances[acct_no] is not None, "Invalid account number"

    # Otherwise print the account number and account balance
    print("Acct #",acct_no,": $", balances[acct_no])

    # prompt the user for a new balance for that account
    new_balance = float(input("Enter your desired balance: $"))
    balances[acct_no] = new_balance
