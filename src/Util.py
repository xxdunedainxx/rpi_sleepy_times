import os

def desktop_icon_raspbian():
  installLocation=f"{os.getcwd()}"
  desktopEntryText: str = f"""
  [Desktop Entry]
  Type=Application
  Name=Sleepy Times
  Exec=python3 {installLocation}/app.py
  Icon={installLocation}/assets/clock.png
  terminal = false"""

  location=f"{os.path.expanduser('~')}/Desktop/sleepytimes.desktop"

  with open(location, "w+") as writer:
    writer.write(installLocation)
    writer.flush()
    writer.close()


def installer():
  desktop_icon_raspbian()