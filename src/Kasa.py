import os

class KasaAPI:
  KASA_HOSTS: dict = {
   'raspberry pi' : '10.0.0.210',
    'all' : 'all'
  }
  KASA_ENABLED: bool = True

  def __init__(self):
    pass

  @staticmethod
  def kill_kasa_outlet_cmd(host: str) -> str:
    if host == 'all':
      cmdBuild: str = ''
      for key in KasaAPI.KASA_HOSTS.keys():
        cmdBuild+=f"kasa --host {KasaAPI.KASA_HOSTS[key]} off &&"
      cmdBuild+=' true'
      return cmdBuild
    else:
      return (f"kasa --host {KasaAPI.KASA_HOSTS[host]} off")

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