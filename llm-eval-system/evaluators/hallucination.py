def detect_hallucination(response, ground_truth, category):
    if category == "speculative" and ground_truth == "unknown":
        return True
    return False
