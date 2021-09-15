import asyncio
from kasa import SmartPlug
import sys
from src.LogFactory import LogFactory

async def turnOn(ip: str):
  LogFactory.MAIN_LOG.info(f"turning on {ip}")
  p = SmartPlug(ip)
  await p.turn_on()
  return
if __name__ == "__main__":
  LogFactory.main_log()
  if(len(sys.argv) <= 1):
    LogFactory.MAIN_LOG.error('not enough args!')
    exit(1)
  else:
    ip = sys.argv[1]

    asyncio.run(turnOn(ip))
    exit(0)