# precommit-forbidden-strings
Check with precommit that particular strings aren't committed

If any strings in `forbidden-strings.txt` are found, the precommit hook fails with error code 13.

### Installation

Add this to your `.pre-commit-hooks.yaml`

```yaml
repos:
  - repo: https://github.com/dragon-dxw/precommit-forbidden-strings
    rev: "v0.1.0"
    hooks:
      - id: forbidden
```

Then run `pre-commit autoupdate` to update and `pre-commit init` to install.

# Development Tips

`script/demo` runs the local version, rather than the version installed on github.
If the environment variable `DEBUG` is set, additional diagnostic information will be printed and it will always fail (so you can read the messages.)

# The Future

* Regex support
* Turn things off with comments
