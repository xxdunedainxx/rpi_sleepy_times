import sys
from src.LogFactory import LogFactory
from src.scripts.kasaOn import turnOn
from src.scripts.kasaSleeperScript import turnOff
import asyncio

LogFactory.main_log()

if (len(sys.argv) <= 2):
  LogFactory.MAIN_LOG.error('not enough args!')
  exit(1)
else:
  method = sys.argv[1]
  methodArg = sys.argv[2]
  LogFactory.MAIN_LOG.info(f"method {method}, arg {methodArg}")
  if method == "on":
    asyncio.run(turnOn(methodArg))
  elif method == "off":
    asyncio.run(turnOff(methodArg))
  else:
    LogFactory.MAIN_LOG.warning(f"method not support {method}")
    exit(1)
  exit(0)