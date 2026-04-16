import json

def save_contacts_json(contacts, filename):
    file = open(filename, "w")
    json.dump(contacts, file)
    file.close()


def load_contacts_json(filename):
    file = open(filename, "r")
    data = json.load(file)
    file.close()
    return data


contacts = {"Alice": "555-1111", "Bob": "555-2222"}

save_contacts_json(contacts, "contacts.json")
contacts = load_contacts_json("contacts.json")

print(contacts)
