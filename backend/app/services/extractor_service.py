import re


def extract_information(text: str):

    email = None
    phone = None
    name = None

    # ----------------------------
    # Email Extraction
    # ----------------------------
    email_match = re.search(r"\S+@\S+", text)
    if email_match:
        email = email_match.group()

    # ----------------------------
    # Phone Extraction
    # ----------------------------
    phone_match = re.search(r"(\+91\s?)?\d{10}", text)
    if phone_match:
        phone = phone_match.group()

    # ----------------------------
    # Name Extraction
    # ----------------------------
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

#Day 6 Skills Extraction from Resume
    skills = []
    inside_skills = False

    lines = text.splitlines()

    for line in lines:

        line = line.strip()

        # Start finding skills
        if "technical skills" in line.lower() or line.lower() == "skills":
            inside_skills = True
            continue

        # Stop finding skills
        if inside_skills and (
            "projects" in line.lower()
            or "experience" in line.lower()
            or "education" in line.lower()
            or "certifications" in line.lower()
        ):
            break
        if inside_skills and line:
            line = line.lstrip("•").lstrip("e").strip()
            skills.append(line)

    return {
        "name": name,
        "email": email,
        "phone": phone,
        "skills": skills,
    }