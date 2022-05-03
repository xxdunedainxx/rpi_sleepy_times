import os
from src.Util import INSTALL_LOCATION, python_location
from kasa import Discover
import asyncio

class KasaAPI:
  KASA_HOSTS: dict = {
    'all' : 'all'
  }
  KASA_ENABLED: bool = True

  def __init__(self):
    pass

  @staticmethod
  async def get_devices():
    devices = await Discover.discover()
    return devices

  @staticmethod
  def init_kasa_api():
    KasaAPI.KASA_HOSTS = {
    }

    devices = asyncio.run(KasaAPI.get_devices())

    for device in devices.keys():
      KasaAPI.KASA_HOSTS[devices[device].alias] = devices[device].host

  @staticmethod
  def kill_kasa_execute(host: str) -> str:
    if host == 'all':
      for key in KasaAPI.KASA_HOSTS.keys():
        os.system(f"kasa --host {KasaAPI.KASA_HOSTS[key]} off &&")
    else:
      os.system(f"kasa --host {KasaAPI.KASA_HOSTS[host]} off")

  @staticmethod
  def kill_kasa_outlet_cmd(host: str) -> str:
    if host == 'all':
      cmdBuild: str = ''
      for key in KasaAPI.KASA_HOSTS.keys():
        cmdBuild+=f"{python_location()} {INSTALL_LOCATION}/cli.py off {KasaAPI.KASA_HOSTS[host]} &&"
      cmdBuild+=' true'
      return cmdBuild
    else:
      return (f"{python_location()} {INSTALL_LOCATION}/cli.py off {KasaAPI.KASA_HOSTS[host]} ")

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