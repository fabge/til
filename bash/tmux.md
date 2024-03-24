# Tmux

## shortcuts

**windows**

`ctrl` + `b` , `%` -> split vertically

`ctrl` + `b` , `"` -> split horizontally

`ctrl` + `b` , `c` -> create new window

`ctrl` + `b` , `n` -> next window

`ctrl` + `b` , `p` -> previous window

`ctrl` + `b` , `w` -> list windows

`ctrl` + `b` , `&` -> kill window

`ctrl` + `b` , `0-9` -> switch to window 0-9

`ctrl` + `b` , `f` -> find window

`ctrl` + `b` , `,` -> rename window

**panes**

`ctrl` + `b` , `z` -> pane zoom in/out

`ctrl` + `b` , `x` -> kill pane

`ctrl` + `b` , `q` -> show pane numbers

`ctrl` + `b` , `o` -> switch to next pane

`ctrl` + `b` , `arrow` -> switch to pane in arrow direction

`ctrl` + `b` , `space` -> cycle through pane layouts

`ctrl` + `b` , `m` -> maximize (and minimize) pane

`ctrl` + `b` , `!` -> turn pane into new window

**session**

`ctrl` + `b` , `d` -> detach session, leave session running in background

`ctrl` + `b` , `$` -> rename session

## commands

`tmux a` -> attach session

`tmux ls` -> list sessions

`tmux new -s <session_name>` -> create new session

`tmux kill-session -t <session_name>` -> kill session

`tmux attach -t <session_name>` -> attach session

## copy mode

`ctrl` + `b` , `[` -> enter copy mode

`?`-> search upward

`/`-> search downward

use vim binding to navigate

`space` -> start selection

`enter` -> copy selection

`ctrl` + `b` , `]` -> paste selection
