import spacy
import re

nlp = spacy.load("en_core_web_sm")

def extract_resume_data(text: str):
    doc = nlp(text)

    # Extract name (first PERSON entity)
    name = next((ent.text for ent in doc.ents if ent.label_ == "PERSON"), None)

    # Extract email
    email = next((t for t in doc if t.like_email), None)

    # Extract phone using regex
    phone = next((t for t in doc if re.match(r'\+?\d[\d\s\-\(\)]{9,}', t.text)), None)

    # Extract possible skills (simplified example: top N nouns)
    skills = [token.text for token in doc if token.pos_ == "NOUN" and token.is_alpha]
    skills = list(set(skills))[:10]

    # Education sentences
    education_keywords = ['bachelor', 'master', 'university', 'degree', 'college']
    education = [sent.text for sent in doc.sents if any(word in sent.text.lower() for word in education_keywords)]

    # Experience sentences
    experience_keywords = ['experience', 'worked', 'intern', 'developer']
    experience = [sent.text for sent in doc.sents if any(word in sent.text.lower() for word in experience_keywords)]

    return {
        "name": name,
        "email": str(email),
        "phone": str(phone),
        "skills": skills,
        "education": education,
        "experience": experience
    }
