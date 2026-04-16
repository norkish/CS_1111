filename = "contacts.txt"

#create dict
contacts = {
    "Alice":"555-1111",
    "Bob":"555-2222",
    "Charlie":"555-3333"
}

outfile = open(filename,"w")

# write dict to file
for (key, value) in contacts.items():
    outfile.write(key + "," + value + "\n")

outfile.close()

# clear dict
contacts.clear()

infile = open(filename, "r")

#read dict back in
for line in infile:
    pair = line.strip().split(",")
    contacts[pair[0]] = pair[1]

infile.close()

print(contacts)
