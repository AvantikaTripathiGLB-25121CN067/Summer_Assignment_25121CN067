class Contact:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone

class ContactManager:
    def __init__(self):
        self.contacts={}

    def add_contact(self,name,phone):
        self.contacts[name]=Contact(name,phone)
        return f"Contact {name} added!"
    
    def search_contact(self,name):
        contact=self.contacts.get(name)
        return f"{name}: {contact.phone}"if contact else "Contact not found."
    
manager=ContactManager()
manager.add_contact("Anu","9956423110")
print(manager.search_contact("Anu"))
print(manager.search_contact("Aamir"))
