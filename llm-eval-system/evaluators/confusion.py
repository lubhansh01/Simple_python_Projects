def detect_confusion(prompt, response):
    if "book" in prompt.lower() and "capital" in response.lower():
        return True
    return False
