import os
import platform
from typing import List
import dataclasses
import subprocess

def copy_to_clipboard(text: str):
    system = platform.system()
    if system == 'Windows':
        process = subprocess.Popen(['clip'], stdin=subprocess.PIPE)
        process.communicate(input=text.encode('utf-8'))
    elif system == 'Darwin':
        process = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
        process.communicate(input=text.encode('utf-8'))

@dataclasses.dataclass
class File:
    path: str
    contents: str

def recursive_files(
    path: str,
    data: List[File] = [],
) -> List[File]:
    """Get all file paths and context in directory and subdirectories."""
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    for file in files:
        file_path = os.path.join(path, file)

        print(f"Found: {file_path}")
        
        with open(file_path, 'r') as f:
            contents = f.read()
        
        data.append(File(file_path, contents))
    
    for directory in directories:
        recursive_files(os.path.join(path, directory), data)
    
    return data


def prepare_context(path: str) -> str:
    """Prepare context string for an AI to read."""
    files = recursive_files(path)

    context = "Below is a list of all the files in this project and their contents.\n\n"

    for file in files:
        context += f"## `{file.path}`:\n```\n{file.contents}\n```\n\n"

    print("Context prepared, copying to clipboard...")

    copy_to_clipboard(context)
