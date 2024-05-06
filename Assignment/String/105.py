'''Write a  Python program to extract and display the name from a given Email address.
Sample Data:
("john@example.com") -> ("john")
("john.smith@example.com") -> ("johnsmith")
("fully-qualified-domain@example.com") -> ("fullyqualifieddomain")'''
def extract_name(email):

    parts = email.split('@')
    if len(parts) != 2:
        return "Invalid email format"

    name_part = parts[0]
    name = ''.join(char for char in name_part if char.isalnum())
    
    return name
samples = [
    "john@example.com",
    "john.smith@example.com",
    "fully-qualified-domain@example.com"
]

for email in samples:
    print(f'("{email}") -> ("{extract_name(email)}")')
