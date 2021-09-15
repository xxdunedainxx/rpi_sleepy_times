import os
import textwrap
import sys
from src.FileIO import FileIO
from src.LogFactory import LogFactory

INSTALL_LOCATION=f"{os.getcwd()}"
LOCATION_FORMATTED=INSTALL_LOCATION.replace(os.sep,f"{os.sep}{os.sep}")

def is_windows():
  return sys.platform == 'win32'

def python_location():
  return sys.executable

def python_location_formatted():
  return python_location().replace(os.sep,f"{os.sep}{os.sep}")

def desktop_icon_raspbian():
  installLocation=INSTALL_LOCATION
  desktopEntryText: str = textwrap.dedent(f"""\
  [Desktop Entry]
  Type=Application
  Name=Sleepy Times
  Exec=python3 {installLocation}/app.py
  Icon={installLocation}/assets/clock.png
  terminal = false""")

  location=f"{os.path.expanduser('~')}/Desktop/RpiSleepy"

  with open(location, "w+") as writer:
    writer.write(desktopEntryText)
    writer.flush()
    writer.close()

def windows_icon_installer():
  LogFactory.MAIN_LOG.info("WINDOWS INSTALLATION")
  installLocation=INSTALL_LOCATION
  create_bat_file(installLocation)
  LogFactory.MAIN_LOG.info(f"mklink \"{os.path.expanduser('~')}/Desktop/Sleepy\" \"{installLocation}/sleepy.bat\"")
  os.system(f"mklink \"{os.path.expanduser('~')}/Desktop/Sleepy\" \"{installLocation}/sleepy.bat\"")

def create_bat_file(loc):
  with open(f"{loc}/sleepy.bat", "w+") as batfile:
    batfile.write("start ms-settings:nightlight")
    batfile.write(f"cd {loc}")
    batfile.write(f"python app.py")

def installer():
  LogFactory.main_log()
  LogFactory.MAIN_LOG.info('start installer')
  if is_windows():
    windows_icon_installer()
  else:
    desktop_icon_raspbian()

def macosx_fix():
  os.environ['QT_MAC_WANTS_LAYER'] = '1'