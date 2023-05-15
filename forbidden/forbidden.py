import sys


def start():
  fail = 0
  forbidden_file = sys.argv[1]
  filenames = sys.argv[2:]
  with open(forbidden_file, "r") as f:
    forbidden_words = [x.strip() for x in f.readlines()]
  for checked_filename in filenames:
    with open(checked_filename, "r") as f:
      file_contents = f.read()
      for forbidden_word in forbidden_words:
        if forbidden_word in file_contents:
          print(f"forbidden word '{forbidden_word}' found in {checked_filename}")
          fail = 1
  exit(fail)
if __name__ == "__main__":
  start()
