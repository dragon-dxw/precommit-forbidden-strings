import sys


def start():
  fail = 0
  forbidden_file = sys.argv[1]
  filenames = sys.argv[2:]
  with open(forbidden_file, "r") as f:
    forbidden_words = [x.strip() for x in f.readlines()]
  print(f"{len(forbidden_words)} found")
  for checked_filename in filenames:
    with open(checked_filename, "r") as f:
      file_contents = f.readlines()
      for line, forbidden_word in enumerate(forbidden_words):
        if forbidden_word in file_contents:
          print(f"forbidden word '{forbidden_word}' found in {checked_filename} on line {line+1}")
          fail = 1
  exit(fail)
if __name__ == "__main__":
  start()
