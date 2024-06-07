import pickle

def deserialize_data(data):
    return pickle.loads(data)

user_data = b'\x80\x03X\x04\x00\x00\x00testq\x00.'
print(deserialize_data(user_data))
