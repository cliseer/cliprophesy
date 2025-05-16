# cliprophesy

A CLI tool that suggests commands based on your shell history. Meant to be used by [cliseer-fish](https://github.com/cliseer/cliseer-fish)

## Usage

``` fish
> cliprophesy "echo 'Hello W" --backend cliseer
echo 'Hello World'
cliprophesy "echo 'Hello World'" --backend cliseer
cliprophesy "echo 'Hello World'" --backend openai
```

## Installation

### Option 1: Using pip (or pipx)
``` fish
pip install cliprophesy
```
### Option 2: Using pyinstaller
``` fish
cd cliprophesy/src/cliprophesy
pyinstaller --onefile main.py
```

## Configuration

See configuration information at [cliseer-fish](https://github.com/cliseer/cliseer-fish)

## Privacy Notice

**Important** When invoked the tool sends the following data to the configured AI provider when ran

- Your current and recent shell commands
- Operating system and shell information
- Previous command exit codes

This data may inadvertently include sensitive information such as API keys or passwords if present in your history. Use with care

## Tags

git tag -a v0.1.5 -m "Release version 0.1.5"
git push --tags

## Local development

* Deploying
** rm -rf build/
** python -m build
** python3 -m twine upload --repository testpypi dist/* --verbose

* Developing
** PYTHONPATH=. python cliprophesy/main.py <command> # run from /src
** Use absolute imports

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
