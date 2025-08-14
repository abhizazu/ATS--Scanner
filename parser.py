

import re

def calculate_match_score(resume_text, job_description):
    # Convert text to lowercase and split words
    resume_words = set(re.findall(r'\b\w+\b', resume_text.lower()))
    jd_words = set(re.findall(r'\b\w+\b', job_description.lower()))

    # Consider words with at least 3 characters to avoid common words
    jd_important = {w for w in jd_words if len(w) > 2}

    # Match with resume
    matching = jd_important & resume_words
    missing = jd_important - resume_words

    # Score calculation
    score = 0
    if jd_important:
        score = round(len(matching) / len(jd_important) * 100)

    return score, list(missing)

