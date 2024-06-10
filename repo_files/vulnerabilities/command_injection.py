import subprocess

def unsafe_subprocess_call(cmd):
    # High severity, high confidence
    subprocess.call(cmd, shell=True)

def safer_subprocess_call(cmd):
    # Medium severity, medium confidence
    subprocess.run(cmd, shell=False)

cmd = "echo Hello, World!"
unsafe_subprocess_call(cmd)
safer_subprocess_call(cmd)
