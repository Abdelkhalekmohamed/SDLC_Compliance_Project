import pickle


def insecure_deserialize(data):
    # High severity, low confidence issue (insecure deserialization)
    obj = pickle.loads(data)  # Deserializing potentially unsafe data
    print(f"Deserialized object: {obj}")


if __name__ == "__main__":
    serialized_data = pickle.dumps({"key": "value"})
    insecure_deserialize(serialized_data)

import subprocess
subprocess.Popen(['ls', '-l'])
import pickle
pickle.loads(b'')
import subprocess
subprocess.Popen(['ls', '-l'])
