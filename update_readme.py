from pathlib import Path
import re

root = Path('.')
readme = ['''---
css:
  custom: >-
    @media (prefers-color-scheme: dark) {html {filter: invert(1);}}
---''']
for folder in sorted(root.iterdir()):
    if folder.is_dir() and not folder.as_posix().startswith('.'):
        readme.append(f'## {folder}')
        for file in folder.iterdir():
            with open(file, 'r') as f:
                md = f.read()
            title = re.search('(?<=# ).*(?=\n)', md).group()
            readme.append(f'* [{title}]({file})')
        readme.append('\n')

with open('README.md', 'w') as f:
    f.write("\n".join(readme))



# index = ['''
# <head>
# @media (prefers-color-scheme: dark) {
#     html {
#         filter: invert(1);
#     }
# }
# </head>
# ''']
# for folder in sorted(root.iterdir()):
#     if folder.is_dir() and not folder.as_posix().startswith('.'):
#         index.append(f'<h2>{folder}</h2>')
#         for file in folder.iterdir():
#             with open(file, 'r') as f:
#                 md = f.read()
#             title = re.search('(?<=# ).*(?=\n)', md).group()
#             index.append(f'<li>[{title}]({file})</li>')
#         index.append('<br>')
#     index.append('<br>')

# with open('index.html', 'w') as f:
#     f.write("<br>".join(index))
