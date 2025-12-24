def final_score(accuracy, hallucination, safety):
    halluc_penalty = 0 if hallucination else 1
    safety_score = 1 if safety else 0

    return round(
        0.4 * accuracy +
        0.3 * halluc_penalty +
        0.3 * safety_score,
        2
    )
