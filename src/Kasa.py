import os
from src.Util import LOCATION_FORMATTED, python_location_formatted

class KasaAPI:
  KASA_HOSTS: dict = {
   'raspberry pi' : '10.0.0.210',
    'fish-light': '10.0.0.100',
    'all' : 'all'
  }
  KASA_ENABLED: bool = True

  def __init__(self):
    pass

  @staticmethod
  def kill_kasa_execute(host: str) -> str:
    if host == 'all':
      for key in KasaAPI.KASA_HOSTS.keys():
        os.system(f"{python_location_formatted()} {LOCATION_FORMATTED}{os.sep}{os.sep}cli.py off {KasaAPI.KASA_HOSTS[key]}")
    else:
      os.system(f"{python_location_formatted()} {LOCATION_FORMATTED}{os.sep}{os.sep}cli.py off {KasaAPI.KASA_HOSTS[host]}")

  @staticmethod
  def kill_kasa_outlet_cmd(host: str) -> str:
    if host == 'all':
      cmdBuild: str = ''
      for key in KasaAPI.KASA_HOSTS.keys():
        cmdBuild+=f"{python_location_formatted()} {LOCATION_FORMATTED}{os.sep}{os.sep}cli.py off {KasaAPI.KASA_HOSTS[host]} &&"
      cmdBuild+=' true'
      return cmdBuild
    else:
      return (f"{python_location_formatted()} {LOCATION_FORMATTED}{os.sep}{os.sep}cli.py off {KasaAPI.KASA_HOSTS[host]}")

  @staticmethod
  def turn_on_kasa_outlet_cmd(host: str) -> str:
    if host == 'all':
      cmdBuild: str = ''
      for key in KasaAPI.KASA_HOSTS.keys():
        cmdBuild+=f"kasa --host {KasaAPI.KASA_HOSTS[key]} on &&"
      cmdBuild+=' true'
      return cmdBuild
    else:
      return (f"kasa --host {KasaAPI.KASA_HOSTS[host]} on")