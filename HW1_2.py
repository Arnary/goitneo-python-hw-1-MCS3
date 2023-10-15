def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    if contacts == {}:
        contacts[name] = phone
        return "Contact added."
    else:
        if name in contacts.keys():
            return "Contact with this name already exists. Use the 'change' command if you want to update a contact."
        else:
            contacts[name] = phone
            return "Contact added."


def change_contact(args, contacts):
    name, phone = args
    if name in contacts.keys():
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."


def show_phone(args, contacts):
    name, = args
    if name in contacts.keys():
        return contacts[name]
    else:
        return "Contact not found."


def show_all(contacts):
    contact_book = list()
    if contacts == {}:
        return "You don't have any contacts yet."
    for name, phone in contacts.items():
        contact_book.append('|{:>15} : {:<17}|'.format(name, phone))
    return "\n".join(contact_book)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()