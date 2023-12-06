import time
import subprocess
import os
import sys

day = sys.argv[0]
part = sys.argv[1]

# Get the current modification time of the directory
current_mod_time = os.stat(part).st_mtime

while True:
    # If the modification time has changed, run the command
    if os.stat(part).st_mtime != current_mod_time:
        current_mod_time = os.stat(part).st_mtime
        subprocess.run('pytest', shell=True)

    # Wait for a while before checking again
    time.sleep(1)
