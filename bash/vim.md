# Vim

## Modes

- normal mode
- insert mode
- command mode
- visual mode

`i` -> insert mode  
`o` -> open a new line underneath in edit mode  
`shift` + `o` -> open a new line above in edit mode

`esc` -> switch from insert mode to command mode

`:` -> switch to ex mode  
`:wq` -> write and quit  
`/` -> different parts/parameters of ex commands are separated by a slash
`:sp` -> split window horizontally
`ctrl` + `w`, `↓` -> switches panes

## Motions

`hjkl` -> correspond to `←↑↓→`

`w` -> go to next word

`b` -> go back a word

`gg` -> go to the start of a file

`shift` + `g` -> go to end of a file

`}` -> go to the end of the paragraph (meaning next empty line)

## Commands

`u` -> undo

`y` -> copy (yank)

`x` -> delete character

`p` -> paste

`c` -> change

`~` -> changes case (upper to lower and vice versa)

`dd` -> delete line

`.` -> do the same thing again

`/` -> search

`%` -> apply to all lines

`g` -> grep

`s` -> search and replace

## Combinations

`5dd` -> delete 5 lines

`d`, `shift` + `g` -> delete to the end of a file

`d`, `gg` -> delete to the end of a file

`shift` + `p` -> paste above

`2` + `d` + `}` -> delete 2 paragraphs

`%g/^-/d` -> search for all lines starting with a `-` and delete them  
`%g/^\s*$/d` -> search for all lines starting with one or more emtpy spaces followed by the end of the line and delete them  
`%s/ / - /` -> search for all lines with an empty space and replace it with ` - `, applies by default only to the first time it finds it  
