from pathlib import Path

root = Path('.')
index = ['# TIL']
for folder in root.iterdir():
    if folder.is_dir():
        index.append(f'## {folder}')
        for file in folder.iterdir():
            index.append(f'* [{file.name}]({file})')
        index.append('\n')

with open('README.md', 'w') as f:
    f.write("\n".join(index))