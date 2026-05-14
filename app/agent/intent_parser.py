def extract_intent(messages):
    
    combined = " ".join(
        [m.content for m in messages]
    ).lower()

    role = None

    role_keywords = {
        "java": "Java Developer",
        "developer": "Software Developer",
        "engineer": "Software Engineer",
        "sales": "Sales Professional",
        "leadership": "Leadership",
        "executive": "Executive Leadership",
        "manager": "Manager"
    }

    for keyword, mapped_role in role_keywords.items():
        if keyword in combined:
            role = mapped_role
            break

    seniority = None

    if "senior" in combined:
        seniority = "Senior"

    elif "mid" in combined:
        seniority = "Mid"

    elif "junior" in combined:
        seniority = "Junior"

    elif "executive" in combined:
        seniority = "Executive"

    return {
        "role": role,
        "seniority": seniority
    }