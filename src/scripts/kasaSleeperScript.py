import asyncio
from kasa import SmartPlug
import sys

from src.LogFactory import LogFactory

LogFactory.main_log()

async def turnOff(ip: str):
  LogFactory.MAIN_LOG.info(f"shutting down {ip}")
  p = SmartPlug(ip)
  await p.turn_off()
  return
if __name__ == "__main__":
  LogFactory.main_log()
  if(len(sys.argv) <= 1):
    LogFactory.MAIN_LOG.error('not enough args!')
    exit(1)
  else:
    ip = sys.argv[1]
    asyncio.run(turnOff(ip))
    exit(0)