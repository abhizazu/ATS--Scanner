import re

def calculate_match_score(resume_text, job_description):
    resume_words = set(re.findall(r'\b\w+\b', resume_text.lower()))
    jd_words = set(re.findall(r'\b\w+\b', job_description.lower()))
    jd_important = {w for w in jd_words if len(w) > 2}
    matching = jd_important & resume_words
    missing = jd_important - resume_words
    score = round(len(matching) / len(jd_important) * 100) if jd_important else 0
    return score, list(missing)
