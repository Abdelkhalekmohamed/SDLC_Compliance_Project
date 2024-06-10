import pickle

def deserialize_data(data):
    # This is a low severity, low confidence issue
    # Consider possible security implications associated with pickle module.
    if isinstance(data, bytes):
        return pickle.loads(data)  # Low confidence

untrusted_data = pickle.dumps({"key": "value"})
deserialize_data(untrusted_data)
