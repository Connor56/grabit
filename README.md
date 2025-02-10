<div align="center">
  <img src="https://github.com/user-attachments/assets/c8a8ff17-791e-49e1-a7c6-9a0a37f16fd0" height="300" width="300">
</div>

# grabit

`grabit` is a command-line tool for recursively scanning a directory, extracting file contents, and saving or copying them to the clipboard while respecting `.grabit` ignore rules. The tool helps turn complex projects into LLM input for big context questions.

## Features

- Recursively extracts file contents from a directory.
- Respects `.grabit` ignore files (similar to `.gitignore`).
- Saves extracted content to a file or copies it to the clipboard.
- Works on Windows, macOS, and Linux.

## Installation

Install `grabit` using pip:

```sh
pip install grabit
```

## Usage

### Basic Usage

```sh
grabit /path/to/directory
```

### Save Output to a File

```sh
grabit /path/to/directory -o output.txt
```

### Copy Output to Clipboard

```sh
grabit /path/to/directory -c
```

## Ignore Files

To ignore specific files or patterns, create a `.grabit` file in the root of your project. This works similarly to `.gitignore`.

Example `.grabit`:

```
*.log
__pycache__/
secrets.txt
```

## Example Output

When run, `grabit` will generate a structured output:

```
## `src/main.py`:
``
print("Hello, World!")
``

## `README.md`:
``
# Project Readme
``
```

## Future Features

- [ ] include and exclude sections in `.grabit`.
- [ ] different titled configurations in the `.grabit` file. i.e. you could have a configuration for getting section A of your app, and another for section B of your app to make it easier to set the configs once and not worry afterwards.
- [ ] include a directory tree in the output as well as the code.
- [ ] tell the user the rough number of tokens that have been found across all the files.
- [ ] if the number of tokens is high, intelligently group files by suffix and prefix and ask the user if they'd like to include or exclude them.
- [ ] automatically generate or update the `.grabit` file to reflect the user's choices.
- [ ] ask the user if they want to include large directories as well, not just by prefix.
- [ ] add an option for setting up a query on the cli that helps grabit decide how simliar files are to that query and suggest including or discluding based on that.
- [ ] Store the query inside of the `.grabit` file for faster query re-runs.
- [ ] If the files have git history, find the git history of every collected file and add when it was last changed.
- [ ] Taking the above further, optionally add the entire git log of commits for each file, or the last N commits or what have you. This could add extra context for an LLM.

## License

MIT License

[Connor Skelland](https://github.com/Connor56)
