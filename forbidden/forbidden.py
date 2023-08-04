import sys
import os

DEBUG = os.environ.get("DEBUG")

def debug(*args):
  if DEBUG: print(*args)

def is_file_ok(checked_filename, forbidden_words):
  """Does this single file contain no forbidden words?"""
  ok = True
  with open(checked_filename, "r") as f:
    file_contents = f.readlines()
  for line_num, line_text in enumerate(file_contents):
    for forbidden_word in forbidden_words:
      if forbidden_word in line_text:
        print(f"forbidden word '{forbidden_word}' found in {checked_filename} on line {line_num+1}")
        print(line_text)
        print()
        ok = False
  return ok

def are_files_ok(filenames, forbidden_words):
  """Iterate over all the filenames: do all of them contain no forbidden words?"""
  ok = True
  for checked_filename in filenames:
    ok = ok and is_file_ok(checked_filename, forbidden_words)
  return ok


def get_word_list(forbidden_file):
  """Return the list of forbidden words from a file"""
  debug(f"Forbidden words come from: {forbidden_file}")
  try:
    with open(forbidden_file, "r") as f:
      return [x.strip() for x in f.readlines()]
  except FileNotFoundError:
    print(f"The forbidden word list '{forbidden_file}' was not found.")
    exit(1)


def start():
  ok = True
  debug(f"sys.argv: {sys.argv}")
  forbidden_file = sys.argv[1]
  filenames = sys.argv[2:]
  try:
    filenames.remove(forbidden_file)
  except ValueError: # if the config file isn't modified, it won't be in the list
    pass
  debug(f"Operating on files: {filenames}")

  forbidden_words = get_word_list(forbidden_file)
  debug(f"{len(forbidden_words)} forbidden words found: {forbidden_words}")
  ok = are_files_ok(filenames, forbidden_words)

  if ok:
    if DEBUG:
      debug("No forbidden words found! Exiting with error code to print messages.")
      exit(1)
    else:
      exit(0)
  else:
    exit(13)
