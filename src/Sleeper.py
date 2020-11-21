import os
import random
import subprocess
import time

def sleeper(SHUTDOWN_TIME_MINUTES: int = 45):
  print('start sleeper')
  total_time_seconds: int = SHUTDOWN_TIME_MINUTES * 60
  scriptName: str = f"sleeperScript-{random.random()}.sh"

  with open(scriptName, "w+") as sleepyScript:
    sleepyScript.write(f"sleep {total_time_seconds}\n")
    sleepyScript.write('shutdown')
    sleepyScript.flush()
    sleepyScript.close()

  # Give time for OS to lay down file above
  # time.sleep(1)
  os.chmod(scriptName, 0o777)
  subprocess.Popen(['bash', '-c', f"./{scriptName}"])
  os.system(f"rm {scriptName}")
  exit(0)
