from pathlib import Path

root = Path('.')
index = []
for folder in sorted(root.iterdir()):
    if folder.is_dir() and not folder.as_posix().startswith('.'):
        index.append(f'## {folder}')
        for file in folder.iterdir():
            index.append(f'* [{file.stem}]({file})')
        index.append('\n')

with open('README.md', 'w') as f:
    f.write("\n".join(index))