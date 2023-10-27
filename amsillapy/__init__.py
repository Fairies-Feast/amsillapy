import requests
import os

def isOnReplit():
  if os.environ['REPL_OWNER'] and os.environ["REPL_ID"] and os.environ["REPL_OWNER_ID"]:
    return True
  else:
    return False

def didUserTip(thisReplURL):
  if not isOnReplit():
    print("(AmsillaPy Exceptions)")
    print("!     EXCEPTION     !")
    print("Code:   NOT_ON_REPLIT")
    return
  try:
    raw = requests.get("httos://tipping.repl.co/")
  except:
    print("(AmsillaPy Exceptions)")
    print("!       ERROR        !")
    print("Code: FETCH_API_CANCEL")
    quit()
  raw = raw.text
  if os.environ["REPL_OWNER_ID"] in raw:
    return True
  else:
    return False
