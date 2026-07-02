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

    # ----------------------------
    # Skills Extraction
    # ----------------------------
    skills = []
    inside_skills = False

    lines = text.splitlines()

    for line in lines:

        line = line.strip()

        if "technical skills" in line.lower() or line.lower() == "skills":
            inside_skills = True
            continue

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

    # ----------------------------
    # Education Extraction
    # ----------------------------
    education = extract_education(text)

    return {
        "name": name,
        "email": email,
        "phone": phone,
        "skills": skills,
        "education": education,
    }


def extract_education(text: str):

    education = []
    inside_education = False

    degree = None
    institution = None
    year = None

    lines = text.splitlines()

    for line in lines:

        line = line.strip()

        if not line:
            continue

        # Debug
        print("LINE:", repr(line))

        # ----------------------------
        # Start Education Section
        # ----------------------------
        if "education" in line.lower():
            inside_education = True
            print(">>> Education Section Found")
            continue

        # ----------------------------
        # Stop Education Section
        # ----------------------------
        if inside_education and (
            "other information" in line.lower()
            or "projects" in line.lower()
            or "experience" in line.lower()
            or "technical skills" in line.lower()
            or "certifications" in line.lower()
        ):
            print(">>> Education Section End")
            break

        if not inside_education:
            continue

        # ----------------------------
        # Degree Detection
        # ----------------------------
        if any(keyword in line.lower() for keyword in [
            "bachelor",
            "master",
            "b.tech",
            "m.tech",
            "bca",
            "mca",
            "b.sc",
            "m.sc",
            "be",
            "me",
            "diploma"
        ]):
            degree = line
            print("Degree:", degree)
            continue

        # ----------------------------
        # Year Detection
        # ----------------------------
        year_match = re.search(r"(19|20)\d{2}.*?(19|20)\d{2}", line)

        if year_match:

            year = year_match.group()

            # Everything before the year is institution
            if institution is None:
                institution = line.replace(year, "").strip(" ,-–")

            education.append({
                "degree": degree,
                "institution": institution,
                "year": year
            })

            degree = None
            institution = None
            year = None

            continue

        # ----------------------------
        # Institution
        # ----------------------------
        if degree and institution is None:

            institution = line
            print("Institution:", institution)

    return education