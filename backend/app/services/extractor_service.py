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
    # Skills Extraction
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
    experience = extract_experience(text)
    projects = extract_projects(text)
    certifications = extract_certifications(text)
    languages = extract_languages(text)

    return {
        "name": name,
        "email": email,
        "phone": phone,
        "skills": skills,
        "education": education,
        "experience": experience,
        "projects": projects,
        "certifications": certifications,
        "languages": languages
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
# Start Education Section
        if "education" in line.lower():
            inside_education = True
            continue
 # Stop Education Section
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
        # Degree Detection
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
        # Year Detection
        year_match = re.search(r"(19|20)\d{2}.*?(19|20)\d{2}", line)
        if year_match:
            year = year_match.group()
            # before the year is institution
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
        # Institution Detection
        if degree and institution is None:
            institution = line
            print("Institution:", institution)
    return education


def extract_experience(text: str):
    experience = []
    inside_experience = False
    designation = None
    company = None
    duration = None
    lines = text.splitlines()
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # Start Experience Section
        if "experience" in line.lower():
            inside_experience = True
            continue
        # End Experience Section
        if inside_experience and (
            "education" in line.lower()
            or "projects" in line.lower()
            or "technical skills" in line.lower()
            or "certifications" in line.lower()
            or "other information" in line.lower()
        ):
            break
        if not inside_experience:
            continue
        # Designation Detection
        if any(keyword in line.lower() for keyword in [
            "developer",
            "engineer",
            "intern",
            "manager",
            "analyst",
            "consultant",
            "architect",
            "lead",
            "tester"
        ]):
            designation = line
            continue
        # Company + Duration Detection
        month_match = re.search(
            r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{4}",
            line,
            re.IGNORECASE
        )
        if month_match:
            index = month_match.start()
            company = line[:index].strip(" ,-–")
            duration = line[index:].strip()
            experience.append({
                "designation": designation,
                "company": company,
                "duration": duration
            })
            designation = None
            company = None
            duration = None
            continue
        # Company Detection (when OCR keeps it on a separate line)
        if designation and company is None:
            company = line

    return experience


def extract_projects(text: str):
    projects = []
    inside_projects = False
    project_name = None
    description = []
    lines = text.splitlines()
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # Start Projects Section
        if line.lower() == "projects":
            inside_projects = True
            continue
        if not inside_projects:
            continue
        # End Projects Section
        if line.lower() in [
            "experience",
            "education",
            "technical skills",
            "skills",
            "certifications",
            "other information"
        ]:

            if project_name:
                projects.append({
                    "project_name": project_name,
                    "description": " ".join(description).strip()
                })

            break
        # Project Name
        if project_name is None:

            # Remove numbering like "1."
            line = re.sub(r"^\d+\.\s*", "", line)

            project_name = line
            description = []
            continue
        # Description
        description.append(line)
    # Save last project
    if inside_projects and project_name:

        # Avoid duplicate append
        if not projects or projects[-1]["project_name"] != project_name:

            projects.append({
                "project_name": project_name,
                "description": " ".join(description).strip()
            })
    return projects

def extract_certifications(text: str):

    certifications = []
    inside_certifications = False

    certification_name = None
    issuer = None
    year = None

    for line in text.splitlines():

        line = line.strip()

        if line.lower() == "certifications":
            inside_certifications = True
            continue

        if inside_certifications and (
            line.lower() == "experience"
            or line.lower() == "education"
            or line.lower() == "projects"
            or line.lower() == "technical skills"
            or line.lower() == "skills"
            or line.lower() == "other information"
        ):
            break

        if not inside_certifications:
            continue

        if not line:
            continue

        # Certificate Name
        if certification_name is None:
            certification_name = line
            continue

        # Issuer | Year
        if "|" in line:

            parts = line.split("|")

            issuer = parts[0].strip()

            if len(parts) > 1:
                year = parts[1].strip()
            else:
                year = ""

            certifications.append({
                "certification_name": certification_name,
                "issuer": issuer,
                "year": year
            })

            certification_name = None
            issuer = None
            year = None

    return certifications

def extract_languages(text: str):

    languages = []
    inside_languages = False

    lines = text.splitlines()

    for line in lines:

        line = line.strip()

        if not line:
            continue

        # ----------------------------
        # Format 1
        # LANGUAGES
        # ----------------------------
        if line.lower() == "languages":
            inside_languages = True
            continue

        # ----------------------------
        # Format 2
        # e Languages: English, Malayalam
        # ----------------------------
        if "languages:" in line.lower() and "programming" not in line.lower():

            parts = line.split(":", 1)[1]

            lang_list = parts.split(",")

            for lang in lang_list:

                lang = lang.strip()

                if lang:
                    languages.append({
                        "language": lang
                    })

            continue

        # ----------------------------
        # End Section
        # ----------------------------
        if inside_languages and (
            line.lower() == "projects"
            or line.lower() == "experience"
            or line.lower() == "education"
            or line.lower() == "technical skills"
            or line.lower() == "certifications"
            or line.lower() == "other information"
        ):
            break

        # ----------------------------
        # Individual Languages
        # ----------------------------
        if inside_languages:

            line = line.lstrip("•").lstrip("e").strip()

            if line:
                languages.append({
                    "language": line
                })

    return languages