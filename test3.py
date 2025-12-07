import subprocess
subprocess.call(["amixer", "set", "Master", "50%"], stdout=subprocess.DEVNULL)
