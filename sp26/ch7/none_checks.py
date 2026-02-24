# drivers_license.py—Write a program that creates variables
# for 1) your name, 2) your state and 3) your driver’s
# license number (if you don’t have one, put None).
name = "Paul Bodily"
state = "Idaho"
license_no = None # "AD123461"

# Then print each variable, checking first to see if it is None.
if name != None:
    print("Name:", name)

if state != None:
    print("State:", state)

if license_no != None:
    print("License #:", license_no)
