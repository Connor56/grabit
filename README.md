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

## License

MIT License

[Connor Skelland](https://github.com/Connor56)
