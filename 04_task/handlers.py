from functools import wraps

def input_error(func):
    
    @wraps(func) # preserve function's metadate
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, IndexError, KeyError):
            return "Enter the argument for the command"

    return inner


@input_error
def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    """ Add new contact to the contact list """
    name, phone = args
    contacts[name] = phone

    return "Contact added."

@input_error
def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    """ Change the phone of specified name, it works only if name has already existed """
    name, phone = args

    if name not in contacts:
        return f"Contact {name} doesnt exist."

    contacts[name] = phone

    return "Contact changed."

@input_error
def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    """ Returns phone number for specified name """
    name = args[0]

    if name not in contacts:
        return f"Contact {name} doesnt exist."

    return f"Phone number for {name}: {contacts.get(name)}"

@input_error
def show_all_phone(contacts: dict[str, str]) -> str:
    """ List all contacts """
    formated_contacts = [f"Phone number for {name}: {contacts.get(name)}" for name in contacts]

    return "\n".join(formated_contacts)
