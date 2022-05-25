from pathlib import Path
import re

root = Path('.')
index = []
for folder in sorted(root.iterdir()):
    if folder.is_dir() and not folder.as_posix().startswith('.'):
        index.append(f'## {folder}')
        for file in folder.iterdir():
            with open(file, 'r') as f:
                md = f.read()
            title = re.search('(?<=# ).*(?=\n)', md).group()
            index.append(f'* [{title}]({file})')
        index.append('\n')

with open('README.md', 'w') as f:
    f.write("\n".join(index))