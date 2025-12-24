def accuracy_score(response, ground_truth):
    if ground_truth in ["unknown", "none"]:
        return 0.5
    return 1.0 if ground_truth.lower() in response.lower() else 0.0
