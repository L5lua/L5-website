# noWindow()

Removes the default canvas.

By default, a 800×600 pixels canvas is created without needing to call
createCanvas(). `noWindow()` removes the
default canvas for sketches that don't need it. No graphics can be drawn. 

**Important: No code in `draw` can continue to run without a window. To have code continue to execute, you must add a `update()` function and place your code there.**

*To stop a continuosly updating program from running you may have to figure out another way to quit your program. If launched from the terminal, you can use control-C to cancel/quit.*

## Examples

```lua
require("L5")

function setup()
  noWindow()
end

function update()
  print("running headless")
end
```

## Related

* [fullscreen()](fullscreen.md)
* [size()](size.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
