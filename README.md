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

## Versioning

Major.Minor.Patch

- Major: Breaking changes.
- Minor: New feature has been added, but backwards compatible.
- Patch: Backwards compatible bug fixes.

## Future Features

- [ ] include ~~and exclude~~ sections in `.grabit`.
- [ ] different titled configurations in the `.grabit` file. i.e. you could have a configuration for getting section A of your app, and another for section B of your app to make it easier to set the configs once and not worry afterwards.
- [ ] add a command line argument option for adding an include or an exclude regex, something like grabit -e "some-regex" or grabit -i "some-regex".
- [ ] include a directory tree in the output as well as the code.
- [x] ~~tell the user the rough number of tokens that have been found across all the files.~~
- [x] ~~predict the number of tokens in a file based on the number of characters in each file.~~
- [ ] if the number of tokens is high, intelligently group files by suffix and prefix and ask the user if they'd like to include or exclude them.
- [ ] ask the user if they'd like to include only a snippet of parts of long files, i.e. first 50 lines or so. Allow them to set this on a per file basis.
- [ ] automatically generate or update the `.grabit` file to reflect the user's choices in the above two features.
- [ ] ask the user if they want to include large directories as well, not just by prefix.
- [ ] add an option for setting up a query on the cli that helps grabit decide how simliar files are to that query and suggest including or discluding based on that. Cursor do something like this, a vector database.
- [ ] store the query inside of the `.grabit` file for faster query re-runs.
- [x] ~~if the files have git history, find the git history of every collected file and add when it was last changed.~~
- [x] ~~taking the above further, optionally add the entire git log of commits for each file, or the last N commits or what have you. This could add extra context for an LLM.~~
- [ ] add an option to include the git diff of each file, or the last N diffs or what have you. This could add even more context for an LLM, an optional argument could be add that switches this on.
- [ ] add the ablity to collect the whole git history of the repo, all the logs, and get the timeline of each log so you can see how frequently a file is changed compared to how many commits have been made in total. This extra information could be used to help decide which files to include or exclude. It could also help the user decide how important a particular file is. Especially if data on recent history is provided.
- [ ] add tests to the package to avoid changes causing failure.
- [x] ~~decide on versioning strategy and add to `README.md`~~
- [ ] add standard configuration setting for `.grabit` files. This will run through their directory and make decisions for them, outputting choices to the terminal for the user to review. e.g. skipping extra large files, or skipping known auto-genned file types like `.dll`.
- [ ] add a terminal based configuration building process that guides users through the various `.grabit` options and lets them build their `.grabit` file via the terminal
- [ ] add an option to set the target number of tokens that grabit should not go over. Then when grabit does go over it will make suggestions underneath the table on what you could do to lower the amount of tokens. If there are embeddings as well, this could be very helpful for figuring out how important different directory paths etc. are.
- [ ] build directory path trees whilst collecting so that more than just the path name can be used to group the directories and find similarities that could be exploited for removing tokens.
- [ ] colour the output that's given to the user depending on size so it's easier to see patterns and make decisions on what to include or disclude.
- [ ] potentially colour the file endings of different file types to also add a visual cue to the user.
- [ ] add an option to order table output by token sizes, last modified by, by order scanned, by file path, and by date last modified.
- [x] ~~add an option for quickly scanning through a directory and getting sizes in bytes very quickly to make choice on inclusion faster.~~
- [ ] improve the option for fast search to include colour coding and ordering by column.

## License

MIT License

[Connor Skelland](https://github.com/Connor56)
