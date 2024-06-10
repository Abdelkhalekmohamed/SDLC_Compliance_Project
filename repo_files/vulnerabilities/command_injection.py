import subprocess

# Insecure
subprocess.call('ls -l', shell=True)

# Secure
subprocess.call(['ls', '-l'])
