function analyze() {
    const resume = document.getElementById("resume").value.toLowerCase();
    const jd = document.getElementById("jd").value.toLowerCase();

    if (!resume || !jd) {
        alert("Please enter both resume and job description!");
        return;
    }

    // Extract words from JD (roles, skills)
    const jdWords = jd.match(/\b[a-z]{3,}\b/g) || [];

    // Count matches
    let matchCount = 0;
    jdWords.forEach(word => {
        if (resume.includes(word)) matchCount++;
    });

    const score = jdWords.length ? Math.round((matchCount / jdWords.length) * 100) : 0;

    // Find missing keywords
    const missing = jdWords.filter(word => !resume.includes(word));

    // Display results
    const resultsDiv = document.getElementById("results");
    const scoreP = document.getElementById("score");
    const missingP = document.getElementById("missing");

    resultsDiv.style.display = "block";
    scoreP.innerHTML = `Score: ${score}%`;

    if (missing.length) {
        missingP.innerHTML = `Missing Keywords: ${missing.join(", ")}`;
    } else {
        missingP.innerHTML = "Excellent! No missing keywords found.";
    }
}

