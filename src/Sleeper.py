import os
import random
from subprocess import  Popen,CREATE_NEW_CONSOLE
import time
import glob

from src.Kasa import KasaAPI
from src.Util import is_windows,LOCATION_FORMATTED
from src.LogFactory import LogFactory
from src.FileIO import FileIO

def cleanOldScripts():
  scripts=glob.glob("sleeperScript-*.sh")
  LogFactory.MAIN_LOG.info(f"cleaning up old scripts: {scripts}")
  for script in scripts:
    LogFactory.MAIN_LOG.info(f"removing: {script}")
    os.remove(script)

def sleeper(SHUTDOWN_TIME_MINUTES: int = 45, kasaHost: str = ''):
  LogFactory.MAIN_LOG.info('start sleeper')
  total_time_seconds: int = SHUTDOWN_TIME_MINUTES * 60

  if KasaAPI.KASA_ENABLED:
    cleanOldScripts()
    scriptName: str = f"sleeperScript-{random.random()}.sh"
    scriptContent: str = ""
    with open(scriptName, "w+") as sleepyScript:
     sleepyScript.write(f"echo \"sleeping for {SHUTDOWN_TIME_MINUTES} minute(s)\" >> {LOCATION_FORMATTED}{os.sep}{os.sep}sleepy.log\n")
     sleepyScript.write(f"sleep {total_time_seconds}\n")
     sleepyScript.write(f"echo \"shuting down...\" >> {LOCATION_FORMATTED}{os.sep}{os.sep}sleepy.log\n")
     sleepyScript.write(KasaAPI.kill_kasa_outlet_cmd(kasaHost))
     sleepyScript.flush()
     sleepyScript.close()

    scriptContent=FileIO.read_file_content(scriptName)
    # Give time for OS to lay down file above
    time.sleep(1)
    os.chmod(scriptName, 0o777)
    if is_windows():
      LogFactory.MAIN_LOG.info("running windows sleeper...")
      Popen([f"{scriptName}"], creationflags=CREATE_NEW_CONSOLE, shell=True)
    else:
      LogFactory.MAIN_LOG.info("running unix sleeper..")
      Popen(['bash', '-c', f"./{scriptName}"])
    LogFactory.MAIN_LOG.info(f"running this script: \n {scriptContent}")
    LogFactory.MAIN_LOG.info(f"rm {scriptName}")
    #os.remove(scriptName)
    exit(0)
  else:
    os.system(f"sudo shutdown +{SHUTDOWN_TIME_MINUTES}")
    exit(0)
