# noCursor()
 
Hides the cursor from view.

## Examples

![noCursor example 1](assets/noCursor1.webp)

```lua
require("L5")

function setup()
  size(100,100)
  windowTitle('noCursor example')
  -- Hide the cursor.
  noCursor()
end

function draw()
  background(200)

  circle(mouseX, mouseY, 10)

  describe('A white circle on a gray background. The circle follows the mouse as it moves. The cursor is hidden.')
end
```

## Related

* [cursor()](cursor.md)
* [describe()](describe.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
