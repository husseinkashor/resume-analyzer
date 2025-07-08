import spacy

nlp = spacy.load("en_core_web_sm")

REQUIRED_SKILLS = {"python", "machine learning", "flask", "nlp", "sql", "data analysis"}

def analyze_resume(text):
    doc = nlp(text.lower())
    tokens = set(token.text for token in doc if not token.is_stop and not token.is_punct)
    matched = REQUIRED_SKILLS.intersection(tokens)
    score = (len(matched) / len(REQUIRED_SKILLS)) * 100
    return {
        "matched_skills": list(matched),
        "missing_skills": list(REQUIRED_SKILLS - matched),
        "score": round(score, 2)
    }
