import re
def extract_information(text: str):
    email = None
    phone = None
    name = None
    email_match = re.search(r"\S+@\S+", text)

    if email_match:
        email = email_match.group()
    
    phone_match = re.search(r"(\+91\s?)?\d{10}", text)
    if phone_match:
        phone = phone_match.group()

    name_match = re.search(r"Name\s*:\s*(.*)", text)

    if name_match:
        name = name_match.group(1).strip()

    if name is None:

        lines = text.splitlines()

        for line in lines:
            line = line.strip()

            if not line:
                continue

            if line.upper() == "RESUME":
                continue

            if "@" in line:
             continue

            if re.search(r"(\+91\s?)?\d{10}", line):
                continue

            if line.isupper():
                name = line.title()
                break
    
    
    return {
        "email": email,
        "phone": phone,
        "name": name
    }