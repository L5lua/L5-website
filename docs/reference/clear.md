# clear()

Clears the pixels on the canvas.

`clear()` makes every pixel 100% transparent. 

## Examples

![clear example 1](assets/clear1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  describe('A gray square. White circles are drawn as the user moves the mouse. The circles disappear when the user presses the mouse.')
end

function draw()
  circle(mouseX, mouseY, 20)
end

function mousePressed()
  clear()
  background(200)
end
```

## Syntax

```lua
clear()
```

## Related

* [background()](background.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
