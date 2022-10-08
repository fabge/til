import re
from pathlib import Path

root = Path('.')
readme = ["Things I've learned, collected in [fabge/til](https://github.com/fabge/til).\n\n"]
for folder in sorted(root.iterdir()):
    if folder.is_dir() and not folder.as_posix().startswith(('.', 'assets')):
        readme.append(f'## {folder}\n\n')
        for file in folder.iterdir():
            if file.suffix == '.md':
                with open(file, 'r') as f:
                    md = f.read()
                title = re.search('# (.*?)\n', md).group(1)
                readme.append(f'* [{title}]({file})\n')
        readme.append('\n')

with open('README.md', 'w') as f:
    f.write(''.join(readme))
