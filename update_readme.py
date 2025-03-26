import re
from pathlib import Path

root = Path('.')
readme = ["Things I've learned, collected in [fabge/til](https://github.com/fabge/til).\n\n"]
for folder in sorted(root.iterdir()):
    if folder.is_dir() and not folder.name.startswith(('.', 'assets')):
        readme.append(f'## {folder.name}\n\n')
        for file in sorted(folder.glob('*.md')):
            content = file.read_text()
            title = re.search('# (.*?)\n', content).group(1)
            readme.append(f'* [{title}]({file})\n')
        readme.append('\n')

Path('README.md').write_text(''.join(readme), encoding='utf-8')
