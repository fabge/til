from pathlib import Path
import re

root = Path('.')
readme = ['''
Things I\'ve learned, collected in [fabge/til](https://github.com/fabge/til).
''']
for folder in sorted(root.iterdir()):
    if folder.is_dir() and not folder.as_posix().startswith(('.', 'assets')):
        readme.append(f'## {folder}')
        for file in folder.iterdir():
            if file.suffix == '.md':
                with open(file, 'r') as f:
                    md = f.read()
                title = re.search('# (.*?)\n', md).group(1)
                readme.append(f'* [{title}]({file})')
        readme.append('\n')

with open('README.md', 'w') as f:
    f.write("\n".join(readme))
