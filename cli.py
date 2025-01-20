import os
import platform
import argparse
import dataclasses
import subprocess
from typing import List

def copy_to_clipboard(text: str):
    """Copies text to clipboard based on OS."""
    system = platform.system()
    if system == 'Windows':
        process = subprocess.Popen(['clip'], stdin=subprocess.PIPE)
        process.communicate(input=text.encode('utf-8'))
    elif system == 'Darwin':  # macOS
        process = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
        process.communicate(input=text.encode('utf-8'))

@dataclasses.dataclass
class File:
    path: str
    contents: str

def recursive_files(path: str, data: List[File] = []) -> List[File]:
    """Recursively gets all file paths and contents in a directory."""
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    for file in files:
        file_path = os.path.join(path, file)

        print(f"Found: {file_path}")
        
        try:
            with open(file_path, 'r', encoding="utf-8", errors="ignore") as f:
                contents = f.read()
            data.append(File(file_path, contents))
        except Exception as e:
            print(f"Skipping {file_path}: {e}")

    for directory in directories:
        recursive_files(os.path.join(path, directory), data)
    
    return data

def prepare_context(path: str, output: str = None, to_clipboard: bool = False):
    """Prepares a context string for AI to read, optionally saves or copies it."""
    files = recursive_files(path)

    context = "Below is a list of all the files in this project and their contents.\n\n"

    for file in files:
        context += f"## `{file.path}`:\n```\n{file.contents}\n```\n\n"

    if output:
        with open(output, 'w', encoding="utf-8") as f:
            f.write(context)
        print(f"Context saved to {output}")

    if to_clipboard:
        print("Context copied to clipboard.")
        copy_to_clipboard(context)

    return context

def main():
    """Command-line interface for the script."""
    parser = argparse.ArgumentParser(
        description="Recursively scan a directory, extract file contents, and save/copy them."
    )
    parser.add_argument("directory", type=str, help="The directory to scan")
    parser.add_argument("-o", "--output", type=str, help="File to save extracted content")
    parser.add_argument("-c", "--clipboard", action="store_true", help="Copy output to clipboard")

    args = parser.parse_args()

    prepare_context(args.directory, output=args.output, to_clipboard=args.clipboard)

if __name__ == "__main__":
    main()
