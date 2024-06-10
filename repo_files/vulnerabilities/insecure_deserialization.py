import pickle

def insecure_deserialize(data):
    # High severity, low confidence issue (insecure deserialization)
    obj = pickle.loads(data)  # Deserializing potentially unsafe data
    print(f"Deserialized object: {obj}")

if __name__ == "__main__":
    # This is an example of potentially unsafe serialized data
    serialized_data = pickle.dumps({"key": "value"})
    insecure_deserialize(serialized_data)
