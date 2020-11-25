import os
import textwrap

def desktop_icon_raspbian():
  installLocation=f"{os.getcwd()}"
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

def installer():
  desktop_icon_raspbian()