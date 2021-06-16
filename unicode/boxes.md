I really like using the box drawing characters in monospace files, but looking 
up the correct glyphs is a pain. Here they are, organized so that every glyph 
is next to the typical context where it is used.

Some of these get rendered wrong in a web browser, but I promise that they are 
the correct unicode symbols.

## Box drawing block: `U+2500..U+257F`
Every character from the  range is represented at least once.

### Light
```
┌───┐ ┌─┬─┐ ┌┄┄┄┐ ┌┈┈┈┐ ┌╶──┐ ╭───╮ ╲ ╱
│   │ ├─┼─┤ ┆   ┆ ┊   ┊ ╵   ╷ │   │  ╳
└───┘ └─┴─┘ └┄┄┄┘ └┈┈┈┘ └──╴┘ ╰───╯ ╱ ╲
```
### Double:
```
╔═══╗ ╔═╦═╗ 
║   ║ ╠═╬═╣
╚═══╝ ╚═╩═╝
```
#### Double vs light:
```
╓─╥─╖ ╒═╤═╕
╟─╫─╢ ╞═╪═╡
╙─╨─╜ ╘═╧═╛
```
### Heavy:
```
┏━━━┓ ┏━┳━┓ ┏┅┅┅┓ ┏┉┉┉┓ ┏╺━━┓
┃   ┃ ┣━╋━┫ ┇   ┇ ┋   ┋ ╹   ╻
┗━━━┛ ┗━┻━┛ ┗┅┅┅┛ ┗┉┉┉┛ ┗━━╸┛
```
#### Heavy vs light:
```
┎─┰─┒ ┍━┯━┑ ┌─╼━┓
┠─╂─┨ ┝━┿━┥ ╽   ╿
┖─┸─┚ ┕━┷━┙ ┗━╾─┘
┌─┲━┓ ┌─┬─┐ ┌─┬─┐ ┏━┱─┐
├─╄━┩ ├─╆━┪ ┢━╅─┤ ┡━╃─┤
└─┴─┘ └─┺━┛ ┗━┹─┘ └─┴─┘
┏━┭─┐ ┏━┳━┓ ┏━┳━┓ ┌─┮━┓
┣━╅─┧ ┣━╃─┦ ┞─╄━┫ ┟─╆━┫
┗━┻━┛ ┗━┵─┘ └─┶━┛ ┗━┻━┛
┏━┳━┓ ┌─┮━┓ ┌─┬─┐ ┏━┭─┐ 
┞─╀─┦ ├─┾━┫ ┟─╁─┧ ┣━┽─┤ 
└─┴─┘ └─┶━┛ ┗━┻━┛ ┗━┵─┘ 
┌─┬─┐ ┏━┱─┐ ┏━┳━┓ ┌─┲━┓  
┢━╈━┪ ┣━╉─┤ ┡━╇━┩ ├─╊━┫  
┗━┻━┛ ┗━┹─┘ └─┴─┘ └─┺━┛  
```
