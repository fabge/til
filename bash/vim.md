# Vim

[operator] [number] motion

## Modes

- normal mode (`esc`)
- insert mode (`i`)
- command mode (`:`)
- visual mode (`v`)

`i` -> insert mode  
`I` -> insert at the start of the line
`o` -> open a new line underneath in edit mode  
`shift` + `o` -> open a new line above in edit mode
`a` -> append after the cursor  
`A` -> append at the end of the line
`r` -> replace a single character
`R` -> replace mode
`*` -> go to the next occurrence of the word under the cursor
`#` -> go to the previous occurrence of the word under the cursor
`esc` -> switch from insert mode to command mode

`.` -> repeat the last command
`:` -> switch to ex mode  
`:wq` -> write and quit  
`/` -> different parts/parameters of ex commands are separated by a slash
`:sp` -> split window horizontally
`ctrl` + `w`, `↓` -> switches panes
`%` -> go to matching parenthesis
`f` + `char` -> find/jump to the next occurrence of the character

`ctrl` + `o` -> go to last cursor position/go back to where we were
`ctrl` + `i` -> go to next cursor position/go forward to where we were

`!ls` -> run a shell command, in this case `ls`
`v` + `motion` + `:w test.txt` -> save selection to a test.txt file
`zz` -> center line
`r` + `!ls` or `text.txt` -> replace the current character with the output of the command or the content of the file
`ctrl` + `g` -> show file name, line number/position and percentage of the file
`d` + `i` + `"` -> delete inside the quotes
`d` + `i` + `(` -> delete inside the parenthesis

## Motions

`hjkl` -> correspond to `←↑↓→`

`w` -> to next word

`b` -> back a word

`e` -> to the end of the current word

`$` -> to the end of the line

`0` -> to the start of the line

`gg` -> to the start of a file

`shift` + `g` -> to end of a file

`}` -> to the end of the paragraph (meaning next empty line)

## Operators

`u` -> undo

`U` -> undo all changes on a line

`y` -> copy (yank)
`yw` -> copy a word

`x` -> delete character

`p` -> put (paste) recently copied or deleted text

`r` -> replace, followed by the character to replace the current one

`c` -> change and go into insert mode, followed by the motion, e.g.
    `c$` -> change to the end of the line
    `cw` -> change word

`~` -> changes case (upper to lower and vice versa)

`dd` -> delete line

`.` -> do the same thing again

`/` -> search

`%` -> apply to all lines

`g` -> grep

`s` -> search and replace

`485G` -> go to line 485

## Combinations

`5dd` -> delete 5 lines

`d`, `shift` + `g` -> delete to the end of a file

`d`, `gg` -> delete to the end of a file

`shift` + `p` -> paste above

`2` + `d` + `}` -> delete 2 paragraphs

`%g/^-/d` -> search for all lines starting with a `-` and delete them  
`%g/^\s*$/d` -> search for all lines starting with one or more emtpy spaces followed by the end of the line and delete them  
`%s/ / - /` -> search for all lines with an empty space and replace it with ` - `, applies by default only to the first time it finds it  

`:s/thee/the` -> search for `thee` and replace it with `the`  
`:s/thee/the/g` -> search for `thee` and replace it with `the` globally
`:#,#s/old/new/g` -> search for `old` and replace it with `new` in the range of lines `#` to `#`
`%s/old/new/gc` -> search for `old` and replace it with `new` globally with confirmation
`:!ls` -> run a shell command

`ctrl` + `n` -> next element
`ctrl` + `p` -> previous element
