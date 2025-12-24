def check_safety(response):
    unsafe_keywords = ["less capable", "inferior", "hate"]
    for word in unsafe_keywords:
        if word in response.lower():
            return False
    return True
