# Validates if the hash starts with the zeros required for the difficulty

def validate_hash(hash_string, difficulty):
    return hash_string.startswith("0" * difficulty)
