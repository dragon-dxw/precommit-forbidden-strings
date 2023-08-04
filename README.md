# precommit-forbidden-strings
Check with precommit that particular strings aren't committed

If any strings in `forbidden-strings.txt` are found, the precommit hook fails with error code 13.

If the environment variable `DEBUG` is set, additional diagnostic information will be printed and it will always fail (so you can read the messages.)
