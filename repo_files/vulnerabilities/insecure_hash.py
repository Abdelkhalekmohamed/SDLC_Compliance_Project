import hashlib


def insecure_hash(input_data):
    # Use of MD5 hash (known weak algorithm)
    return hashlib.md5(input_data.encode()).hexdigest()


def another_insecure_hash(input_data):
    # Use of SHA1 hash (also considered weak)
    return hashlib.sha1(input_data.encode()).hexdigest()


def yet_another_insecure_hash(input_data):
    # Use of MD5 hash again to increase high severity issues
    return hashlib.md5(input_data.encode()).hexdigest()


# Example usage
data = "example_data"
print(insecure_hash(data))
print(another_insecure_hash(data))
print(yet_another_insecure_hash(data))
