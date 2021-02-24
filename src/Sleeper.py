import os
import random
import subprocess
import time

from src.Kasa import KasaAPI

def sleeper(SHUTDOWN_TIME_MINUTES: int = 45, kasaHost: str = ''):
  print('start sleeper')
  total_time_seconds: int = SHUTDOWN_TIME_MINUTES * 60

  if KasaAPI.KASA_ENABLED:
    scriptName: str = f"sleeperScript-{random.random()}.sh"

    with open(scriptName, "w+") as sleepyScript:
     sleepyScript.write(f"sleep {total_time_seconds}\n")
     sleepyScript.write(KasaAPI.kill_kasa_outlet_cmd(kasaHost))
     sleepyScript.flush()
     sleepyScript.close()

    # Give time for OS to lay down file above
    time.sleep(1)
    os.chmod(scriptName, 0o777)
    subprocess.Popen(['bash', '-c', f"./{scriptName}"])
    os.system(f"rm {scriptName}")
  else:
    os.system(f"sudo shutdown +{SHUTDOWN_TIME_MINUTES}")
  exit(0)
