import sys
import os

DEBUG = os.environ.get("DEBUG")

def debug(*args):
  if DEBUG: print(*args)


def start():
  print("go")
  fail = 0
  debug(sys.argv)
  forbidden_file = sys.argv[1]
  filenames = sys.argv[2:]
  debug(f"Forbidden words come from: {forbidden_file}")
  debug(f"Operating on files: {filenames}")
  with open(forbidden_file, "r") as f:
    forbidden_words = [x.strip() for x in f.readlines()]
  debug(f"{len(forbidden_words)} forbidden words found: {forbidden_words}")
  for checked_filename in filenames:
    with open(checked_filename, "r") as f:
      file_contents = f.readlines()
      for line, forbidden_word in enumerate(forbidden_words):
        if forbidden_word in file_contents:
          print(f"forbidden word '{forbidden_word}' found in {checked_filename} on line {line+1}")
          fail = 1
  if DEBUG:
    if not fail:
      debug("No forbidden words found! Exiting with error code to print messages.")
    exit(1)
  exit(fail)

start()

# DRAGON
